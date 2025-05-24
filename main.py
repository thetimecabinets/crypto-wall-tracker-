from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/orders')
def get_orders():
    path = os.path.join(os.path.dirname(__file__), 'orders.json')
    with open(path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
