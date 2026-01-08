import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATTENDANCE_FILE = os.path.join(BASE_DIR, "attendance.csv")

def mark_attendance(user_id):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    file_exists = os.path.exists(ATTENDANCE_FILE)

    with open(ATTENDANCE_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["User ID", "Date", "Time"])

        writer.writerow([user_id, date_str, time_str])

    print(f"✅ Attendance marked for User {user_id}")
