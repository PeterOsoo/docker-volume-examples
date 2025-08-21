from flask import Flask

app = Flask(__name__)

DATA_FILE = '/shared/log.txt'

@app.route('/')
def read_log():
    try:
        with open(DATA_FILE, 'r') as f:
            content = f.read()
        return f"<pre>{content}</pre>"
    except FileNotFoundError:
        return "No logs yet."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
