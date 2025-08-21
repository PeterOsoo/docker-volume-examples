from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = '/shared/log.txt'

@app.route('/')
def write_log():
    os.makedirs('/shared', exist_ok=True)
    with open(DATA_FILE, 'a') as f:
        f.write(f"Writer: {datetime.now()}\n")
    return "Writer updated log file!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
