class Warrior:
    def attack(self):
        pass

    def defense(self):
        pass

    def move(self):
        pass

class Healer:
    def defense(self):
        pass

    def move(self):
        pass

    def heal(self):
        pass

class Tree:
    def defense(self):
        pass

    def on_fire(self):
        pass

class Trap:
    def attack(self):
        pass

if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()