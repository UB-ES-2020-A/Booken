from db import create_app, db
from models.accounts import AccountModel
from models.address import AddressModel
from models.payment_card import CardModel
from data import admin_add, admin_cards


for i in range(2792):


app = create_app()
app.app_context().push()

db.session.commit()
db.session.close()
exit(0)