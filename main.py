class Dog:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.days_passed = 0

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        print(self.name + " is eating. Hunger decreased!")

    def play(self):
        if self.energy > 10:
            self.happiness = min(100, self.happiness + 20)
            self.energy -= 10
            print(self.name + " is playing! Happiness increased!")
        else:
            print(self.name + " is too tired to play.")

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        print(self.name + " is sleeping. Energy restored!")

    def status(self):
        print("\nDay " + str(self.days_passed))
        print(self.name + " (Dog) - Hunger: " + str(self.hunger) + ", Happiness: " + str(self.happiness) + ", Energy: " + str(self.energy))

    def next_day(self):
        self.days_passed += 1
        self.hunger = min(100, self.hunger + 10)
        self.happiness = max(0, self.happiness - 5)
        self.energy = max(0, self.energy - 5)
        print("\nA new day begins...\n")


def main():
    name = input("Enter your dog's name: ").strip()
    dog = Dog(name)

    while True:
        dog.status()
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            dog.feed()
        elif choice == "2":
            dog.play()
        elif choice == "3":
            dog.sleep()
        else:
            print("Invalid choice. Try again.")

        dog.next_day()
        
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont != "yes":
            print("Goodbye! " + dog.name + " lived for " + str(dog.days_passed) + " days.")
            break

if __name__ == "__main__":
    main()
set