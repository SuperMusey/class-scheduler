from flask import jsonify, request
from flask_restx import Resource, Api
from app.services.data_handler import handle_data

api = Api()

@api.route('/api/data')
class ClassData(Resource):
    def post(self):
        # data_got is an array of classes
        data_got = request.json
        response = handle_data(dataFromRequest=data_got)
        #response = {'message':'From /api/data'}
        return jsonify(response)
