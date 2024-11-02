'''Модуль с тестами'''
from math import factorial
from random import randint
from main import find_combinations
from helpers import required_input

# ПРИМЕР
# (1, 2, 3, 4, 5)
# k = 3

# 1, 2, 3 (1, 1, 1, 0, 0) (28) - (1)
# 1, 2, 4 (1, 1, 0, 1, 0) (26)
# 1, 2, 5 (1, 1, 0, 0, 1) (25)
# 1, 3, 4 (1, 0, 1, 1, 0) (22)
# 1, 3, 5 (1, 0, 1, 0, 1) (21)
# 1, 4, 5 (1, 0, 0, 1, 1) (19)
# 2, 3, 4 (0, 1, 1, 1, 0) (14)
# 2, 3, 5 (0, 1, 1, 0, 1) (13)
# 2, 4, 5 (0, 1, 0, 1, 1) (11)
# 3, 4, 5 (0, 0, 1, 1, 1) (7) - Конец цикла при (1) == reversed(1)


def run_tests(tests_amount: int):
    '''Запускает тесты для проверки работоспособности алгоритма

    Args:
        tests_amount (int): Количество тестов
    '''
    tests_completed = 0

    for test_num in range(1, tests_amount + 1):
        test_k = randint(2, 5)
        test_n = randint(test_k, 5)
        test_items = tuple(randint(0, 100) for _ in range(test_n))
        result = tuple(find_combinations(test_items, test_k))
        combinations_amount = (
            factorial(test_n) //
            (factorial(test_k) * factorial(test_n - test_k))
        )

        print('--------------------------------------',
              f'Тест {test_num}',
              f'Числа: {test_items}',
              f'Длина комбинаций: {test_k}',
              'Результат:',
              *result,
              '--------------------------------------', sep='\n\t')

        if len(result) == combinations_amount:
            print(f'Тест {test_num} пройден ✅')
            tests_completed += 1
        else:
            print(f'Тест {test_num} не пройден ❌')

    if tests_completed == tests_amount:
        print('Программа работает верно')
    else:
        print('Не все тесты были пройдены')


if __name__ == '__main__':
    tests_amount = required_input('Введите количество тестов: ', int,
                                  value_range=(1, float('inf')))
    run_tests(tests_amount)
