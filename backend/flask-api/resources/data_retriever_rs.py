from flask_restful import Resource

from utils.data_retriever import DataRetriever


class Retriever(Resource):

    def get(self, needed_data):
        data_info = DataRetriever.get_data(needed_data)
        return {needed_data: data_info}, 200
