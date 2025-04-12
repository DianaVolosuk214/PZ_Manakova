# Делала Волощук Диана из Ис-25
# Задание №6 задача №1
def gen_fib_num():
  N = 10 

  fib = [1, 1]
  for i in range(2, N):
    fib.append(fib[i-2] + fib[i-1])
  return fib

print (gen_fib_num())
