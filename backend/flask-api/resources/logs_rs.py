from flask_restful import Resource
from models.log import LogModel


class LoginLogs(Resource):

    def get(self):
        return {"logs": [l.json() for l in LogModel.query.all()]}
