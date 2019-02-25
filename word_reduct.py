word = (input("Напишите слово: ")).upper()
for n in range(len(word)):
    print(' '*n, word[n:], sep="")
