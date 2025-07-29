# alerts.py
import smtplib
from db import get_inventory
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_email(subject, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        body = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, body)

def check_and_alert():
    alerts = []
    for id, name, qty, threshold in get_inventory():
        if qty <= threshold:
            alerts.append(f"⚠️ ALERT: '{name}' is low on stock (Qty: {qty})")

    if alerts:
        msg = "\n".join(alerts)
        send_email("Stock Alert - Smart Inventory", msg)
