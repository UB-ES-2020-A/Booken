from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import models here


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

#new_author = AuthorModel(id=1, name="Bad Gyal23", country="Spain", genre="TRAP")

# Tancament de la sessio
db.session.close()
exit()
