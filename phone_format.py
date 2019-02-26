def phone_format(phone):
    """Format tel number (fixed representation)
    
    Formats only 10-digit number preceeding '+' and 1-digit number
    """
    return "%s%s %s%s%s %s%s%s-%s%s-%s%s" % tuple(list(phone))

phone="+79998887766"
print(phone_format(phone))
