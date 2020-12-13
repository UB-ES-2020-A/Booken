from flask_restful import Resource

from models.accounts import auth
from models.log import LogModel


class LoginLogs(Resource):

    @auth.login_required(role='stock_manager')
    def get(self):
        return {"logs": [l.json() for l in LogModel.query.all()]}
