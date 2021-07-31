# Breaks LSP
class User:
    def __init__(self, name):
        self.name = name

    def can_view(self):
        pass

    def can_edit(self):
        pass

    def get_storage(self):
        pass


class Moderator(User):
    def __init__(self, name):
        User.__init__(self, name)

    def can_edit(self):
        return True

    def can_view(self):
        return True

    def get_storage(self):
        return "10GB"


class Viewer(User):
    def __init__(self, name):
        User.__init__(self, name)

    def can_edit(self):
        return False

    def can_view(self):
        return True

    def get_storage(self):
        raise Exception("Viewer has no storage")

# x = Moderator("Babe")
# print(x.get_storage())

# y = Viewer("Afif")
# print(y.get_storage())


# Refactor
class StoragePermission:
    def get_storage(self):
        pass


class RefactorUser:
    def __init__(self, name):
        self.name = name

    def can_view(self):
        pass

    def can_edit(self):
        pass


class RefactorModerator(RefactorUser, StoragePermission):
    def __init__(self, name):
        RefactorUser.__init__(self, name)

    def can_edit(self):
        return True

    def can_view(self):
        return True

    def get_storage(self):
        return "10GB"


class RefactorViewer(RefactorUser):
    def __init__(self, name):
        User.__init__(self, name)

    def can_edit(self):
        return False

    def can_view(self):
        return True

x = RefactorModerator("Babe")
print(x.get_storage())

y = RefactorViewer("Afif")
# No get_storage() method
print(y.get_storage())