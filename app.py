from flask import Flask, request
from flask_cors import CORS, cross_origin
from primary_color import extract_primary_color
app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/hello", methods=['GET'])
def hello_world():
    return "Hello, World!"

@app.route("/primary-color", methods=['GET'])
@cross_origin()
def primary_color_from_url():
    rgb = extract_primary_color(request.args['img_url'])

    return app.json.response(rgb)