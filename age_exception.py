while True:
    try:
        s = input("Сколько вам лет?: ")
        age = int(s)
        if age < 0:
            print(f"Ха-ха, {age} — это меньше нуля! Серьёзно:")
        elif age > 199:
            print(f"Да ладно, {age} — это слишком много! Серьёзно:")
        else:
            break
    except ValueError:
        print(f"«{s}» лет? Неееет... Ещё раз:")
print(f"Ваш возраст — {age}!")
