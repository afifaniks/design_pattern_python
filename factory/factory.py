from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def do_something():
        pass


class Man(IPerson):
    def __init__(self):
        self.type = "Maaaan"

    def do_something(self):
        return "Shouting"


class Woman(IPerson):
    def __init__(self):
        self.type = "Whooman"

    def do_something():
        return "Crying"


class PersonFactory:
    @staticmethod
    def build_person(choice):
        if choice == "Man":
            return Man()

        if choice == "Woman":
            return Woman()


if __name__ == "__main__":
    choice = "Man"

    person = PersonFactory.build_person(choice)

    print(person.do_something())
