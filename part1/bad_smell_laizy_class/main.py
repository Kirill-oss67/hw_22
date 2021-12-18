# Один из классов не делает совсем ничего,
# просто переадресует вызовы к другому классу.
# Удалите этот класс и перенаправьте вызовы напрямую.

class Unit:
    def __init__(self):
        self.x = 0
        self.y = 0

    def attack(self):
        pass

    def defense(self):
        pass

    def move(self, field_adapter):
        field_adapter.set_unit(x=self.x, y=self.y, unit=self)


class Field:
    def set_unit(self, x, y, unit: Unit):
        pass


class FieldAdapter:
    def __init__(self, field: Field):
        self.field = field

    def set_unit(self, x, y, unit: Unit):
        self.field.set_unit(x, y, unit)


class Main:
    def __init__(self):
        self.field = Field()
        self.field_adapter = FieldAdapter(field=self.field)
        self.unit = Unit()
        self.unit.move(field_adapter=self.field_adapter)
