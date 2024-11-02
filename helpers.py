'''Модуль со вспомогательными функциями'''
from typing import Type, Any


def wait_for_input():
    '''Создаёт задержку, чтобы пользователь успел прочитать текст выше
    '''
    input('Нажмите Enter чтобы продолжить...')


def required_input(input_text: str, var_type: Type = str, **kwargs) -> Any:
    '''Обязательный для ввода input с расширенными опциями

    Args:
        input_text (str): Текст, который видит пользователь
        var_type (Type, optional): Тип, который будет иметь значение функции.
        По умолчанию str.

    Returns:
        Any: значение, введенное пользователем
    '''
    result = None
    value_range = kwargs.get('value_range')
    should_run = True

    while should_run:
        try:
            result = var_type(input(input_text))

            if var_type == str and result.strip() == '':
                should_run = True
            elif var_type in (int, float) and value_range:
                start = value_range[0]
                end = value_range[1]
                should_run = not start <= result <= end
            else:
                should_run = False
        except ValueError:
            print(f'Элемент должен соответствовать типу {var_type.__name__}!')

    return result


def required_iterable(input_text: str, iterable_type: Type,
                      items_type: Type = str, min_length: int = 1
                      ) -> tuple[Any] | list[Any]:
    '''Обязательный ввод для пользователя с клавиатуры
    некоторой последовательности

    Args:
        input_text (str): Текст, который видит пользователь
        iterable_type (Type): Тип последовательности
        items_type (Type, optional): Тип элементов. По умолчанию str.
        min_length (int, optional): Минимальная длина последовательности.
        По умолчанию 1.

    Returns:
        tuple[Any] | list[Any]: Последовательность, вводимая пользователем
        с клавиатуры
    '''
    result = None
    should_run = True

    while should_run:
        try:
            result = iterable_type(map(items_type, input(input_text).split()))
            if len(result) >= min_length:
                should_run = False
        except ValueError:
            print(f'Элементы должны быть {items_type.__name__}!')

    return result
