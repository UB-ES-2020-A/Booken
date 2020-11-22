from flask_restful import Resource
from models.wishlist import WishlistModel
from models.accounts import AccountModel
from models.book import BookModel


class Wishlist(Resource):

    def get(self, id_account):
        wl = WishlistModel.find_by_account(id_account)
        if wl:
            return {'List': wl.json()}, 200

    def post(self, id_account, id_book):
        acc = AccountModel.find_by_id(id_account)
        if not acc:
            return {'message': "Account with ['id': {}] not found".format(id_account)}, 404
        book = BookModel.find_by_id(id_book)
        if not book:
            return {'message': "Book with ['id': {}] not found".format(id_book)}, 404
        wl = WishlistModel.find_by_account(id_account)
        if book in wl.books:
            return {'message': "Book with ['id': {}] is already is this wish list".format(id_book)}, 400
        wl.books.append(book)
        wl.save_to_db()
        return {'message': "Book with ['id': {}] added to wish list".format(id_book), 'wl': wl.json()}, 200

    def delete(self, id_account, id_book):
        acc = AccountModel.find_by_id(id_account)
        if not acc:
            return {'message': "Account with ['id': {}] not found".format(id_account)}, 404
        book = BookModel.find_by_id(id_book)
        if not book:
            return {'message': "Book with ['id': {}] not found".format(id_book)}, 404
        wl = WishlistModel.find_by_account(id_account)
        if book not in wl.books:
            return {'message': "Book with ['id': {}] is not in the wish list".format(id_book)}, 400
        wl.books.remove(book)
        wl.save_to_db()
        return {'message': "Book with ['id': {}] removed from wish list".format(id_book)}, 200