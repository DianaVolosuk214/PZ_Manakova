# Практическая работа №4. Делала Волощук Диана ИС-25.
# Задание 1
Дано вещественное число - цена за 1 кг конфет. Вывести стоимость 1.2, 1.4 ... 2 кг конфет.
# Алгоритм
float(input) - цена за кг конфет
->
current_weight - вес кг
->
Назначение цикла while --  конечная цена = цена * вес -
Ввыводим цену за кг конфент (print total_coast)
->
Прибавляем вес - current_weight +0.2
->
Вводим цену за 1 кг конфет price
->
Записываем текущий вес current_weight
->
Считаем стоимость конфет total_cost
->
Выводим стоимость веса за кг конфет print 
# Объяснение кода
float(input()) - берем цену вещественным числом
-> Назначаем текущий вкс (1.2 кг). Пока текущий вес не достиг 2, прибавляем по 0.2 кг и умножаем на цену.
# Задание 2
Дано число N больше нуля. Найти количнство и сумму его цифр.
# Алгоритм
Вводим n
->
Если n меньше, либо равно нулю, то выводим ошибку
->
Если n больше нуля, то вводим переменные sum_digits, count_digits, temp
->
Пока  temp  больше 0, то:
->
Выводим количество цифр
->
Выводим сумму цифр
# Обяснение кода
int(input()) - берет значение из консоли и преобразует его в целое число. Условие на значение введенного числа: пока наше число больше 0 выполняем алгоритм по получению последней цифры и убиранию ее же. Выводим сумму и количество чисел, введенных пользователем.


