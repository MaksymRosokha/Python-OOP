class Pet:
    def __init__(self, name, hunger = 0, tiredness = 0):
        if len(name) < 3 or not name.isalpha():
            raise ValueError("Your entered name is incorrect")
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness
        self.talk()

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    def mood(self):
        if self.tiredness < 5 and self.hunger < 5:
            return "happy"
        elif self.tiredness <= 10 and self.hunger <= 10:
            return "pleasured"
        elif self.tiredness <= 15 and self.hunger <= 15:
            return "nervous"
        else:
            return "mad"

    def talk(self):
        self._passage_of_time()
        print(f"{self.name} is {self.mood()}")


    def eat(self, food = 4):
        self._passage_of_time()
        self.hunger = max(0, self.hunger - food)

    def play(self, fun = 4):
        self._passage_of_time()
        self.tiredness = max(0, self.tiredness - fun)

    def __str__(self):
        return f"Your pet {self.name} has:\nHunger: {self.hunger}\nTiredness: {self.tiredness}\nMood: {self.mood()}"

def main():
    name = input("Enter the name of your pet: ")
    pet = Pet(name)

    while True:
        print("\nWhat do you want to do?")
        print("1. Talk to pet")
        print("2. Feed pet")
        print("3. Play with pet")
        print("4. Exit")
        print('Type "xy" to see full stats')

        choice = input("> ")

        if choice == "1":
            pet.talk()
        elif choice == "2":
            food = int(input("How much food to give? "))
            pet.eat(food)
        elif choice == "3":
            fun = int(input("How long to play? "))
            pet.play(fun)
        elif choice.lower() == "xy":
            print(pet)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()