from flask import Flask, jsonify
from common.db import create_db_and_tables

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'status': 'ok!'})

if __name__ == '__main__':
    create_db_and_tables()
    app.run(debug=True)