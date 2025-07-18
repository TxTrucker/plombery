from plombery import pipeline, task, schedule
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1394869114929152211/P9doWe7xkwO_UGrg3_wr1X9jnbDF91MswkeiA5tsBttfCIodOZK-Ck5_fObCAkJDQTpp"

def send_to_discord(message: str):
    payload = { "content": message }
    requests.post(WEBHOOK_URL, json=payload)


@pipeline(schedule=schedule.daily(hour=910, minute=19))
def breakthrough_checkin():
    @task()
    def run_bot():
        message = "✅ BreakthroughBot checking in... 🌫️ Daily vibe in motion. Steady support, quiet strength."
        
        print(message)
        if __name__ == "__main__":
    send_to_discord("⚡ Test message from BreakthroughBot")

    if __name__ == "__main__":
    message = "⚡ Manual test from BreakthroughBot"
    print(message)
    send_to_discord(message)

    response = requests.post(WEBHOOK_URL, json=payload)
print(response.status_code)
print(response.text)
