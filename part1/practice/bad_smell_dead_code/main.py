# Где-то тут закрался класс который никто не использует. 
# Есть мнение, что он зря тратит чернила монитора. Удалите его

class Unit:
    def __init__(self):
        self.x = 0
        self.y = 0

    def attack(self):
        pass

    def defense(self):
        pass

    def move(self, field):
        field.set_unit(x=self.x, y=self.y, unit=self)

class GameItem():
    def __init__(self, name: str):
        self.name = name

    def step_on(self, unit: Unit):
        pass

class Field:
    def set_unit(self, x, y, unit: Unit):
        pass

class Main:
    def __init__(self):
        self.field = Field()
        self.unit = Unit()
        self.unit.move(field=self.field)

if __name__ == "__main__":
    main = Main()