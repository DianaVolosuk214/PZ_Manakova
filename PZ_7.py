# Делала Волощук Диана из Ис-25
# Задание 1
def reverse(N):
  if 1 < N < 26:
    last = [chr(ord('z') - i ) for i in range(N)] # ord('z') - i вычисляет код символа, который находится на i позиций раньше в таблице ASCII.
   # for i in range(N) означает, что цикл выполнится N раз, для i от 0 до N-1. chr() преобразует этот код обратно в символ.
    print(' '.join(last)) # выводим элементы списка last, объединённые в строку с пробелами между ними.
  else:
    print("N должна быть в диапазоне 1 < N < 26")
N = int(input("Введите N:"))
reverse(N)

# Задание 2
def enc_sent(sentence, K): # Функция для шифрования предложения
  if not (0 < K < 10):
    return "К должна быть в диапазоне от 0 до 10 (не включительно)" # Проверка на корректность к

  encrypted = [] # Список для хранения зашифрованных символов
  for char in sentense: # Перебираем каждый символ в предложении
    if char.isalpha(): # Проверяем, является ли символ буквой
      if char.islower(): # Проверяем, является ли символ строчной буквой
        base = ord("а")
        end = ord("я")
      else:
        base = ord("А")
        end = ord("Я")
        # Игнорируем букву "ё"
      if char.lower() == "ё":
        encrypted.append(char)
        continue
        
      shifted = ord(char) + K # Сдвигаем символ на К позиций
      if shifted > end:
        shifted -=32 # Количество букв в алфавите без "ё"
      encrypted.append(chr(shifted))
    else:
      encrypted.append(char)
      
  return " ".join(encrypted) # Возвращаем зашифрованное предложение
  
sentence = input()
K = int(input())
print(enc_sent(sentence, K))  
