class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days

    def show(self) -> None:
        print(f'{self.name.capitalize()}:',
              round(self.height, 1), f'cm, {self.age_days} days old')

    def grow(self, day_rate: float = 0.2) -> None:
        self.height += day_rate

    def age(self, days: int = 1) -> None:
        self.age_days += days


if __name__ == '__main__':
    print('== Garden Plant Registry ===')
    rose: Plant = Plant('Rose', 30.0, 20)
    day_rate: float = 0.5
    growth: float = 0
    rose.show()
    for day in range(1, 8):
        print(f'=== Day {day} ===')
        rose.grow(day_rate)
        rose.age()
        rose.show()
        growth += day_rate
    print(f'Growth this week: {growth}cm')
