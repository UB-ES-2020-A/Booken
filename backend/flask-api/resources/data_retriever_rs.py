from flask_restful import Resource

from models.data_retriever import DataRetriever


class Retriever(Resource):

    def get(self, needed_data):
        data_info = DataRetriever.get_data(needed_data)
        """
        if not data_info:
            return {"message": "Data info not available"}, 404
        """
        return {needed_data: data_info}
