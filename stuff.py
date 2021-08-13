def getSecretNum(numDigits, base):
    numbers = list(range(base))

def isOnlyDigits(num, base):

# The map() method in the line of code below converts a list of values to a string and returns that string.
base_String_Elements = ''.join(map(str, list(range(base))))
for i in num:
if i not in base_String_Elements:
    return False

print('WELCOME TO BAGELS')
print(' ')
NUMDIGITS = int(input('Enter the number of digits in the secret number:'))
MAXGUESS = int(input('Enter the number of guesses you would like to try:'))
BASE = int(input('Enter a base number system from 5 to 10 to use:'))

secretNum = getSecretNum(NUMDIGITS, BASE)

while len(guess) != NUMDIGITS or not isOnlyDigits(guess,BASE):
