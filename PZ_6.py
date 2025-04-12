# Делала Волощук Диана из Ис-25
# Задание №6 задача №1
def gen_fib_num():
  N = 10 

  fib = [1, 1]
  for i in range(2, N):
    fib.append(fib[i-2] + fib[i-1])
  return fib

print (gen_fib_num())

# Задание №6 задача №2
def reverse(A, K, L):
  if 1 < K < L < len(A):
    A[K-1:L] = A[K-1:L][::-1]
  return A
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K = int(input("Введите диапазон K:")
L = int(input("Введите диапазон L:")
print(reverse(A, K, L)
