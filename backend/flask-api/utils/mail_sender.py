from flask_mail import Mail, Message
from flask import current_app
from bs4 import BeautifulSoup

from db import email_templates

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
