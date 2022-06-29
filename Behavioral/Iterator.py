from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
    _position: int = None

    def __init__(self, collection: Alerts) -> None:
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()
        return value


class Alerts(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = Alerts()
    collection.add_item("Alert 1")
    collection.add_item("Alert 2")
    collection.add_item("Alert 3")

    print("Alerts:")
    print("\n".join(collection))
    print("")
