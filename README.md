# 🏠 U.S. Housing Market Correlation Analyzer

A Flask web application that fetches live U.S. housing data from my [Housing Data Pipeline API](https://housing-data-pipeline.onrender.com) and performs statistical correlation analysis across 4 Federal Reserve (FRED) datasets.

## 🔴 Live Demo
[View Live App](https://housing-market-analyzer-vlkx.onrender.com)

## 📊 Features
- **4 Individual Trend Charts** — Each dataset plotted with proper units and formatting
- **Correlation Heatmap** — Color-coded matrix showing relationships between all variables
- **Auto-Generated Insights** — Automatically highlights strong/weak positive/negative correlations
- **Live Data** — Pulls fresh data from my Housing Data Pipeline API on every page load
- **Responsive Design** — Works on desktop and mobile

## 📈 Datasets (via FRED)
| Dataset | Series ID | Description |
|---|---|---|
| Median Home Price | MSPUS | U.S. median home sales price (USD) |
| 30-Year Mortgage Rate | MORTGAGE30US | Average fixed mortgage rate (%) |
| Housing Starts | HOUST | New privately-owned housing starts (thousands) |
| Homeownership Rate | RHORUSQ156N | U.S. homeownership rate (%) |

## 🏗️ Architecture
FRED API (Federal Reserve)
→ Housing Data Pipeline API (my live REST API)
→ Housing Market Analyzer (this app)

This project consumes data from my own live microservice rather than calling FRED directly, demonstrating a real-world API consumption pattern.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Data:** Pandas, NumPy, SciPy (Pearson correlation)
- **Frontend:** HTML, CSS, Chart.js
- **Deployment:** Render (free tier)
- **Data Source:** Federal Reserve Economic Data (FRED)

## 🚀 Run Locally
```bash
git clone https://github.com/GabeTorrijos/housing-market-analyzer.git
cd housing-market-analyzer
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
```
Then visit `http://127.0.0.1:5000`

## 🔗 Related Projects
- [Housing Data Pipeline](https://github.com/GabeTorrijos/housing-data-pipeline) — The API that powers this app