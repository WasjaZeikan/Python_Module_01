class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age_days: int = age_days

    def show(self, prefix: str = '') -> None:
        if prefix:
            print(prefix, ': ', sep='', end='')
        print(f'{self._name.capitalize()}:',
              round(self._height, 1),
              f'cm, {self._age_days} days old')

    def grow(self, day_rate: float = 0.2) -> None:
        self._height += day_rate

    def age(self, days: int = 1) -> None:
        self._age_days += days

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def _validate_height(self, height: float) -> bool:
        if height >= 0:
            return True
        print(f'{self._name.capitalize()}: Error, height can\'t be negative')
        print('Height update rejected')
        return False

    def _validate_age(self, age: int) -> bool:
        if age >= 0:
            return True
        print(f'{self._name.capitalize()}: Error, age can\'t be negative')
        print('Age update rejected')
        return False

    def set_height(self, height: float = 25.5) -> None:
        if self._validate_height(height):
            self._height = height
            print(f'Height updated: {round(self._height, 1)}cm')

    def set_age(self, age: int = 20) -> None:
        if self._validate_age(age):
            self._age_days = age
            print(f'Age updated: {self._age_days} days')


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int, color: str):
        super().__init__(name, height, age_days)
        self.color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self, prefix: str = '') -> None:
        super().show(prefix)
        print(f' Color: {self.color}')
        if self._bloomed:
            print(f' {self._name.capitalize()} is blooming beautifully!')
        else:
            print(f' {self._name.capitalize()} has not bloomed yet')


class Tree(Plant):
    def __init__(self, name: str,
                 height: float,
                 age_days: int,
                 trunk_diameter: float):
        super().__init__(name, height, age_days)
        self.trunk_diameter: float = trunk_diameter

    def show(self, prefix: str = '') -> None:
        super().show(prefix)
        print(f' Trunk diameter: {round(self.trunk_diameter, 1)}cm')

    def produce_shade(self) -> None:
        print(f'Tree {self._name.capitalize()} now produces a shade of',
              f'{round(self._height, 1)}cm long and',
              f'{round(self.trunk_diameter, 1)}cm wide',
              end='')


class Vegetable(Plant):
    def __init__(self, name: str,
                 height: float,
                 age_days: int,
                 harvest_season: str):
        super().__init__(name, height, age_days)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def show(self, prefix: str = '') -> None:
        super().show(prefix)
        print(f' Harvest season: {self.harvest_season.capitalize()}')
        print(f' Nutritional value: {self.nutritional_value}')

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += days

    def grow(self, day_rate: float = 0.2) -> None:
        super().grow(day_rate)
        self.nutritional_value += 1


if __name__ == '__main__':
    print('=== Garden Plant Types ===')
    print('=== Flower')
    rose: Flower = Flower('rose', 25.5, 20, 'pink')
    rose.show()
    print('[asking the rose to bloom]')
    rose.bloom()
    rose.show()
    print('=== Tree')
    oak: Tree = Tree('Oak', 300.5, 60, 7.3)
    oak.show()
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    print('=== Vegetable')
    tomato: Vegetable = Vegetable('tomato', 5.2, 10, 'April')
    tomato.show()
    print('[make tomato grow and age for 20 days]')
    for _ in range(20):
        tomato.grow(2.3)
        tomato.age()
    tomato.show()
