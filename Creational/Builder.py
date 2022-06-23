from abc import ABC, abstractmethod


class Bicycle:

    def __init__(self):
        self.wheels = None
        self.wheels_diameter = None
        self.shock_absorbers = None
        self.brakes = None

    def __str__(self):
        info = f'Количество колес: {self.wheels}\n' \
               f'Диаметр колес: {self.wheels_diameter}\n' \
               f'Количество амортизаторов: {self.shock_absorbers}\n' \
               f'Тип тормозов: {self.brakes}'
        return info


class Builder(ABC):
    @abstractmethod
    def set_wheels(self):
        pass

    @abstractmethod
    def set_wheels_diameter(self):
        pass

    @abstractmethod
    def set_shock_absorbers(self):
        pass

    @abstractmethod
    def set_brakes(self):
        pass

    @abstractmethod
    def get_bicycle(self) -> Bicycle:
        pass


class Cross_Bicycle_Builder(Builder):

    def __init__(self):
        self.bicycle = Bicycle()

    def set_wheels(self):
        self.bicycle.wheels = 2

    def set_wheels_diameter(self):
        self.bicycle.wheels_diameter = 28

    def set_shock_absorbers(self):
        self.bicycle.shock_absorbers = 1

    def set_brakes(self):
        self.bicycle.brakes = 'Дисковые'

    def get_bicycle(self) -> Bicycle:
        return self.bicycle


class Mountain_Bicycle_Builder(Builder):

    def __init__(self):
        self.bicycle = Bicycle()

    def set_wheels(self):
        self.bicycle.wheels = 2

    def set_wheels_diameter(self):
        self.bicycle.wheels_diameter = 26

    def set_shock_absorbers(self):
        self.bicycle.shock_absorbers = 2

    def set_brakes(self):
        self.bicycle.brakes = 'Дисковые'

    def get_bicycle(self) -> Bicycle:
        return self.bicycle


class Kids_Bicycle_Builder(Builder):

    def __init__(self):
        self.bicycle = Bicycle()

    def set_wheels(self):
        self.bicycle.wheels = 3

    def set_wheels_diameter(self):
        self.bicycle.wheels_diameter = 12

    def set_shock_absorbers(self):
        self.bicycle.shock_absorbers = 0

    def set_brakes(self):
        self.bicycle.brakes = 'Ободные'

    def get_bicycle(self) -> Bicycle:
        return self.bicycle


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def make_bicycle(self):
        self.builder.set_brakes()
        self.builder.set_wheels_diameter()
        self.builder.set_wheels()
        self.builder.set_shock_absorbers()
        return self.builder.get_bicycle()


director = Director()
director.set_builder(Cross_Bicycle_Builder())
kid = director.make_bicycle()
print(kid)
