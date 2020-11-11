from flask_restful import Resource, reqparse
from db import db
from models.book import BookModel
from flask_restful import Resource, reqparse
from db import db
from models.author import AuthorModel
from models.book import BookModel


class BookList(Resource):

    def get(self, genre=None):
        if genre:
            return {'books': [i.json()['book'] for i in BookModel.find_by_genre(genre)]}, 200
        return {'books': [i.json()['book'] for i in db.session.query(BookModel).all()]}, 200


class BookArtist(Resource):

    def get(self, id):
        book = BookModel.find_by_id(id)
        if book:
            return {'Book': book.author.json()}, 200
        return {'message': "Book with ['id': {}] not found".format(id)}, 404


class Book(Resource):

    def get(self, id):
        book = BookModel.find_by_id(id)
        if book:
            return book.json(), 200
        return {'message': "Book with ['id': {}] not found".format(id)}, 404

    def post(self):
        data = self.__parse_request__()
        exists = BookModel.find_by_name(data.get('name'))
        if exists:
            return {'message': "A book with ['name': {}] already exists".format(exists.name)}, 409
        authors = []
        a = AuthorModel.find_by_name(data.get('author_name'))
        if a:
            authors.append(a)
        else:
            new_author = AuthorModel(data.get('author_name'), data.get('author_bd'),
                                     data.get('author_city'), data.get('author_country'))
            authors.append(new_author)
            new_author.save_to_db()
        new_book = BookModel(data.get('isbn'), data.get('name'), authors, data.get('genre'), data.get('year'),
                             data.get('editorial'), data.get('language'), data.get('price'), data.get('synopsis'),
                             data.get('description'), data.get('num_pages'), data.get('cover_type'),
                             data.get('num_sales'), data.get('total_available'), data.get('cover_image_url'),
                             data.get('back_cover_image_url'))
        new_book.save_to_db()
        return new_book.json(), 200

    def delete(self, id):
        book = BookModel.find_by_id(id)
        if not book:
            return {'message': "There is no book with ['id': {}], therefore it cannot be deleted".format(id)}, 404
        book.delete_from_db()
        return {'message': "Book with ['id': {}, 'name': {}] has successfully been"
                           " deleted".format(id, book.name)}, 200

    def put(self, id):
        data = self.__parse_request__()
        exists = BookModel.find_by_id(id)
        if not exists:
            return {'message': "A book with ['id': {}] not found".format(id)}, 404
        authors = []
        a = AuthorModel.find_by_name(data.get('author_name'))
        if a:
            authors.append(a)
        else:
            new_author = AuthorModel(data.get('author_name'), data.get('author_bd'),
                                     data.get('author_city'), data.get('author_country'))
            authors.append(new_author)
            new_author.save_to_db()
        exists.delete_from_db()
        new_book = BookModel(data.get('isbn'), data.get('name'), authors, data.get('genre'), data.get('year'),
                             data.get('editorial'), data.get('language'), data.get('price'), data.get('synopsis'),
                             data.get('description'), data.get('num_pages'), data.get('cover_type'),
                             data.get('num_sales'), data.get('total_available'), data.get('cover_image_url'),
                             data.get('back_cover_image_url'))
        new_book.save_to_db()
        return new_book.json(), 200

    def __parse_request__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('isbn', type=int, required=True, help="Operation not valid: 'ISBN' not provided")
        parser.add_argument('name', type=str, required=True, help="Operation not valid: 'name' not provided")
        parser.add_argument('author_name', type=str, required=True, help="Operation not valid: "
                                                                         "'author_name' not provided")
        parser.add_argument('author_bd', type=str, required=True, help="Operation not valid: 'author_bd' not provided")
        parser.add_argument('author_city', type=str, required=True, help="Operation not valid: "
                                                                         "'author_city' not provided")
        parser.add_argument('author_country', type=str, required=True, help="Operation not valid: "
                                                                            "'author_country' not provided")
        parser.add_argument('genre', type=str, required=True, help="Operation not valid: 'genre' not provided")
        parser.add_argument('year', type=int, required=True, help="Operation not valid: 'year' not provided")
        parser.add_argument('editorial', type=str, required=True, help="Operation not valid: 'editorial' not provided")
        parser.add_argument('language', type=str, required=True, help="Operation not valid: 'language' not provided")
        parser.add_argument('price', type=float, required=True, help="Operation not valid: 'price' not provided")
        parser.add_argument('synopsis', type=str, required=True, help="Operation not valid: 'synopsis' not provided")
        parser.add_argument('description', type=str, required=True, help="Operation not valid: "
                                                                         "'description' not provided")
        parser.add_argument('num_pages', type=int, required=True, help="Operation not valid: 'num_pages' not provided")
        parser.add_argument('cover_type', type=str, required=True, help="Operation not valid: "
                                                                        "'cover_type' not provided")
        parser.add_argument('num_sales', type=int, required=True, help="Operation not valid: 'num_sales' not provided")
        parser.add_argument('total_available', type=int, required=True, help="Operation not valid: "
                                                                             "'total_available' not provided")
        parser.add_argument('cover_image_url', type=str, required=True, help="Operation not valid: "
                                                                             "'cover_image_url' not provided")
        parser.add_argument('back_cover_image_url', type=str, required=True, help="Operation not valid: "
                                                                                  "'back_cover_image_url' not provided")
        return parser.parse_args()
