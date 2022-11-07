from flask import Flask
from flask import jsonify
import requests 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def base_url():
    """Base url to test API."""

    response = {
        'response': 'Hello from internal server !!!'
    }

    #return jsonify(response)
    return '<h2>Hello world! from <h1>Internal server</h1> !!! </h2>'




@app.route('/search')
def hello():
    r = requests.get('http://www.google.com')
    return r.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
