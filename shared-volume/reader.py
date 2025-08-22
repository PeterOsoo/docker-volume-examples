from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = '/shared/log.txt'

@app.route('/')
def read_log():
    logs = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith("Writer: "):
                timestamp_str = line.replace("Writer: ", "").strip()
                try:
                    timestamp = datetime.fromisoformat(timestamp_str)
                    logs.append(timestamp.strftime("%I:%M %p %d %b %Y"))
                except ValueError:
                    logs.append(line.strip())

    # Reverse order (latest first)
    logs.reverse()
    return render_template('reader.html', logs=logs)

@app.route('/clear', methods=['POST'])
def clear_logs():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    return render_template('clear.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
