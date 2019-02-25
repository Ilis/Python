def prime_numbers(val):
    return [
        x for x in range(2, val+1) if all((x%y for y in range(2, 1+int(x**0.5)))            )
        ]
for n in prime_numbers(42):
    print("%d" % n, end=" ")
print("")