from flask import Flask
from datetime import datetime

app = Flask(__name__)

DATA_FILE = '/shared/log.txt'

@app.route('/')
def read_log():
    try:
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()

        formatted_logs = []
        for line in lines:
            if line.startswith("Writer: "):
                timestamp_str = line.replace("Writer: ", "").strip()
                try:
                    timestamp = datetime.fromisoformat(timestamp_str)
                    formatted_logs.append(timestamp.strftime("%I:%M %p %d %b %Y"))
                except ValueError:
                    formatted_logs.append(line.strip())  # fallback for invalid format

        formatted_output = "<br>".join(formatted_logs)
        return f"<h3>Log Entries:</h3><p>{formatted_output}</p>"

    except FileNotFoundError:
        return "No logs yet."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
