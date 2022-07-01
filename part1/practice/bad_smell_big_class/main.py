class Warrior:

    def attack(self):
        pass

    def defense(self):
        pass

    def move(self):
        pass


class Healer:
    def healer_defense(self):
        pass

    def healer_move(self):
        pass

    def heal(self):
        pass


class Tree:
    def tree_defense(self):
        pass

    def on_fire(self):
        pass


class Trap:
    def trap_attack(self):
        print("It's a trap!")


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()
