"""Giraffes class example
"""
class Mammals:
    def eat(self):
        print("Ням-ням...")

class Giraffes(Mammals):
    def __init__(self, s):
        self.name = s
    def greet(self, msg=""):
        newmsg = "Привет, я %s!" % self.name
        if bool(msg):
            newmsg = newmsg + " " + msg
        print(newmsg)
    def eat(self):
        print("%s кушает. Ням-ням..." % self.name)
        
tonny = Giraffes("Тони")
guffy = Giraffes("Гуфи")

tonny.greet()
guffy.greet("Гав-гав!")
guffy.eat()
