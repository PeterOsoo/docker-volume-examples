from flask import Flask, request
import os
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
                    formatted_logs.append(line.strip())

        # Reverse order (latest first)
        formatted_logs.reverse()

        # Add numbering
        numbered_logs = [f"{idx+1}. {log}" for idx, log in enumerate(formatted_logs)]

        # Create HTML response
        html_output = "<h3>Log Entries:</h3><p>" + "<br>".join(numbered_logs) + "</p>"
        html_output += "<br><form action='/clear' method='POST'><button type='submit'>Clear Logs</button></form>"
        return html_output

    except FileNotFoundError:
        return "No logs yet. <br><form action='/clear' method='POST'><button type='submit'>Clear Logs</button></form>"

@app.route('/clear', methods=['POST'])
def clear_logs():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    return "<p>Logs cleared!</p><a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
