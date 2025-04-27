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
K = int(input("Введите диапазон K:"))
L = int(input("Введите диапазон L:"))
print(reverse(A, K, L))

# Задание №6 задача №3
def remove_local_maximum(arr): # функция, которая удаляет локальные максимумы из списка arr
  if not arr:
    return arr # если список пустой, то возвращаем пустой список
  n = len(arr)
  result = arr.copy()
  
  for i in range(n): # проверяем каждый элемент списка
    is_local_maximum = True
    if i > 0 and arr[i] <= arr[i-1]: # проверяем, является ли элемент локальным максимумом
      is_local_maximum = False # не трогаем элемент, если он не максимум      
    if i < n - 1 and arr [i] <= arr[i+1]: # проверяем, является ли элемент локальным максимумом
       is_local_maximum = False # не трогаем элемент, если он не максимум
      
    if is_local_maximum: # если элемент локальный максумум, то удаляем его из списка
      result[i] = 0 
  return result # возвращаем список без локальных максимумов
  
N = int(input("размер списка: "))
arr = list(map(int, input("введите элементы списка через пробел: ").split()))
print("исходный список: ", arr)
print("список после удаления локальных максимумов: ", remove_local_maximum(arr))
