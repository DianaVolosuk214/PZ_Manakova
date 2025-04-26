# Делала Волощук Диана из ис-25
# Задание 1
price = float(input("Введите цену за 1 кг конфет:"))
current_weight = 1.2 # Текущий вес

while current_weight <= 2.0: # Условие выполнения
  total_cost = price * current_weight # Стоимость конфет
  print(f"Стоимость {current_weight} кг конфет: {total_cost:.2f}")"
  current_weight += 0.2 # Прибавление веса

# Задание 2

n = int(input("Введите число больше 0:")) # Переменная целого числа
if n <= 0: # Условие, если введенное число меньше или равно 0
  print("Вы ввели неправильное число")
  
else: # Если введенное число больше 0
  sum_digits = 0 # Сумма цифр
  count_digits = 0 # Количество цифр
  temp = n # Временная переменная
  
  while temp > 0: # Цикл, пока переменная больше 0
    digit = temp % 10 # Получаем последнюю цифру
    sum_digits += digit # Сумма цифр
    count_digits += 1 # Количество цифр
    temp = temp // 10 # Убираем последнюю цифру
  print(f"Количество цифр: {count_digits}")
  print(f"Сумма цифр: {count_digits}")
