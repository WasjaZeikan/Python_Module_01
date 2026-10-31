class Plant:
    class Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def show(self) -> None:
            print(f'Stats: {self.grow_count} grow,',
                  f'{self.age_count} age,',
                  f'{self.show_count} show')

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age_days: int = age_days
        self._stats = self.Stats()

    def show(self, prefix: str = '') -> None:
        self._stats.show_count += 1
        if prefix:
            print(prefix, ': ', sep='', end='')
        print(f'{self._name.capitalize()}:',
              round(self._height, 1),
              f'cm, {self._age_days} days old')

    def grow(self, day_rate: float = 0.2) -> None:
        self._height += day_rate
        self._stats.grow_count += 1

    def age(self, days: int = 1) -> None:
        self._age_days += days
        self._stats.age_count += 1

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

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls, name: str = 'Unknown plant',
                  height: float = 0.0,
                  age: int = 0):
        return cls(name, height, age)


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
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.shade_count = 0

        def show(self) -> None:
            super().show()
            print(f' {self.shade_count} shade')

    def __init__(self, name: str,
                 height: float,
                 age_days: int,
                 trunk_diameter: float):
        super().__init__(name, height, age_days)
        self._stats: Tree.TreeStats = self.TreeStats()
        self.trunk_diameter: float = trunk_diameter

    def show(self, prefix: str = '') -> None:
        super().show(prefix)
        print(f' Trunk diameter: {round(self.trunk_diameter, 1)}cm')

    def produce_shade(self) -> None:
        self._stats.shade_count += 1
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


class Seed(Flower):
    def __init__(self, name: str, height: float, age_days: int, color: str):
        super().__init__(name, height, age_days, color)

    def show(self, prefix: str = '') -> None:
        super().show(prefix)
        seeds = self._age_days // 2 if self._bloomed else 0
        print('Seeds:', seeds)


def display_stats(plant: Plant):
    print(f'[statistics for {plant._name}]')
    plant._stats.show()


if __name__ == '__main__':
    def test_flower(flower: Flower, name: str) -> None:
        flower.show()
        display_stats(flower)
        print(f'[asking the {name} to bloom]')
        flower.bloom()
        flower.show()
        display_stats(flower)

    def test_tree(tree: Tree, name: str) -> None:
        tree.show()
        display_stats(tree)
        print(f'[asking the {name} to produce shade]')
        tree.produce_shade()
        display_stats(tree)

    def test_vegetable(vegetable: Vegetable, name: str, days: int) -> None:
        vegetable.show()
        display_stats(vegetable)
        print(f'[make {name} grow and age for {days} days]')
        for _ in range(days):
            vegetable.grow(2.3)
            vegetable.age()
        vegetable.show()
        display_stats(vegetable)

    def test_seed(seed: Seed, name: str) -> None:
        seed.show()
        print(f'[make {name} grow, age and bloom]')
        seed.grow(15.2)
        seed.age(55)
        seed.bloom()
        seed.show()
        display_stats(seed)

    def test_days(days: int) -> None:
        print(f'Is {days} days more than a year ->',
              Plant.is_older_than_year(days))

    print('=== Garden statistics ===')
    print('=== Check year-old')
    test_days(50)
    test_days(400)
    rose: Flower = Flower('rose', 25.5, 20, 'pink')
    test_flower(rose, 'rose')
    print('\n=== Tree')
    oak: Tree = Tree('Oak', 300.5, 60, 7.3)
    test_tree(oak, 'oak')
    print('\n=== Vegetable')
    tomato: Vegetable = Vegetable('tomato', 5.2, 10, 'April')
    test_vegetable(tomato, 'tomato', 20)
    print('\n=== Seed')
    sunflower: Seed = Seed('Sunflower', 80.5, 30, "yellow")
    test_seed(sunflower, 'sunflower')
    print('\n=== Anonymous')
    anon: Plant = Plant.anonymous()
    anon.show()
    display_stats(anon)
