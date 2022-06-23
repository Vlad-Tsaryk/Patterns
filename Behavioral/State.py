from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass


class TurnedON(State):

    def volume_up(self):
        print('Volume + 10')

    def volume_down(self):
        print('Volume - 10')


class TurnedOFF(State):

    def volume_up(self):
        print('Now the radio is off, turn it on')

    def volume_down(self):
        print('Now the radio is off, turn it on')


class RadioStation(State):

    def __init__(self, state: State = TurnedOFF()):
        self.state = state

    def set_state(self, state: State):
        self.state = state

    def volume_up(self):
        self.state.volume_up()

    def volume_down(self):
        self.state.volume_down()


if __name__ == "__main__":
    Radio = RadioStation()
    Radio.volume_down()
    Radio.set_state(TurnedON())
    Radio.volume_down()
    Radio.volume_up()
