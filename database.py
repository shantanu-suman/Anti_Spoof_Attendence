import csv
from datetime import datetime
import os

LOG_FILE = 'data/attendance_log.csv'

def log_attendance(name):
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Timestamp'])

    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([name, timestamp])
