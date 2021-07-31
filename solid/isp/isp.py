# Somewhat similar to LSP
from abc import abstractmethod
# Breaks ISP
class FullPrinter:
    @abstractmethod
    def print(self, doc):
        pass

    @abstractmethod
    def scan(self, doc):
        pass

class MultipurposePrinter(FullPrinter):
    def print(self, doc):
        print("{doc} - Printing doc")

    def scan(self, doc):
        print("{doc} - Scanning doc")


class OnlyPrinter(FullPrinter):
    def print(self, doc):
        print("{doc} - Printing doc")

    # Violates ISP as this type of printer should not implement scan
    def scan(self, doc):
        raise NotImplementedError(f"{doc} - Scan not supported")

# p = OnlyPrinter()
# p.scan("My doc")

# Refactor
class Printer:
    @abstractmethod
    def print(self, doc):
        pass

class Scanner:
    @abstractmethod
    def scan(self, doc):
        pass

class RefcatoredMultipurposePrinter(Printer, Scanner):
    def print(self, doc):
        print("{doc} - Printing doc")

    def scan(self, doc):
        print("{doc} - Scanning doc")


class RefactoredPrinterOnly(Printer):
    # Implemented only the interfaces it needs
    def print(self, doc):
        print("{doc} - Printing doc")


pp = RefactoredPrinterOnly()
pp.print("Test")