
# 📦 Smart AI Inventory System

A simple inventory management system built using Python, Streamlit, SQLite, and basic machine learning for demand forecasting.

## 🔧 Features

- View current inventory
- Add new products
- Update product quantities
- Set and monitor low-stock thresholds
- Email alerts when stock is low
- Predict future demand using linear regression

##  Tech Stack

- Python
- Streamlit (UI)
- SQLite (database)
- scikit-learn (forecasting)
- smtplib (email alerts)

##  Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart-ai-inventory.git
   cd smart-ai-inventory
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your email credentials:
   - Copy `config_sample.py` to `config.py`
   - Fill in your email details (use app password for Gmail)

4. Run the app:
   ```bash
   streamlit run app.py
   ```

##  Important

- **Do NOT push `config.py`, `inventory.db`, or any real data to GitHub.**
- Use `.gitignore` to exclude sensitive files.

## 📩 Email Alerts

Make sure to allow SMTP access in your email settings and use app-specific passwords if required.

## 📊 Forecasting

Forecasting is based on historical inventory CSV data. Make sure `inventory.csv` exists with sufficient entries for accurate predictions.

---

Feel free to contribute or suggest improvements!
