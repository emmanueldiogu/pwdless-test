from django.core.mail import EmailMessage


class EmailHelper(EmailMessage):
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            to=data['email_to'],
        )
        email.send()
