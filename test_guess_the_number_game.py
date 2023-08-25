
import unittest
from unittest.mock import patch
from guess_the_number_game import GuessTheNumberGame

class TestGuessTheNumberGame(unittest.TestCase):

    def test_correct_guess(self):
        #Here we test whether the guessed number is correct or incorrect
        # Mocking the random number generator to ensure a known number (1234) for testing
        with patch('random.randint', return_value=1234):
            #Create the instance of the game
            game = GuessTheNumberGame()
            #Here we check whether the guess is identified correctly
            self.assertEqual(game.play("1234"), 1)
    
    def test_incorrect_guess(self):
        #Testing whether the guessed number is incorrect
        # Mocking the random number genartor to ensure a known number(5678) for testing
        with patch('random.randint', return_value=5678):
            game = GuessTheNumberGame()
            #Here we check whether the incorrect guess is processed as expected
            self.assertEqual(game.play("1234"), 1)
    
    def test_invalid_guess(self):
        #Testing whether the user input is invalid, whether it contains any special characters or symbols
        # Mocking the random number to ensure a known number (9876) for testing
        with patch('random.randint', return_value=9876):
            game = GuessTheNumberGame()
            # Here we check whether the invalid guess is handled as expected or not
            self.assertEqual(game.play("12a4"), 1)
    
if __name__ == '__main__':
    unittest.main()
