"""age program

Program for defining ages
"""
gulls = int(input("Сколько чаек?: "))

def fmtnum(num, str1, strS, strM):
    """format number with trailing word

    Format number and trailing words according to number
    """
    if 11 <= num%100 <= 14:
        return "{} {}".format(num, strM)

    if num%10 == 1:
        return "{} {}".format(num, str1)
    elif 2 <= num%10 <= 4:
        return "{} {}".format(num, strS)
    else:
        return "{} {}".format(num, strM)


age = int(input("Ваш возраст?: "))

print("На острове %s." % fmtnum(gulls, "чайка", "чайки", "чаек"))

print("— Вам %s, " % fmtnum(age, "год", "года", "лет"), end="")

if age <= 2:
    print("пора в ясли!")
elif 3 <= age <= 6:
    print("пора в садик!")
elif 7 <= age <= 16:
    print("пора в школу!")
else:
    print("даже не знаю...")
