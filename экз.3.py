# #2. Напишите функцию, которая проверяет: является ли слово палиндромом
#
# def isPalindrome(a):
#     rev = ''.join(reversed(a))   # Используем  функцию
#     if (a == rev):   # Проверяем строки на равенство
#         return 'Да'
#     return 'Нет'
# a = input('Введите слово: ')
# rezult = isPalindrome(a)
# print(rezult)


# # 1. Напишите функцию, которая будет принимать номер кредитной карты и
# # показывать только последние 4 цифры. Остальные цифры должны заменяться
# # звездочками
# def cardalfa(card):
#     return '*' * len(card[:-4]) + card[-4:]
#
# card = input('vvedite nomer karti: ')
# rezult = cardalfa(card)
# print(rezult)


# 3. Решите задачу
# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

class Tomato:
    states = {0: 'rostok', 1: 'cvetok', 2: 'zelen_pomidor', 3: 'krasn_pomidor'}
    # Динамические свойства
    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переходим к следующей стадии созревания
    def grow(self):
        self._next_state()

    # Проверяем созрел ли помидор
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def _next_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')

# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все помидоры из списка на следующий этап созревания
    def grow_all(self):
        for Tomato in self.tomatoes:
            Tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([Tomato.is_ripe() for Tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []

# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.

class Gardener:

    # Динамические свойства
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Uhazhivaem za ogorodom')
        self._plant.grow_all()
        print('Zakanchivaem rabotu')

    # Собираем урожай
    def harvest(self):
        print('Sobiraem urozhay')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Vse sobrali')
        else:
            print('Podozhdi poka sozreyt')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''Esli hochesh viraschivat pomidori, izuchi instrukcii v google).''')

# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай


Gardener.knowledge_base()
great_tomato_bush = TomatoBush(4)
gardener = Gardener('Alex', great_tomato_bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()