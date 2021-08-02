from abc import ABCMeta, abstractclassmethod


class ISubscriber(metaclass=ABCMeta):
    pass


class Subscriber1(ISubscriber):
    def __init__(self, name):
        self.name = name

    def message(self, message):
        print(f"This is the message: {message}")


class Subscriber2(ISubscriber):
    def __init__(self, name):
        self.name = name

    def message2(self, message):
        print(f"This is the different message: {message}")


class Publisher:
    def __init__(self):
        self.subscribers = dict()

    def register(self, subscriber: ISubscriber, callback=None):
        self.subscribers[subscriber] = callback

    def unregister(self, subscriber: ISubscriber):
        del self.subscribers[subscriber]

    def publish(self, message):
        for _, callback in self.subscribers.items():
            callback(message)

if __name__ == "__main__":
    sub1 = Subscriber1('Afif')
    sub2 = Subscriber2('Noisshhh')
    sub3 = Subscriber1('Uncle Bob')

    publisher = Publisher()

    publisher.register(sub1, sub1.message)
    publisher.register(sub2, sub2.message2)
    publisher.register(sub3, sub1.message)

    publisher.publish("Event One")
