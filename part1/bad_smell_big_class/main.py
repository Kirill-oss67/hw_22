# в задании представлен один класс который нужно разбить на 4
# Воин      - Unit
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
# Лекарь может защищаться, лечить воина и панически спасаться бегством
# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
# Ловушка не может ничего кроме как атаковать того, кто на нее наступит

class Unit:
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
