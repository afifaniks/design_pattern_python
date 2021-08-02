class Target:
    def request(self, text: str) -> str:
        return text[::-1]


class Adaptee:
    def special_request(self, text: str) -> str:
        return text*2


class Adapter(Target, Adaptee):
    def request(self, text):
        return self.special_request(text)


x = Adapter()
print(x.request("Anik"))
        