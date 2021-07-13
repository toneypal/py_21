# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
#


def my_func(*args):
    min_1 = min(args)
    list_1 = []
    for el in args:
        if el > min_1:
            list_1.append(el)
        else:
            continue
    return sum(list_1)


print(my_func(1,2,3))