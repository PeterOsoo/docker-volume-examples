from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = '/shared/log.txt'

@app.route('/')
def write_log():
    os.makedirs('/shared', exist_ok=True)
    now = datetime.now()
    with open(DATA_FILE, 'a') as f:
        f.write(f"Writer: {now}\n")
    # Format output like: "RD Writer updated log file! at 10:37 PM 22nd Aug 2025"
    formatted_time = now.strftime("%I:%M %p %d %b %Y")
    return f"RD Writer updated log file! at {formatted_time}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
