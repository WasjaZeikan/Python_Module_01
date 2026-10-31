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


if __name__ == '__main__':
    rose: Plant = Plant('Rose', 25.5, 20)
    print('=== Garden Security System ===')
    rose.show('Plant created')
    print()
    rose.set_height(31.2)
    rose.set_age(50)
    print()
    rose.set_height(-12.2)
    rose.set_age(-20)
    print()
    rose.show('Current state')
