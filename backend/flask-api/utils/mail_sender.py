from flask_mail import Mail, Message
from flask import current_app
from bs4 import BeautifulSoup
from xhtml2pdf import pisa
from io import BytesIO
from weasyprint import HTML

from db import email_templates


from models.orders import OrdersModel
from models.address import AddressModel
from models.payment_card import CardModel
from models.book import BookModel

import copy

class MailSender():

    @classmethod
    def send_contact_response_mail(cls, target, full_name, contact_query, response):
        html = open(email_templates["response_template"])

        parser = BeautifulSoup(html, 'lxml')
        parser.find(id="UserName").contents[0].replaceWith(full_name + ",")
        parser.find(id="AdminResponse").contents[0].replaceWith(response)
        parser.find(id="UserQuery").contents[0].replaceWith(contact_query)

        current_app.config['MAIL_DEFAULT_SENDER'][0] = "Equipo de consultas Booken"
        mail = Mail(current_app)

        msg = Message("Consulta Booken",
                      recipients=[target],
                      html=parser)

        with mail.connect() as connection:
            connection.send(msg)

    @classmethod
    def send_ticket_order_mail(cls, target, order: OrdersModel):
        card = CardModel.find_by_id(order.card_id)
        address = AddressModel.find_by_id(order.address_id)

        html = open(email_templates["ticket_template"])

        parser = BeautifulSoup(html, 'lxml')

        # Añadimos la fecha del pedido
        parser.find(id="order_date").contents[0].replaceWith(order.date)
        #parser.find(id="order_id").contents[0].replaceWith("Pedido " + order.date[-4:] + "-" + str(order.id) + "QRL 02154")
        parser.find(id="order_id").contents[0].replaceWith("Pedido " + "2020" + "-" + str(order.id) + " QRL 02154")

        # Añadimos los productos con su respectiva cantidad y precio
        products = parser.find(id="products")
        all_products = parser.find(id="all_products")
        tmp = copy.copy(products.findChildren('p', recursive=False)) # 0: Quant x Book Title / 1: Price
        products.contents = []
        all_products.contents = []
        for art in order.articles:
            book_title = BookModel.find_by_id(art.book_id).name
            tmp_products = copy.copy(products)

            quant, price = copy.copy(tmp[0]), copy.copy(tmp[1])
            quant.contents[0].replaceWith(str(art.quant) + " x " + book_title)
            price.contents[0].replaceWith(str(art.price) + "€")
            tmp_products.append(quant)
            tmp_products.append(price)
            all_products.append(tmp_products)

        # Añadimos el tipo de envio con su respectivo precio
        sending = parser.find(id="send_type").findChildren('p', recursive=False)
        send_type, price = sending[0], sending[1]  # 0: 1 x Envio / 1: Price

        envio = "1 x "
        if order.send_type == 1:
            envio += "Envío Estándard"
        elif order.send_type == 2:
            envio += "Envío Estándard Plus"
        else:
            envio += "Envío Ultra Express"

        send_type.contents[0].replaceWith(envio)
        price.contents[0].replaceWith(str(order.shipping) + "€")

        # Añadimos los impuestos
        taxes = parser.find(id="taxes")
        taxes.contents[0].replaceWith(str(order.taxes) + "€")

        # Añadimos el precio total
        totals = parser.find(id="totals").findChildren('p', recursive=False)
        n_articles, t_price = totals[0], totals[1] # 0: Total n articles / 1: Total price

        n_articles.contents[0].replaceWith("Total "+ str(len(order.articles)) + " artículo/s")
        t_price.contents[0].replaceWith(str(order.total) + "€")

        # Añadimos tambien el precio en pesetas
        pesetas = parser.find(id="pesetas")
        pesetas.contents[0].replaceWith("En pesetas : " + str(round(order.total*166.386,2)) + " ptas")

        # Añadimos la dirección de envio
        direction = parser.find(id="dirección").findChildren('p', recursive=False)
        name, street, cp, telf = direction[0], direction[1], direction[2], direction[3]

        name.contents[0].replaceWith(address.name + " " + address.surnames)
        street.contents[0].replaceWith(address.street + ", " + str(address.number))
        cp.contents[0].replaceWith(str(address.cp) + ", " + address.province)
        telf.contents[0].replaceWith("Tfno: " + str(address.telf))

        # Añadimos la tarjeta con la que se realizó el pago
        method = parser.find(id="vendor")
        method.contents[0].replaceWith(card.payment_method + " **** **** **** " + str(card.number)[-4:])

        # Generamos el pdf
        pdf = BytesIO()

        HTML(string=str(parser)).write_pdf(target=pdf)

        current_app.config['MAIL_DEFAULT_SENDER'][0] = "Pedido de Booken"
        mail = Mail(current_app)

        msg = Message("Pedido de Booken",
                      recipients=[target])

        msg.attach("ticket.pdf", "ticket/pdf", pdf.getvalue())

        with mail.connect() as connection:
            connection.send(msg)

        del pdf
