class Car:
    def __init__(self, model, year):
        self._model = model
        self._year = year

    def drive(self, model, year):
        print(f"{self._model}, {self._year} is driving")

audi = Car("Audi R8", 2016)

audi.drive()