# Делала Волощук Диана из Ис-25
# Задание 1
def reverse(N):
  if 1 < N < 26:
    last = [chr(ord('z') - i ) for i in range(N)]
    print(' '.join(last))
  else:
    print("N должна быть в диапазоне 1 < N < 26")
N = int(input("Введите N:"))
reverse(N)

# Задание 2
def enc_sent(sentence, K):
  if not (0 < K < 10):
    return "К должна быть в диапазоне от 0 до 10 (не включительно)"

  encrypted = []
  for char in sentense:
    if char.isalpha():
      if char.islower():
        base = ord("а")
        end = ord("я")
      else:
        base = ord("А")
        end = ord("Я")
      if char.lower() == "ё":
        encrypted.append(char)
        continue
      shifted = ord(char) + K
      if shifted > end:
        shifted -=32
      encrypted.append(chr(shifted))
    else:
      encrypted.append(char)
  return " ".join(encrypted)
sentence = input(":")
K = int(input(":"))
print(enc_sent(sentence, K))
      
        
        
