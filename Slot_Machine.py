#Slot Machine
import random

class wheel:
    def roll(self):
        value = random.randint(0,5)
        self.value = value
        symbols = [0, 1, 2, 3, 4, 5]
        print(symbols[value], end=" ")
        return value

class slotmachine:
    def play(self, wager):
        print(type(wager))
        wheel1 = wheel()
        wheel2 = wheel()
        wheel3 = wheel()
        v1 = wheel1.roll()
        v2 = wheel2.roll()
        v3 = wheel3.roll()
        print()
        if v1 == 0 or v2 == 0 or v3 == 0:
            print("You get your money back.")
            return wager
        if v1 == v2 and v2 == v3:
            print("You win")
            if v1 == 1:
                print("3x")
                return wager * 3
            if v1 == 2:
                print("4x")
                return wager * 4
            if v1 == 3:
                print("5x")
                return wager * 5
            if v1 == 4:
                print("6x")
                return wager * 6
            if v1 == 5:
                print("7x")
                return wager * 7
        if (v1 == v2 and v1 != v3) or (v1 == v3 and v1 != v2) or (v2 == v3 and v2 != v1):
            print("You win")
            print("2x")
            return wager * 2
        print("You lose")
        return 0
