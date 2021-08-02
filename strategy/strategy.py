from abc import ABC


class RefactorStrategy(ABC):
    def refactor(self):
        pass


class RefactorToHTML(RefactorStrategy):
    def refactor(self):
        print("Converted to HTML")


class RefactorToMD(RefactorStrategy):
    def refactor(self):
        print("Converted to Markdown")


class Context:
    def __init__(self, strategy: RefactorStrategy):
        self.refactor_strategy = strategy

    def refactor(self):
        self.refactor_strategy.refactor()


if __name__ == "__main__":
    md_strategy = Context(RefactorToMD())
    md_strategy.refactor()
