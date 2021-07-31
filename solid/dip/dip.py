# Breaks DIP
class SendNotification:
    def send_by_email(self):
        print("Sending email ...")


class Sender:
    def notify(self):
        notification_service = SendNotification()
        notification_service.send_by_email()

sender = Sender()
sender.notify()

# Now if we want to add another notification service
# the code will break so ...

# Refactoring
class RefactoredNotifier:
    def send(self): pass


class SendByEmail(RefactoredNotifier):
    def send(self):
        print("Sending Email ...")


class SendBySMS(RefactoredNotifier):
    def send(self):
        print("Sending SMS ...")


class RefactoredSender:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def notify(self):
        self.notification_service.send()

sender2 = RefactoredSender(SendBySMS())
sender2.notify()
