from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'road_facilities.json')


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    return jsonify(load_data())


@app.route('/add', methods=['POST'])
def add():
    data = load_data()
    item = {
        'lat': float(request.form.get('lat')),
        'lng': float(request.form.get('lng')),
        'description': request.form.get('description', '')
    }
    data.append(item)
    save_data(data)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
