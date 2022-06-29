from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Blog(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class TripBlog(Blog):
    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        print(f"Blog: {observer} attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Blog: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        print("\nBlog: I'm writing new blog!.")
        self._state = randrange(0, 10)

        print(f"Blog: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, blog: Blog) -> None:
        pass


class SubscriberObserver(Observer):
    def update(self, blog: Blog) -> None:
        if blog._state < 3:
            print("Subscriber: I read this blog!!")

    def __str__(self):
        return 'Subscriber'


class FanObserver(Observer):
    def update(self, blog: Blog) -> None:
        if blog._state:
            print("Fan: Yhoo new blog")

    def __str__(self):
        return 'Fan'


if __name__ == "__main__":
    subject = TripBlog()

    observer_a = SubscriberObserver()
    subject.attach(observer_a)

    observer_b = FanObserver()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
