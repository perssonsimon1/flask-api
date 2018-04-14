from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

from app import firebase
from app.api import acc
