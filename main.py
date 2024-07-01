import random

'''
This program recreates the Bagels game and has been modified to being entirely object oriented programming (OOP).
'''

# The Bagel class contains objects for the secret number to be guessed.
class Bagel:
    def __init__(self, value, num_of_digits):
        self.value = value
        self.num_of_digits = num_of_digits

    def getClues(self, guess):
        # Returns a string with the pico, fermi, bagels clues to the user.
        if guess == self.value:
            return 'You got it!'

        clue = []

        for i in range(len(guess)):
            if guess[i] == self.value[i]:
                clue.append('Fermi')
            elif guess[i] in self.value:
                clue.append('Pico')
        if len(clue) == 0:
            return 'Bagels'

        clue.sort()
        return ' '.join(clue)

# The Guess class contains objects for the user's guesses.
class Guess:
    def __init__(self, value):
        self.value = value

    def isOnlyDigits(self):
        # Returns True if num is a string made up only of digits. Otherwise returns False.
        if self.value == '':
            return False

        for i in self.value:
            if i not in '0 1 2 3 4 5 6 7 8 9'.split():
                return False

        return True


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def getSecretNumValue(numDigits):
    # Returns a string that is numDigits long, made up of unique random digits.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum_value = ''
    for i in range(numDigits):
        secretNum_value += str(numbers[i])
    return secretNum_value

NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')

while True:
    secretNum = Bagel(getSecretNumValue(NUMDIGITS), NUMDIGITS)
    print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))

    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = Guess('')
        while len(guess.value) != NUMDIGITS or not guess.isOnlyDigits():
            print('Guess #%s: ' % (numGuesses))
            guess.value = input()

        clue = secretNum.getClues(guess.value)
        print(clue)
        numGuesses += 1

        if guess.value == secretNum.value:
            break
        if numGuesses > MAXGUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum.value))

    if not playAgain():
        break
