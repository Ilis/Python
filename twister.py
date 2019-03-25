import random


side = ["правая", "левая"]
part = ["нога", "рука"]
color = ["жёлтый", "красный", "зелёный", "синий"]

players = []

while True:
    player = input("Игрок: ")
    if player == "":
        break
    else:
        players.append(player)

pn = 0
while True:
    command = input("Ход: ")
    if command == "":
        if random.randrange(9) == 0:
            print(players[pn], "—", "cвободный выбор")
        else:
            print(players[pn], "—",
                  random.choice(side),
                  random.choice(part), "на",
                  random.choice(color), "круг"
                  )
        pn += 1
        if pn >= len(players):
            pn = 0
    else:
        break

print("Пока-пока!")
