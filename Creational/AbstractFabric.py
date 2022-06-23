from __future__ import annotations
from abc import ABC, abstractmethod


class Tableware_Factory(ABC):
    @abstractmethod
    def create_cup(self):
        pass

    @abstractmethod
    def create_plate(self):
        pass


class Minimalism_Tableware_Factory(Tableware_Factory):
    def create_cup(self) -> Cup:
        return Minimalism_Cup()

    def create_plate(self) -> Plate:
        return Minimalism_Plate()


class Baroque_Tableware_Factory(Tableware_Factory):
    def create_cup(self) -> Cup:
        return Baroque_Cup()

    def create_plate(self) -> Plate:
        return Baroque_Plate()


class Cup(ABC):
    @abstractmethod
    def info(self) -> str:
        pass


class Plate(ABC):
    @abstractmethod
    def info(self) -> str:
        pass


class Minimalism_Cup(Cup):

    def info(self) -> str:
        return 'It`s Minimalism_Cup'


class Minimalism_Plate(Plate):

    def info(self) -> str:
        return 'It`s Minimalism_Plate'


class Baroque_Cup(Cup):

    def info(self) -> str:
        return 'It`s Baroque_Cup'


class Baroque_Plate(Plate):

    def info(self) -> str:
        return 'It`s Baroque_Plate'


def client(factory: Tableware_Factory):
    cup = factory.create_cup()
    plate = factory.create_plate()

    print(cup.info())
    print(plate.info())


client(Minimalism_Tableware_Factory())
client(Baroque_Tableware_Factory())
