def phone_format(phone):
    """Format tel number (fixed representation)"""
    
    l = len(phone)

    if l < 3:
        return phone
    elif l < 5:
        return "%s-%s" % (phone[-4:-2], phone[-2:])
    elif l < 8:
        return "%s-%s-%s" % (phone[-7:-4], phone[-4:-2], phone[-2:])
    elif l < 10:
        return "%s %s-%s-%s" % (phone[-9:-7], phone[-7:-4], phone[-4:-2], phone[-2:])
    elif l == 10:
        if phone[0] == '9':
            return "%s %s-%s-%s" % (phone[-10:-7], phone[-7:-4], phone[-4:-2], phone[-2:])
        else:
            return "(%s)%s-%s-%s" % (phone[-10:-7], phone[-7:-4], phone[-4:-2], phone[-2:])
    else:
        return "%s %s %s-%s-%s" % (phone[:-10], phone[-10:-7], phone[-7:-4], phone[-4:-2], phone[-2:])

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
