from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)


class IphoneHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Lightning":
            return f"Iphone: {request} connection successful"
        else:
            return super().handle(request)


class AndroidHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Type-C":
            return f"Android: {request} connection successful"
        else:
            return super().handle(request)


class OldAndroidHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Micro usb":
            return f"OldAndroid: {request} connection successful"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    for connector in ["Micro usb", "Type-C", "Type-F"]:
        print(f"\nClient: Connector {connector}")
        result = handler.handle(connector)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {connector} was left untouched.", end="")


if __name__ == "__main__":
    iphone = IphoneHandler()
    android = AndroidHandler()
    old_android = OldAndroidHandler()

    iphone.set_next(old_android).set_next(android)
    print("Chain: Iphone > Old_android > Android")

    client_code(iphone)
    print("\n")

    print("SubChain: Old_android > Android")
    client_code(old_android)
