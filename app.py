from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/add', methods=['POST'])
def add_coefficient():
    try:
        data = request.get_json()
        a = [float(x.strip()) for x in data['a'].split(',') if x.strip()]
        b = float(data['b'])

        result = [round(val + b, 4) for val in a]
        return jsonify({'result': ', '.join(str(r) for r in result)})

    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
