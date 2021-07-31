class Monostate:
    __shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls)
        obj.__dict__ = cls.__shared_state
        return obj


class User(Monostate):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Name: {self.name}'


u1 = User('Anik')
print(u1)
u2 = User('Noishh')

# Should change for both variables
assert u1.name == "Noishh" and u2.name == "Noishh"


