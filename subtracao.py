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
        data = data_request['data']
        data = data[1:-1].replace(' ', '').split(',')
        
        if len(data) > 1:
            result = int(data[0])
            argumento = ''
            for num in range(1, len(data)):
                result -= float(data[num])

                argumento += str(data[num])
                if num != len(data) - 1: argumento += ' - '

            return jsonify({ 'argumento': argumento, 'resultado': result })
        
        else: 
            return jsonify({ 'erro': 'mais de um valor deve ser inserido para a subtracao' }), 200

    except Exception as error:
        res = {'error': str(error)}
        return jsonify(res), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)