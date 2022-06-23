from threading import Lock, Thread


class Meta(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class DataBase(metaclass=Meta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def get_value(self):
        print(self.value)


def test(value: str) -> None:
    singleton = DataBase(value)
    singleton.get_value()


if __name__ == "__main__":

    p1 = Thread(target=test, args=('P1',))
    p2 = Thread(target=test, args=('P2',))
    p1.start()
    p2.start()
