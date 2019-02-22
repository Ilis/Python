# Hello
import sys
""" Hello world py

First doc in hello program

"""

def sq(a):
    """Square a

    Returns a squared

    """

    return a*a

print("Hello, %s!" % "Ilis")
print("Sq 5 = %d" % sq(5))
for i in range(5):
    print("i= %.2f" % i, end='; ')
    if i == 2: print("i==%s!" % i, end='; ', file=sys.stderr)  # Error!
print("\n--")

