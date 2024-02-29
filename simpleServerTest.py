# server.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask server!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
