import time
import threading
import os
import sys

try:
    from plyer import notification  # For desktop notifications
except ImportError:
    print("Missing dependency: plyer. Install it using 'pip install plyer'")
    sys.exit(1)

def set_reminder(message, delay):
    time.sleep(delay)
    try:
        notification.notify(
            title="Reminder!",
            message=message,
            timeout=10
        )
    except Exception as e:
        print(f"Reminder: {message}")
        print(f"(Notification failed: {e})")

def main():
    print("Simple Reminder - Set your reminders easily!")
    while True:
        message = input("Enter reminder message: ")
        try:
            minutes = float(input("Enter time in minutes: "))
            seconds = int(minutes * 60)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        threading.Thread(target=set_reminder, args=(message, seconds)).start()
        print(f"Reminder set for {minutes} minutes.\n")

if __name__ == "__main__":
    main()
