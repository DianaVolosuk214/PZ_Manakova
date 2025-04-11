# Делала Волощук Диана из Ис-25
# Задание 1
def print_horizontal_line(symbol, length)
  print(symbol * length)
  
def print_word_in_frame(symbol, word):
  length = len(word) + 6
  
  print_horizontal_line(symbol, length)
  print(f" {symbol} {word} {symbol}")
  print_horizontal_line(symbol, length)

word = input(":")
symbol = input(":")
print_word_in_frame(symbol, word)

# Задание 2
def DigitCountSum(K):
  C = 0 # Count Количество
  S = 0 # Sum Сумма
  num = K

  while num > 0:
    digit = num % 10
    C += 1
    S += digit
    num = num // 10
  return C, S
  
numbers = [int(input(f"Введите число {i+1}: ")) for i in range(5)]

for num in numbers:
  count, sum_digits = DigitCountSum(num)
  print(f"Число {num}: количество цифр = {count}, сумма цифр = {sum_digits}") 
