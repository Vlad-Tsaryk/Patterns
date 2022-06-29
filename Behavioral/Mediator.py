from __future__ import annotations
import datetime
import time
from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, message: str) -> None:
        pass


class ChatRoom(Mediator):

    def notify(self, sender: User, message: str) -> None:
        print(f'ChatRoom[{sender.get_name()}]:{message} [{datetime.datetime.now()}]')


class User:
    def __init__(self, name: str, mediator: Mediator):
        self._mediator = mediator
        self.name = name

    def send_message(self, msg: str) -> None:
        print("User send message")
        self._mediator.notify(self, msg)

    def get_name(self) -> str:
        return self.name


if __name__ == "__main__":
    # Клиентский код.
    mediator = ChatRoom()
    usr1 = User('Bob', mediator)
    usr2 = User('Luna', mediator)

    print("ChatRoom:")
    usr1.send_message('Hello')
    time.sleep(1)
    usr2.send_message('Hi')