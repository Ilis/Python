import random


items = []

while True:
    s = input(": ")
    if s == "":
        break
    items.append(s)

print("И ваш выбор:")
print(random.choice(items))
