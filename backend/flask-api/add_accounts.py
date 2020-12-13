# file deepcode ignore W0611: <comment the reason here>
from data import books, users, admin_add, admin_cards
from db import db, create_app
from models.author import AuthorModel
from models.book import BookModel
from models.accounts import AccountModel
from models.orders import OrdersModel
from models.articles import ArticlesModel
from models.review import ReviewModel
from models.address import AddressModel
from models.payment_card import CardModel
from models.wishlist import WishlistModel
from models.interface import InterfaceModel
"""
app = create_app()
app.app_context().push()

card, address = admin_cards[0], admin_add[0]

for i in range(712):
    #email, name, lastname, password):
    n_account = AccountModel("email"+str(i)+"@provider.com", "Pepito", "Numero " + str(i), "pass")
    n_address = AddressModel(address[0], address[1], address[2], address[3], address[4], address[5], address[6], address[7], address[8])
    n_card = CardModel(card[0], card[1], card[2], card[3])
    n_account.cards.append(n_card)
    n_account.addresses.append(n_address)
    db.session.add(n_address)
    db.session.add(n_card)
    db.session.add(n_account)
    print(i)

db.session.commit()
db.session.close()
exit(0)
"""