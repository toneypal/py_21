# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = input("Введите  число: ")

op1 = int(user_number)
op2 = int(user_number + user_number)
op3 = int(user_number + user_number + user_number)

result = op1 + op2 +op3

print(result)