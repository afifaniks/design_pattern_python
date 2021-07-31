def singleton(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        print(f'args: {args}')
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        else:
            print('Already exists')

        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loading...')


d1 = Database()
d2 = Database()
print(d1 == d2)