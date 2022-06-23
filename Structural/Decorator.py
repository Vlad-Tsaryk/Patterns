from abc import ABC, abstractmethod


class IPerson(ABC):
    @abstractmethod
    def wear(self) -> str:
        pass


class Person(IPerson):
    def wear(self) -> str:
        return 'Pants  '


class Decorator(IPerson):
    person: IPerson = None

    def __init__(self, pers: IPerson) -> None:
        self.person = pers

    def person(self) -> IPerson:
        return self.person

    def wear(self) -> str:
        return self.person.wear()


class Tshirt(Decorator):
    def wear(self) -> str:
        return 'T-shirt  ' + self.person.wear()


class Jacket(Decorator):
    def wear(self) -> str:
        return 'Jacket  ' + self.person.wear()


def client_code(pers: IPerson):
    print(pers.wear())


if __name__ == '__main__':
    person = Person()
    client_code(person)
    dec1 = Tshirt(person)
    client_code(dec1)
    dec2 = Jacket(dec1)
    client_code(dec2)
