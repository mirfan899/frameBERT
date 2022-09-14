import os
import sys
import argparse
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
sys.path.append('../')
from frameBERT import frame_parser

app = Flask(__name__)
# CORS(app)
api = Api(app, prefix="/api/v1")

parser = reqparse.RequestParser()
parser.add_argument('text', type=str, location='form', help="provide text for supersenses.")
parser.add_argument('format', type=str, location='form', help="Provide the format you want to get in response i.e. json, conll")

f_parser = frame_parser.FrameParser(model_path="./en/", masking=True, language="en")


class WebService(Resource):
    def get(self):
        return {"message": "Welcome to frameBERT.", "status": 200}

    def post(self):
        args = parser.parse_args()
        print(args)

        if not args['format']:
            result_format = 'graph'
        else:
            result_format = args['format']

        result = f_parser.parser(args['text'], sent_id=False, result_format=result_format)
        return result, 200


api.add_resource(WebService, '/fbert')

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
