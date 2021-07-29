class Product:
    def __init__(self, p_type, price):
        self.p_type = p_type
        self.price = price

    def __str__(self):
        return f"Type: {self.p_type}, Price: {self.price}"

# Breaks OCP
class Filter:
    def filter_by_type(self, products, p_type):
        for product in products:
            if product.p_type == p_type:
                yield product

prods = [
    Product('cloth', 1600),
    Product('cloth', 9100),
    Product('shoe', 1020),
    Product('cloth', 2100),
    Product('shoe', 1100)]

print(Filter().filter_by_type(prods, 'cloth'))