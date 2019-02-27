def phone_format(s):
    """Format tel number (using f-str)"""
    
    l = len(s)

    if l < 3:
        return s
    elif l < 5:
        return f"{s[-4:-2]}-{s[-2:]}"
    elif l < 8:
        return f"{s[-7:-4]}-{s[-4:-2]}-{s[-2:]}"
    elif l < 10:
        return f"{s[-9:-7]} {s[-7:-4]}-{s[-4:-2]}-{s[-2:]}"
    elif l == 10:
        if s[0] == '9':
            return f"{s[-10:-7]} {s[-7:-4]}-{s[-4:-2]}-{s[-2:]}"
        else:
            return f"({s[-10:-7]}){s[-7:-4]}-{s[-4:-2]}-{s[-2:]}"
    else:
        return f"{s[:-10]} {s[-10:-7]} {s[-7:-4]}-{s[-4:-2]}-{s[-2:]}"

for s in ["+839987654321",
          "+73437654321",
          "9987654321",
          "3437654321",
          "87654321",
          "7654321",
          "654321",
          "54321",
          "4321",
          "321",
          "21",
          "1",
          ]:
    print(phone_format(s).rjust(20))
