# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#
# Подсказка: использовать функцию reduce().


from functools import reduce

def mult_func(start_val, end_val):
    return start_val*end_val


gen = (param * param for param in range(100,1001,2))
print(reduce(mult_func, gen))
