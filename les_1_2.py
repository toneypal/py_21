# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_seconds = int(input("Введите секунды "))

seconds = user_seconds % 60

minutes = user_seconds  // 60

hours = minutes // 60

if user_seconds  // 60 >  60:
    hours_minutes = user_seconds  // 60 % 60
    minutes = hours_minutes

print(f'Время в формате чч:мм:сс - это {hours:d}:{minutes:02d}:{seconds:02d}') #
