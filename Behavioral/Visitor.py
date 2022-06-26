from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

    def get_price(self):
        pass


class Coffee(Component):

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def accept(self, visitor: Visitor) -> None:
        return visitor.visit(self)

    def get_price(self):
        return self.price


class Bake(Component):

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def accept(self, visitor: Visitor):
        return visitor.visit(self)

    def get_price(self):
        return self.price


class Visitor(ABC):

    @abstractmethod
    def visit(self, item: Component):
        pass


class RegularCustomerVisitor(Visitor):

    def visit(self, item: Component):
        cost = item.get_price()
        if isinstance(item, Coffee):
            cost -= item.price * 0.2
        elif isinstance(item, Bake):
            cost -= item.price * 0.1
        return cost


class FistTimeCustomerVisitor(Visitor):
    def visit(self, item: Component):
        cost = item.get_price()
        if isinstance(item, Coffee):
            cost = item.price
        elif isinstance(item, Bake):
            cost -= item.price * 0.2
        return cost


class VipCustomerVisitor(Visitor):
    def visit(self, item: Component):
        cost = item.get_price()
        if isinstance(item, Coffee):
            cost -= item.price * 0.3
        elif isinstance(item, Bake):
            cost -= item.price * 0.3
        return cost


class Customer:
    def __init__(self, discount: Visitor):
        self._discount = discount
        self.components: List[Component] = []

    def set_components(self, components: List[Component]):
        self.components = components

    def set_discount(self, discount: Visitor):
        self._discount = discount

    def calculate_price(self):
        price = 0
        if self.components:
            for item in self.components:
                price += item.accept(self._discount)
        return price


if __name__ == "__main__":
    discount = RegularCustomerVisitor()
    customer = Customer(discount)
    components = [Coffee('Latte', 88.5), Bake('Cake', 140.9)]
    customer.set_components(components)
    print(f'Regular Customer price: {customer.calculate_price()} UAH')
    customer.set_discount(FistTimeCustomerVisitor())
    print(f'First Time Customer price: {customer.calculate_price()} UAH')
    customer.set_discount(VipCustomerVisitor())
    print(f'VIP Customer price: {customer.calculate_price()} UAH')
