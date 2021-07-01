# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = input("ВВедите целое положительное число - ")

max = user_number[0]
i = 0

while i < len(user_number):
    if user_number[i] > max:
        max = user_number[i]
    else: i += 1

print(max)


