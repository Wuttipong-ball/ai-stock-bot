import os
import requests
from datetime import datetime

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def generate_stock_signal():

    today = datetime.now().strftime("%d/%m/%Y %H:%M")

    message = f"""
📈 AI QUANT TERMINAL {today}
"""

    return message


def send_telegram():

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": generate_stock_signal()
        }
    )

    print(response.text)


send_telegram()
