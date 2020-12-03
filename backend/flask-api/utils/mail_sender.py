from flask_mail import Mail, Message
from flask import current_app
from bs4 import BeautifulSoup

class MailSender():

    @classmethod
    def send_contact_response_mail(cls, target, full_name, contact_query, response):
        try:
            html = open("utils/email_templates/contact_response_email.html")
        except FileNotFoundError as e:
            print(e)
            return 500

        parser = BeautifulSoup(html, 'lxml')
        parser.find(id="UserName").contents[0].replaceWith(full_name + ",")
        parser.find(id="AdminResponse").contents[0].replaceWith(response)
        parser.find(id="UserQuery").contents[0].replaceWith(contact_query)

        current_app.config['MAIL_DEFAULT_SENDER'][0] = "Equipo de consultas Booken"
        mail = Mail(current_app)

        msg = Message("Consulta Booken",
                      recipients=[""],
                      html=parser)

        with mail.connect() as connection:
            connection.send(msg)

