"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num**2 for num in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    if num == 1 or num == 0:
        return False
    counter = 0
    div_max = num//2
    for div in range(2,div_max+1):
        if num % div == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

def filter_numbers(list_numbers,filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type==ODD:
        filter_list=list(filter((lambda x: x % 2 == 1),list_numbers))
    if filter_type==EVEN:
        filter_list=list(filter((lambda x: x % 2 == 0),list_numbers))
    if filter_type==PRIME:
        filter_list=list(filter(is_prime,list_numbers))
    return filter_list