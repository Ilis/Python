import random

word = (input("Напишите слово: ")).upper()
letters = list(word)
random.shuffle(letters)
newword = "".join(letters)
print(word)
print(newword)