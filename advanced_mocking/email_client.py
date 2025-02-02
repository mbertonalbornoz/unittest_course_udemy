import smtplib


class EmailClient:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_email(self, recipient, subject, body):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(self.email, recipient, message)
        server.quit()


class EmailSender:
    def __init__(self, email_client):
        self.email_client = email_client

    def send_emails(self, recipients, subject, body):
        for recipient in recipients:
            self.email_client.send_email(recipient, subject, body)
