# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted(self):
        self.lst.sort()
        return self.lst

    def sorting(self):
        return sorted(self.lst)

    def asc_sorting(self):
        return sorted(self.lst, reverse=False)
