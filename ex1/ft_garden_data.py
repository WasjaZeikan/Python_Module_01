class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(f'{self.name.capitalize()}:',
              self.height, 'cm, {self.age} days old')


if __name__ == '__main__':
    print('== Garden Plant Registry ===')
    rose = Plant('Rose', 30, 20)
    sunflower = Plant('Sunflower', 110, 50)
    cactus = Plant('Cactus', 20, 150)
    rose.show()
    sunflower.show()
    cactus.show()
