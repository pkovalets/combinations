'''Программа для поиска сочетаний'''
from typing import Iterator
from helpers import wait_for_input, required_input, required_iterable


def find_combinations(items: tuple[int] | list[int], k: int) -> \
                                        Iterator[tuple[int]]:
    '''Ищет все сочетания для последовательности целых чисел
    длиной k без повторений

    Args:
        items (tuple[int] | list[int]): Всевозможные числа для сочетаний
        k (int): Длина одного сочетания

    Yields:
        Iterator[tuple[int]]: Сочетания, если они существуют
    '''
    def get_combination():
        return tuple(items[i] for i in range(n) if items_bool[i])

    if not k or not items or len(items) < k or k < 2:
        return

    n = len(items)
    items_bool = tuple(1 if i < k else 0 for i in range(n))
    last_iteration = tuple(reversed(items_bool))
    yield get_combination()

    while items_bool != last_iteration:
        items_bool_bin = ''.join(map(str, items_bool))
        items_bool_dec = int(items_bool_bin, 2)

        while items_bool_dec > 0:
            items_bool_dec -= 1
            items_bool_bin = bin(items_bool_dec)[2:].zfill(n)

            if items_bool_bin.count('1') == k:
                items_bool = tuple(map(int, items_bool_bin))
                yield get_combination()
                break


def print_combinations(items: tuple[int], k: int):
    '''Выводит комбинации на экран, если они существуют.
    В противном случае - ошибку

    Args:
        items (tuple[int]): Последовательность элементов
        k (int): Длина комбинации
    '''
    result = find_combinations(items, k)

    if not items:
        print('Необходимо ввести элементы!')
    elif not k:
        print('Необходимо ввести длину комбинаций!')
    elif k < 2:
        print('Длина комбинаций не может быть меньше чем 2!')
    elif len(items) >= k:
        print('Найдены комбинации:')
        for item in result:
            print(item)
    else:
        print('Длина комбинаций больше чем количество чисел!')

    wait_for_input()


def start(items: tuple[int], k: int) -> tuple[bool, tuple[int], int]:
    '''Запускает алгоритм поиска сочетаний для пользователя
    с проверками ввода, также синхронизирует данные с окружением выше

    Args:
        items (tuple[int]): Последовательность элементов
        k (int): Длина комбинации

    Returns:
        tuple[bool, tuple[int], int]: Выход из программы, последовательность
        элементов, длина комбинации
    '''
    print('----------------',
          '***** МЕНЮ *****',
          '-----------------',
          'Выберите действие:',
          '1) Ввести последовательность для поиска комбинаций',
          '2) Ввести длину комбинаций',
          '3) Вывести получившиеся комбинации',
          '4) Выход', sep='\n')

    user_choice = required_input('Выберите действие: ',
                                 int, value_range=(1, 4))

    if user_choice == 4:
        return False, items, k

    if user_choice == 1:
        items = required_iterable('Введите числа через пробел: ',
                                  tuple, int, 2)
    elif user_choice == 2:
        k = required_input('Введите длину комбинаций: ', int)
    elif user_choice == 3:
        print_combinations(items, k)
    return True, items, k


def main():
    '''Основная функция программы, которая зацикливает её выполнение
    и хранит данные
    '''
    should_run = True
    items = None
    k = None

    while should_run:
        should_run, items, k = start(items, k)


if __name__ == '__main__':
    main()
