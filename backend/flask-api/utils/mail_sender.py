from flask_mail import Mail, Message
from flask import current_app
from bs4 import BeautifulSoup
from io import BytesIO
from weasyprint import HTML
from datetime import date, datetime

from db import email_templates

from models.orders import OrdersModel
from models.address import AddressModel
from models.payment_card import CardModel
from models.book import BookModel

import copy

class MailSender():
    parser = None
    pdf = None

    @classmethod
    def send_contact_response_mail(cls, target, full_name, contact_query, response):
        current_app.config['MAIL_DEFAULT_SENDER'][0] = "Equipo de consultas Booken"
        mail = Mail(current_app)

        cls._prepare_contact_response(cls, "contact_response_template", data=dict(
                                                                            full_name=full_name,
                                                                            contact_query=contact_query,
                                                                            response=response
                                                                        ))
        msg = Message("Consulta Booken",
                      recipients=[target],
                      html=cls.parser)

        with mail.connect() as connection:
            connection.send(msg)

    @classmethod
    def send_ticket_order_mail(cls, target, full_name, order: OrdersModel):
        current_app.config['MAIL_DEFAULT_SENDER'][0] = "Pedido de Booken"
        mail = Mail(current_app)

        cls._prepare_ticket_response(cls, "ticket_response_template", data=dict(full_name=full_name))
        msg = Message("Pedido de Booken",
                      recipients=[target],
                      html=cls.parser)

        cls._prepare_ticket_pdf(cls, "ticket_pdf_template", order)
        msg.attach("ticket.pdf", "ticket/pdf", cls.pdf.getvalue())

        with mail.connect() as connection:
            connection.send(msg)

        cls.pdf.close()

    def _get_component(self, component_id):
        return self.parser.find(id=component_id)

    def _replace_content(self, component_id, content):
        self.parser.find(id=component_id).contents[0].replaceWith(content)

    def _replace_component_content(self, component, content):
        component.contents[0].replaceWith(content)

    def _get_copy_children(self, component_id):
        return copy.copy(self.parser.find(id=component_id).findChildren('p', recursive=False))

    def _get_children(self, component_id):
        return self.parser.find(id=component_id).findChildren('p', recursive=False)

    def _prepare_contact_response(self, html_name, data):
        html = open(email_templates[html_name])

        self.parser = BeautifulSoup(html, 'lxml')
        self._replace_content(self, "UserName", data['full_name'] + ",")
        self._replace_content(self, "footeryear", str(datetime.now().year))
        self._replace_content(self, "AdminResponse", data['response'])
        self._replace_content(self, "UserQuery", data['contact_query'])

        html.close()

    def _prepare_ticket_response(self, html_name, data):
        html = open(email_templates[html_name])

        self.parser = BeautifulSoup(html, 'lxml')
        self._replace_content(self, "UserName", data['full_name'] + ",")
        self._replace_content(self, "footeryear", str(datetime.now().year))

        html.close()

    def _prepare_ticket_pdf(self, html_name, order: OrdersModel):
        html = open(email_templates[html_name])
        card = CardModel.find_by_id(order.card_id)
        address = AddressModel.find_by_id(order.address_id)

        self.parser = BeautifulSoup(html, 'lxml')

        # Añadimos la fecha del pedido
        self._replace_content(self, "order_date", order.date)
        self._replace_content(self, "order_id", "Pedido " + str(date.today().strftime("%Y")) + "-" + str(order.id) + " QRL 02154")

        # Añadimos los productos con su respectiva cantidad y precio
        products = self._get_component(self, "products")
        all_products = self._get_component(self, "all_products")
        tmp = self._get_copy_children(self,"products") # 0: Quant x Book Title / 1: Price
        products.contents = []
        all_products.contents = []

        for art in order.articles:
            book_title = BookModel.find_by_id(art.book_id).name
            tmp_products = copy.copy(products)

            quant, price = copy.copy(tmp[0]), copy.copy(tmp[1])

            self._replace_component_content(self, quant, str(art.quant) + " x " + book_title)
            self._replace_component_content(self, price, str(art.price) + "€")

            tmp_products.append(quant)
            tmp_products.append(price)
            all_products.append(tmp_products)

        # Añadimos el tipo de envio con su respectivo precio
        sending = self._get_children(self, "send_type")
        send_type, price = sending[0], sending[1]  # 0: 1 x Envio / 1: Price

        envio = "1 x "
        if order.send_type == 1:
            envio += "Envío Estándard"
        elif order.send_type == 2:
            envio += "Envío Estándard Plus"
        else:
            envio += "Envío Ultra Express"

        self._replace_component_content(self, send_type, envio)
        self._replace_component_content(self, price, str(order.shipping) + "€")

        # Añadimos los impuestos
        self._replace_content(self, "taxes", str(order.taxes) + "€")

        # Añadimos el precio total
        totals = self._get_children(self, "totals")
        n_articles, t_price = totals[0], totals[1] # 0: Total n articles / 1: Total price

        self._replace_component_content(self, n_articles, "Total "+ str(len(order.articles)) + " artículo/s")
        self._replace_component_content(self, t_price, str(order.total) + "€")

        # Añadimos tambien el precio en pesetas
        self._replace_content(self, "pesetas", "En pesetas : " + str(round(order.total*166.386,2)) + " ptas")

        # Añadimos la dirección de envio
        direction = self._get_children(self, "dirección")
        name, street, cp, telf = direction[0], direction[1], direction[2], direction[3]

        self._replace_component_content(self, name, address.name + " " + address.surnames)
        self._replace_component_content(self, street, address.street + ", " + str(address.number))
        self._replace_component_content(self, cp, str(address.cp) + ", " + address.province)
        self._replace_component_content(self, telf, "Tfno: " + str(address.telf))

        # Añadimos la tarjeta con la que se realizó el pago
        self._replace_content(self, "vendor", card.payment_method + " **** **** **** " + str(card.number)[-4:])

        # Generamos el pdf
        self.pdf = BytesIO()

        HTML(string=str(self.parser)).write_pdf(target=self.pdf)

        html.close()
