from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class CopyCommand(Command):

    def __init__(self, screen: Screen) -> None:
        self._screen = screen

    def execute(self) -> None:
        print(self._screen.copy())


class PasteCommand(Command):
    def __init__(self, screen: Screen):
        self._screen = screen

    def execute(self) -> None:
        print(self._screen.paste())


class Screen:
    def __init__(self, text):
        self.text = text

    def copy(self):
        return f'[{self.text}]' + ' fragment copied'

    def paste(self):
        return f'[{self.text}]' + ' fragment pasted'


class Invoker:

    def __init__(self):
        self.history: list[Command] = []

    def add_command(self, command: Command):
        self.history.append(command)

    def do_something_important(self) -> None:
        if not self.history:
            print('Задач нет')
        else:
            for ex in self.history:
                ex.execute()


if __name__ == "__main__":
    invoker = Invoker()
    screen = Screen('Hello i`am test text')
    invoker.add_command(CopyCommand(screen))
    invoker.add_command(PasteCommand(screen))
    invoker.add_command(PasteCommand(screen))
    invoker.add_command(PasteCommand(screen))
    invoker.do_something_important()
