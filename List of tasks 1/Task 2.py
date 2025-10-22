import random

class Dice:
    def __init__(self, sides):
        self._sides = sides
        self._value = None

    def roll(self):
        self._value = random.randint(1, self._sides+1)

    def get_sides(self):
        return self._sides

    def get_value(self):
        return self._value

    def __str__(self):
        return f"From 1 to {self.get_sides()} the value is {self.get_value()}"


dices = [Dice(6), Dice(6)]
while True:
    print("What do you want?:")
    print("0 - Exit")
    print("1 - Start the game")
    controller = int(input(": "))
    user_points, computer_points = 0, 0

    if controller == 0:
        break
    elif controller == 1:
        while True:
            for dice in dices:
                dice.roll()
                computer_points += dice.get_value()
            print("What do you want?:")
            print("1 - Roll the dices")
            print("2 - Get results")
            controller = int(input(": "))

            if controller == 1:
                for dice in dices:
                    dice.roll()
                    user_points += dice.get_value()
                print(f"Your points: {user_points}")
                if user_points >= 21:
                    controller = 2
                else:
                    continue
            if controller == 2:
                if user_points == computer_points or (user_points >= 21 and computer_points >= 21):
                    print("It's draw")
                elif (user_points >= 21 or computer_points > user_points) and computer_points < 21:
                    print("Computer won")
                elif (user_points > computer_points or computer_points >= 21) and user_points < 21:
                    print("You won")
                print(f"Your points: {user_points}")
                print(f"Computer points: {computer_points}")
                break
