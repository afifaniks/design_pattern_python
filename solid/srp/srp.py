# This section gonna break Single Responsibility Principle
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self) -> bool:
        if self.age >= 18:
            return True
        else:
            return False

    # Breaks SRP
    def calculate_payment(self):
        """Payment calculation is not a user's responsibility""" 
        pass


# Solution
class PaymentCalculator:
    def calculate_payment(self, user) -> str:
        return f"Calculated payment for {user.name}"


u = User('Noish', '22')
print(PaymentCalculator().calculate_payment(u))