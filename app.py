from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/average', methods=['POST'])
def calculate_average():
    data = request.json
    runs = int(data['runs'])
    matches = int(data['matches'])
    average = runs // matches
    float_average = runs / matches
    return jsonify({
        'average': average,
        'float_average': float_average
    })

if __name__ == '__main__':
    app.run(debug=True)
