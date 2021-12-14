# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine
# - stop_engine
# - move
# - stop

# Отнаследуйте от него три класса Boat, Car, Electroscooter
# для каждого из требуемых методов через print укажите какое либо действие.
# К примеру start_engine -> print('Двигатель катера запущен')

# Создайте класс Person у которого будет один единственный метод
# use_transport в который в качестве параметра должен передаваться объект реализующий интерфейс Transport
# Медот для этого объекта должен запускать двигатель, двигаться куда-то, тормозить и глушить двигатель.

# Корректным решением будет когда экземпляр класса Person смог использовать все три различных транспорта

# в решении класс Transport должен быть отнаследован от ABC
# все методы Transport должны быть помечены декоратором @abstractmethod
# Классы Boat, Car, Electroscooter должны быть отнаследованы от Transport

# экземлпяр класса Person должен поочередно взаимодействовать с объектами Car, Boat, Electroscooter

# код должен выполняться не выбрасывая исключений

# TODO напишите Ваш код здесь