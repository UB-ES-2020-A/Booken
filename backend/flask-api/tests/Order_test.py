import unittest
import sys
import json

sys.path.append('../')
from app import setupApp
from db import db

class OrderTest(unittest.TestCase):

    order_info = {
        "date": "29/11/2020",
        "total": 1.,
        "shipping": 1.,
        "taxes": 1.,
        "state": 0,
        "send_type": 0,
        "card_id": 0
    }

    article_order_info = {
        "price": 1.,
        "id_book": 1,
        "quant": 1
    }

    address_order_info = {
        "label_name": "Test",
        "name": "Test",
        "surnames" : "Test",
        "street": "Test",
        "number": 1,
        "cp": "08080",
        "city": "Barcelona",
        "province": "Barcelona",
        "telf": 666666666,
    }

    account_info = {
        "name" : "Test",
        "lastname" : "Test",
        "email" : "prueba@gmail.com",
        "password" : "EsTo123Prueba"
    }

    card_info = {
        "card_owner": "Bender Bending Rodríguez",
        "number": "4475482935309482",
        "date": "02/2558",
        "payment_method": "Visa"
    }

    book_info = {
        "isbn": 12345678910,
        "name": 'Book Test',
        "author_name": 'Kim Follet',
        "author_bd": '10/10/1979',
        "author_city": "BCN",
        "author_country": "Spain",
        "genre": 'HUMANIDADES',
        "year": 2020,
        "editorial": 'Santillana',
        "language": 'Castellano',
        "price": 10.9,
        "synopsis": 'Synopsis',
        "description": 'Descripcion',
        "num_pages": 130,
        "cover_type": 0,
        "num_sales": 0,
        "total_available": 15,
        "cover_image_url": 'asd',
        "back_cover_image_url": 'asd'
    }

    def setUp(self):

        self.app = setupApp().test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        # Executed after each test
        pass

    def test_create_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        response = self.add_order(self.order_info)
        self.assertEqual(response.status_code, 200)


    def test_get_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        response = self.app.get('/order/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_get_orders(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        self.add_order(self.order_info)
        response = self.app.get('/orders', follow_redirects=True)

        order_1 = self.order_info.copy()
        order_2 = self.order_info.copy()

        order_1["id"] = 1
        order_2["id"] = 2

        self.assertEqual(response.status_code, 200)

    def test_put_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        info_put = {
            "state": 1
        }
        response = self.app.put('/order/1', data=info_put,follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)

        response = self.app.delete('/order/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_create_article_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        self.postBook(self.book_info)
        response = self.add_article_order(self.article_order_info)
        self.assertEqual(response.status_code, 200)


    def test_get_article_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        self.postBook(self.book_info)
        self.add_article_order(self.article_order_info)
        response = self.app.get('/article-order/1/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_get_articles_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        response = self.app.get('/articles-order/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_article_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        self.add_article_order(self.article_order_info)
        response = self.app.delete('/article-order/1/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_create_address_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        response = self.add_address_order(self.address_order_info)
        self.assertEqual(response.status_code, 200)

    def test_get_address_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        self.add_address_order(self.address_order_info)
        response = self.app.get('/address-order/1/1', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    def test_get_addresses_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        response = self.app.get('/addresses-order/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_address_order(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        self.add_address_order(self.address_order_info)
        response = self.app.delete('/address-order/1/1', follow_redirects=True)

        self.assertEqual(response.status_code, 201)

    def test_get_order_user(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        response = self.app.get('/order-user/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_order_user(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        response = self.app.delete('/order-user/1/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_get_orders_inprogress(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        response = self.app.get('/orders-state-0/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_orders_send(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        response = self.app.get('/orders-state-1/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_get_orders_received(self):
        self.create_account(self.account_info)
        self.add_card(self.card_info)
        self.add_order(self.order_info)
        response = self.app.get('/orders-state-1/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def add_order(self, info):
        return self.app.post('/order/1',
                             data=info,
                             follow_redirects=True)

    def add_article_order(self, info):
        return self.app.post('/article-order/1',
                             data=info,
                             follow_redirects=True)

    def add_address_order(self, info):
        return self.app.post('/address-order/1/1',
                             data=info,
                             follow_redirects=True)

    def add_card(self, info):
        return self.app.post('/account/1/card',
                             data=info,
                             follow_redirects=True)

    def create_account(self,info):
        return self.register(info)
    def register(self,info):
        return self.app.post('/account',
                             data=info,
                             follow_redirects=True)

    def postBook(self, info):
        return self.app.post('/book', data=info, follow_redirects=True)

if __name__ == '__main__':
    unittest.main()
