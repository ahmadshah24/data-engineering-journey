import time
from plyer import notification


while True:
    notification.notify(
        title="Drink Water Reminder",
        message="It's time to drink water! Stay hydrated.",
        timeout=10
    )
    time.sleep(3600)  # Remind every hour (3600 seconds)

