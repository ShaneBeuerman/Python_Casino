#Slot Machine
import random

class wheel:
    def roll(self):
        value = random.randint(0,5)
        self.value = value
        symbols = ["Free", 1, 2, 3, 4, 5]
        print(symbols[value], end="")

class slotmachine:
    def play(self):
        wheel1 = wheel()
        wheel2 = wheel()
        wheel3 = wheel()
        v1 = wheel1.roll()
        v2 = wheel2.roll()
        v3 = wheel3.roll()
        print()
        if v1 == 0 or v2 == 0 or v3 == 0:
            print("Free Spin!")
        if v1 == v2 and v2 == v3:
            print("You win")
        
