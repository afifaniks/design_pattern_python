class Alloc:
    _instance = None
    def __new__(cls, *args, **kwargs):
        print(cls)
        if not cls._instance:
            cls._instance = super(Alloc, cls).__new__(cls, *args, **kwargs)
        return cls._instance
  
a1 = Alloc()
a2 = Alloc()
print(a1 == a2)