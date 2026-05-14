import requests
from datetime import datetime

TOKEN = "YOUR_NEW_TOKEN"
CHAT_ID = "7288678832"

def send_telegram():

```
now = datetime.now().strftime("%d/%m/%Y %H:%M")

message = f"""
```

📈 AI STOCK BOT
{now}

CPALL
🟢 Buy: 60–60.5

ADVANC
🟢 Buy: 288–290

AOT
🟢 Buy: 68–69

PTTEP
🟢 Buy: 152–154

WHA
🟢 Buy: 5.40–5.45

₿ BTC/USD
🟢 Buy: realtime
"""

```
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
```

send_telegram()
