# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from functools import reduce

def fact_gen(num):
    for i in range(1, num + 1):
        yield i

def mult_func(start_val, end_val):
    return start_val*end_val

def fuct(n):
    el = 1
    fg = fact_gen(n)
    for i in fg:

        # yield i
        return reduce(mult_func, fg)

# for i in fuct(5):
#     print(i)

print(fuct(5))


# Не смогла сделать так чтобы функция вызывалась через for и одновременно возвращала факториал









