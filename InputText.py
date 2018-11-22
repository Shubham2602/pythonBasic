import sys
class InputText:

    def __init__(self):  # class constructur (called at creation time)
        self.name = ""   # the default name is the empty string

    def ask(self):
        while 1: # infinite loop
            name = input("Name: ")
            if name == "":
                print("Oops! Retry")
            else:
                print("Hello ", name)
                break  # this will break the loop

        self.name = name  # assign to self.name the value name

obj1 = InputText()
obj1.ask()
