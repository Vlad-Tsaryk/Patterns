class FahrenheitThermometer:
    def __init__(self, temperature_F):
        self.temperature = temperature_F

    def get_temperature(self) -> float:
        return self.temperature


class CelsiusThermometer:

    def __init__(self, temperature_C):
        self.temperature = temperature_C

    def get_celsius_temperature(self) -> float:
        return self.temperature


class Adapter(FahrenheitThermometer, CelsiusThermometer):
    def get_temperature(self) -> float:
        return (self.get_celsius_temperature() * 1.8) + 32


def view_temperature(thermometer: FahrenheitThermometer):
    print(thermometer.get_temperature())


if __name__ == '__main__':
    FT = FahrenheitThermometer(520.5)
    view_temperature(FT)
    adapter = Adapter(22)
    view_temperature(adapter)
