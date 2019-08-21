from flask import Flask , request , jsonify
from flask_restful import Api , Resource
import json
from QueryData.QueryData import QueryData


class ListOfPolls(Resource):
    def __init__(self,**kwargs):
        self.db = kwargs['data']

    def get(self,pageNos):
        current = (pageNos - 1) * 10
        query = "SELECT * FROM poll ORDER BY poll_start_time DESC LIMIT {0},10".format(str(current))
        queryData = QueryData(self.db)
        data = queryData.selectQueryMethod(query)
        return jsonify(data)
        