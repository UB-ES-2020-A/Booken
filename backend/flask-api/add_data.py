from data import books
from db import db, create_app
from models.author import AuthorModel
from models.book import BookModel


app = create_app()
app.app_context().push()

# Cleaning database.
meta = db.metadata
for table in reversed(meta.sorted_tables):
    print("add_data> Clearing table %s" % table)
    db.session.execute(table.delete())
db.session.commit()

bookss, authorss = 0, 0
for i in books:
    book = db.session.query(BookModel).filter_by(name=i[1]).first()
    if book:
        break;
    authors = []
    for j in i[2]:
        a = AuthorModel(j[0], j[1], j[2], j[3], j[4])
        authors.append(a)
        db.session.add(a)
        authorss += 1
    book = BookModel(i[0], i[1], authors, i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13])
    bookss += 1
    db.session.add(book)

print("add_data> Added {} new books and {} new authors".format(bookss, authorss))

db.session.commit()
db.session.close()
exit(0)
