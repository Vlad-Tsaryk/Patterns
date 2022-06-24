from datetime import datetime


class Memento:
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:

        return self._state

    def get_name(self) -> str:

        return f"{self._date}: {self._state}"

    def get_date(self) -> str:
        return self._date

class Player:
    _state = None

    def __init__(self, state: list = [0,0]) -> None:
        self._state: list  = state
        print(f"Player: My coords: {self._state}")

    def move(self,x,y):
        self._state = [x,y]
        print(f'Set coords: {x,y}')

    def save(self) -> Memento:

        return Memento(self._state)

    def restore(self, memento: Memento) -> None:

        self._state = memento.get_state()
        print(f"Player: My coords has changed to: {self._state}")



class Game:

    def __init__(self, palyer: Player) -> None:
        self._mementos = []
        self._player = palyer

    def backup(self) -> None:
        print("\nGame: Saving Originator's state...")
        self._mementos.append(self._player.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Game: Restoring state to: {memento.get_name()}")
        try:
            self._player.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Game: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    player = Player([0,0])
    game = Game(player)

    game.backup()
    player.move(1,0)

    game.backup()
    player.move(15,6)

    game.backup()
    player.move(12,8)
    game.backup()

    print()
    game.show_history()

    print("\nClient: Now, let's rollback!\n")
    game.undo()

    print("\nClient: Once more!\n")
    game.undo()
    game.undo()
