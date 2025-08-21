from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = '/data/log.txt'

@app.route('/')
def index():
    os.makedirs('/data', exist_ok=True)
    with open(DATA_FILE, 'a') as f:
        f.write(f"Visited at {datetime.now()}\n")
    return f"Hello from Named Volume! Data written to {DATA_FILE}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
