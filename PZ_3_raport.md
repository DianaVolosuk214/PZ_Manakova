# Практическая работа №3. Делала Волощук Диана ИС-25.
# Задание 1
Даны два целых числа А и В. Проверить истинность высказывания: "Справедливы ли неравенства А > 0 и В < - 2" 
# Алгоритм
Вводим число А
->
Вводим число В
->
Проверяем истинность неравенств (result)
->
Выводим результат (print)
# Объяснение кода
int(input()) - берет значение из консоли и преобразует его в целое число 
result = (a > 0) or (b < -2) - проверяет, верно ли какое либо выражение 
print(result) - выводит истинно ли какое либо выражение

#  Задание 2
Дано трехзначное число, в котором первая цифра указывает на масть, а вторые две на достоинство карты. Вывести соответсвующее название карты вида "дама червей".
# Алгоритм
Вводим а (трехзначное число)
->
Первое число из трехзначного - suit_num
->
Остальные числа из трехзначного - rank_num
->
Задаем словарь - suits
->
Задаем словарь - ranks
->
Получаем значение по ключу - suit_name
->
Выводим результат - print

# Обяснение кода
int(input()) - берет значение из консоли и преобразует его в целое число 
suit_num - узнаем первое число
rank_num - узнаем оставшееся число
Задаем словарь значений для первого числа (suits)
Задаем словарь значений для остальных чисел (ranks)
Получение масти из списка для опредения (suit_name)
Задаем условие, что два последующих числа нахлдятся в диапазоне от 2 до 10. Если условие соблюдаются, то пишется это число, иначе берется название из списка ranks
Выводим нашу игральную карту (print)
