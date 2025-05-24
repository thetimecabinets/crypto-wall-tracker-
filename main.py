from flask import Flask, jsonify, send_from_directory
import json
import os

# ✅ Create Flask app and point to frontend folder
app = Flask(__name__, static_folder='frontend', static_url_path='')

# ✅ Serve the frontend page (index.html)
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# ✅ Serve the API endpoint with live data
@app.route('/api/orders')
def get_orders():
    # orders.json is still in backend folder
    file_path = os.path.join('backend', 'orders.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)

# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True)

