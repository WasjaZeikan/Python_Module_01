class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days

    def show(self, prefix: str = '') -> None:
        if prefix:
            print(prefix, ': ', sep='', end='')
        print(f'{self.name.capitalize()}:',
              round(self.height, 1),
              f'cm, {self.age_days} days old')

    def grow(self, day_rate: float = 0.2) -> None:
        self.height += day_rate

    def age(self, days: int = 1) -> None:
        self.age_days += days


if __name__ == '__main__':
    rose: Plant = Plant('Rose', 30.0, 20)
    cactus: Plant = Plant('Cactus', 8.5, 14)
    sunflower: Plant = Plant('Sunflower', 51.2, 41)
    pine: Plant = Plant('pine', 320.8, 150)
    oak: Plant = Plant('oak', 270.5, 230)
    print('=== Plant Factory Output ===')
    prefix: str = 'Created'
    rose.show(prefix)
    cactus.show(prefix)
    sunflower.show(prefix)
    pine.show(prefix)
    oak.show(prefix)
