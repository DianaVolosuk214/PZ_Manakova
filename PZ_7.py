# Делала Волощук Диана из Ис-25
# Задание 1
def reverse(N):
  if 1 < N < 26:
    last = [chr(ord('z') - i ) for i in range(N)]
    print(' '.join(last))
  else:
    print("N должна быть в диапазоне 1 < N < 26")

N = int(input("")
reverse(N)
