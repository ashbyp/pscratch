class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        return self.temperature * 1.8 + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


def main():
    c = Celsius(100)
    print(c.temperature)
    print(c.fahrenheit)
    c.temperature = 300
    print(c.fahrenheit)

    c.temperature = -273
    while c.temperature != c.fahrenheit:
        c.temperature = c.temperature + 1
    print(c.temperature)


if __name__ == '__main__':
    main()


