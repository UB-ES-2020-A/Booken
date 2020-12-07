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


app = create_app()
app.app_context().push()

# Cleaning database.
meta = db.metadata
for table in reversed(meta.sorted_tables):
    print("add_data> Clearing table %s" % table)
    db.session.execute(table.delete())
db.session.commit()

acc, accc, accd = 0, 0, 0
for c in admin_cards:
    card = CardModel(c[0], c[1], c[2], c[3])
    db.session.add(card)
    accc -= -1

for a in admin_add:
    add = AddressModel(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8])
    db.session.add(add)
    accd -= -1

for i in users:
    user = AccountModel(i[0], i[1], i[2], i[3])
    user.type = i[4]
    if user.type == 2:
        user.cards.append(card)
        user.addresses.append(add)

    db.session.add(user)
    acc -= -1

bookss, authorss = 0, 0
for i in books:
    authors = []
    for j in i[2]:
        a = AuthorModel(j[0], j[1], j[2], j[3])
        authors.append(a)
        db.session.add(a)
        authorss += 1
    book = BookModel(i[0], i[1], authors, i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15])
    bookss += 1
    db.session.add(book)

print("add_data> Added {} new accounts".format(acc))
print("add_data> Added {} new cards".format(accc))
print("add_data> Added {} new addresses".format(accd))
print("add_data> Added {} new books and {} new authors".format(bookss, authorss))

db.session.commit()
db.session.close()
exit(0)
