import random

class GuessTheNumberGame:

    def __init__(self):
        #Initialize the game with a randomly generated 4-digit number.
        self.number = str(random.randint(1000, 9999))
        self.attempts = 0

    def check_guess(self, guess):
        #Comapres the guessed number with the randomly generated number
        #Check if there is a match or not. If the match is not found we provide the hints to make correct guess.
        clues = []
        for i in range(4):
            if guess[i] == self.number[i]:
                #The hint is correct digit is in the correct position
                clues.append("circle")
                #The correct digit is in the wrong position
            elif guess[i] in self.number:
                clues.append("x")
            else:
                # The digit is not present the randomly generated number
                clues.append("-")
        return " ".join(clues)

    def play(self, guess):
        #Method to play the game and display the hints based on the gusses made
        self.attempts += 1
        result = self.check_guess(guess)
        if result == "circle circle circle circle":
            print(f"Congratulations! Your guess is correct and you guessed the number in {self.attempts} attempts.")
            return self.attempts
        else:
            print("Hints:", result)
            return self.attempts

    def get_number(self):
        #Here we retrieve the actual number and it is used when the player quits the game
        return self.number

if __name__ == "__main__":
    game = GuessTheNumberGame()
    print("Welcome to Guess the Number game")
    while True:
        guess = input("Enter your guess (or enter 'quit' to exit): ")
        if guess.lower() == "quit":
            print(f"The correct number was: {game.get_number()}")
            break
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        attempts = game.play(guess)
