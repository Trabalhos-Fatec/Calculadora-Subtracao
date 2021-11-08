from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/subtracao', methods=['POST'])
def index():
    try:
        v1 = request.json['v1']
        v2 = request.json['v2']
        
        if v1 and v2:
            return jsonify({ 'resultado': v1 - v2 })
        
        else: 
            return jsonify({ 'erro': 'os campos v1 e v2 sao obrigatorios' }), 400

    except Exception as error:
        res = {'error': str(error)}
        return jsonify(res), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)