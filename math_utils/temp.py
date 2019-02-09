class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        #print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        #print("Setting value")
        self._temperature = value


if __name__ == '__main__':
    c = Celsius(100)
    print(c.temperature)
    print(c.to_fahrenheit())
    c.temperature = 300
    print(c.to_fahrenheit())

    c.temperature = -273
    while c.temperature != c.to_fahrenheit():
        c.temperature = c.temperature + 1
    print(c.temperature)


