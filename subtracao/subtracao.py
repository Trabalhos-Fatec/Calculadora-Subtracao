from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib import parse

app = Flask(__name__)
CORS(app)

@app.route('/subtracao', methods=['POST'])
def index():
    try:
        data_request = request.get_data()
        data_request = dict(parse.parse_qsl(data_request.decode('utf8')))

        v1 = data_request['v1']
        v2 = data_request['v2']
        
        if v1 and v2:
            argumento = data_request['v1'] + '-' + data_request['v2']
            return jsonify({ 'argumento': argumento, 'resultado': v1 - v2 })
        
        else: 
            return jsonify({ 'erro': 'os campos v1 e v2 sao obrigatorios' }), 400

    except Exception as error:
        res = {'error': str(error)}
        return jsonify(res), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)