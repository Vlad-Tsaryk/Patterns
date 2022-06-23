from __future__ import annotations
from abc import ABC, abstractmethod


class Delivery:
    def __init__(self, strategy: Strategy, weight) -> None:
        self._strategy = strategy
        self._weight = weight

    @property
    def strategy(self) -> Strategy:

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:

        self._strategy = strategy

    def make_a_delivery(self) -> None:

        print("Your delivery is: ")
        result = self._strategy.do_delivery(self._weight)
        print(result)

        # ...


class Strategy(ABC):
    @abstractmethod
    def do_delivery(self, weight):
        pass


class NovaPoshtaStrategy(Strategy):
    def do_delivery(self, weight) -> str:
        time = 2
        if weight > 15:
            time = 5

        return 'Nova Poshta: ' + f'{time} days'


class JustinStrategy(Strategy):
    def do_delivery(self, weight) -> str:
        time = 4
        if weight > 15:
            time = 7
        return 'Justin: ' + f'{time} days'


if __name__ == "__main__":

    context = Delivery(NovaPoshtaStrategy(), weight=16)
    context.make_a_delivery()
    print()
    context.strategy = JustinStrategy()
    context.make_a_delivery()