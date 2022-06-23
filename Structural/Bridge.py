from __future__ import annotations
from abc import ABC, abstractmethod


class Tableware(ABC):
    def __init__(self, style: Style):
        self.style = style

    @abstractmethod
    def info(self):
        pass


class Plate(Tableware):

    def info(self):
        return f'Plate in {self.style.styling()} style'


class Glass(Tableware):

    def info(self):
        return f'Glass in {self.style.styling()} style'


class Style(ABC):
    @abstractmethod
    def styling(self):
        pass


class Minimalism(Style):
    def styling(self):
        return 'minimalism'


class Fashion(Style):
    def styling(self):
        return 'fashion'


class Baroque(Style):

    def styling(self):
        return 'baroque'


if __name__ == '__main__':
    print(Plate(Fashion()).info())
    print(Glass(Minimalism()).info())
    print(Plate(Minimalism()).info())
    print(Glass(Baroque()).info())
