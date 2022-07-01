# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def calc_cube_volume(self):
        return self.x * self.y * self.z


cube = Cube(1,7,22)
print(cube.calc_cube_volume())

