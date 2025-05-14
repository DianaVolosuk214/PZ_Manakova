fruits = {
  "цвет":"красный",
  "форма":"круглая",
  "вкус":"кислый"
}
print(f"первоначальный словарь: {fruits}")

found = False

for key, value in fruits.items():
  if key == "фрукт" and value == "яблоко":
    found = True
    break

if not found:
  fruits["фрукт"] = "яблоко"
  print(f":{fruits}")
