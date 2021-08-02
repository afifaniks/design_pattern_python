from abc import ABCMeta, abstractmethod


class EmailSender(metaclass=ABCMeta):
    @abstractmethod
    def verify_email(self, email_from, email_to):
        pass

    @abstractmethod
    def validate(self, body):
        pass

    @abstractmethod
    def send(self, email_from, email_to, body):
        pass

    def send_email(self, email_from, email_to, body):
        self.verify_email(email_from, email_to)
        self.validate(body)
        self.send(email_from, email_to, body)


class GmailSender(EmailSender):
    def verify_email(self, email_from, email_to):
        print("Email Verified")

    def validate(self, body):
        print("Email validated")

    def send(self, email_from, email_to, body):
        print("Sending ...")


class YmailSender(EmailSender):
    def verify_email(self, email_from, email_to):
        print("Y Email Verified")

    def validate(self, body):
        print("Y Email validated")

    def send(self, email_from, email_to, body):
        print("Y Sending ...")


gmail = GmailSender()
gmail.send_email("xx@ymail.com", "gg@ez.com", "body")


ymail = YmailSender()
ymail.send_email("xx@ymail.com", "gg@ez.com", "body")
