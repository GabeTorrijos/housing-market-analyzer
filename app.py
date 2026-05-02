from flask import Flask, render_template, jsonify
import requests
import pandas as pd
import numpy as np
from scipy import stats

app = Flask(__name__)

PIPELINE_URL = "https://housing-data-pipeline.onrender.com/api/all-data"

LABELS = {
    "Median Home Price": "Median Home Price",
    "30-Year Mortgage Rate": "30-Year Mortgage Rate",
    "Housing Starts": "Housing Starts",
    "Home Ownership Rate": "Home Ownership Rate"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def get_data():
    response = requests.get(PIPELINE_URL)
    raw = response.json()

    dfs = {}
    for label, records in raw.items():
        df = pd.DataFrame(records)
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        df = df.dropna()
        df = df.set_index("date")
        dfs[label] = df

    combined = pd.concat(dfs, axis=1)
    combined.columns = combined.columns.droplevel(1)
    combined = combined.dropna()

    corr = combined.corr().round(3)

    chart_data = {}
    for label, df in dfs.items():
        df_reset = df.reset_index()
        chart_data[label] = {
            "labels": df_reset["date"].tolist(),
            "values": df_reset["value"].tolist(),
            "label": label
        }

    insights = []
    keys = list(dfs.keys())
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            a, b = keys[i], keys[j]
            if a in combined.columns and b in combined.columns:
                r, p = stats.pearsonr(combined[a], combined[b])
                strength = "strong" if abs(r) > 0.7 else "moderate" if abs(r) > 0.4 else "weak"
                direction = "positive" if r > 0 else "negative"
                insights.append(f"{a} and {b} have a {strength} {direction} correlation (r = {r:.2f}).")

    return jsonify({
        "correlation": corr.to_dict(),
        "chart": chart_data,
        "insights": insights,
        "columns": keys,
        "labels": LABELS
    })

if __name__ == "__main__":
    app.run(debug=True)