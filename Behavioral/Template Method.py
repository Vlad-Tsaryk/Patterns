from abc import ABC, abstractmethod


class House(ABC):

    def build_house(self) -> None:
        self.pour_foundation()
        self.build_walls()
        self.lay_roof()
        self.install_windows()
        self.install_doors()
        self.install_air_conditioning()

    def pour_foundation(self) -> None:
        print("Foundation is build")

    def build_walls(self) -> None:
        print("Walls are build")

    def lay_roof(self) -> None:
        print("Roof installed")

    @abstractmethod
    def install_windows(self) -> None:
        pass

    @abstractmethod
    def install_doors(self) -> None:
        pass

    def install_air_conditioning(self):
        pass


class House1(House):

    def install_windows(self) -> None:
        print("Two big window, and one small installed")

    def install_doors(self) -> None:
        print("One door installed")


class House2(House):

    def install_windows(self) -> None:
        print("One small window installed")

    def install_doors(self) -> None:
        print("Five door installed")

    def install_air_conditioning(self):
        print('Air conditioning installed')


def client_code(house: House) -> None:
    house.build_house()


if __name__ == "__main__":
    client_code(House1())
    print("")
    client_code(House2())



