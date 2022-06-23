from abc import ABC, abstractmethod


class IHeadphones(ABC):
    @abstractmethod
    def create_headphones(self):
        pass


class Headphones(IHeadphones):
    def create_headphones(self):
        return 'Headphones create'


class Proxy(IHeadphones):

    def __init__(self, headphones: Headphones):
        self.headphones = headphones

    def create_headphones(self):
        return 'It`s a proxy:\n' + self.headphones.create_headphones()


if __name__ == "__main__":
    headphones = Headphones()
    proxy = Proxy(headphones)
    print(proxy.create_headphones())
