# Задание 1

def create(sequence):
  new_sequence = []
  for i in range(len(sequence) - 1):
    new_element = (sequence[i] + sequence[i + 1]) ** 2
    new_sequence.append(new_element)
  return new_sequence 

input_sequence = [int(input("Введите 5 разных чисел: ")) for x in range(5)]
result = create(input_sequence)
print(f"Новая последовательность:" {result}")

# Задание 2
def uppercase_generator(input_string):
  for char in input_string:
    yield char.upper()

input_string = input(":")
generator = uppercase_generator(input_string)

print(list(generator))
