from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained ML pipeline
model = joblib.load("aadhaar_risk_pipeline.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    result = None

    if request.method == "POST":
        data = {
            "date": request.form["date"],
            "state": request.form["state"],
            "district": request.form["district"],
            "pincode": int(request.form["pincode"]),
            "age_0_5": int(request.form["age_0_5"]),
            "age_5_17": int(request.form["age_5_17"]),
            "age_18_greater": int(request.form["age_18_plus"])
        }

        df = pd.DataFrame([data])

        # Feature Engineering
        df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day
        df['week'] = df['date'].dt.isocalendar().week.astype(int)
        df['day_of_week'] = df['date'].dt.dayofweek
        df['is_weekend'] = df['day_of_week'].isin([5,6]).astype(int)

        df['total_population'] = df['age_0_5'] + df['age_5_17'] + df['age_18_greater']

        df['pct_age_0_5'] = df['age_0_5'] / df['total_population']
        df['pct_age_5_17'] = df['age_5_17'] / df['total_population']
        df['pct_age_18_plus'] = df['age_18_greater'] / df['total_population']

        df = df.sort_values(['pincode','date'])
        df['growth_rate'] = df.groupby('pincode')['total_population'].pct_change().fillna(0)

        df['priority_score'] = (
            0.4*df['pct_age_0_5'] +
            0.4*df['pct_age_5_17'] +
            0.2*(1 - df['pct_age_18_plus'])
        )

        drop_cols = ["date","state","district","pincode","priority_score"]
        df_model = df.drop(columns=drop_cols)

        pred = model.predict(df_model)[0]
        result = "High Risk Region" if pred == 1 else "Low Risk Region"

    return render_template("prediction.html", prediction_result=result)

if __name__ == "__main__":
    app.run(debug=True)
