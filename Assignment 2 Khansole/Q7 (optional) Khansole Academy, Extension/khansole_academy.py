"""
Generates addition problems until the user correctly answers 3 in a row.
"""

import random

CORRECT_REQUIRED = 3
MIN = 10
MAX = 99

def main():
    CORRECT_NOW = 0
    while(CORRECT_NOW < CORRECT_REQUIRED):
        num1 = random.randint(MIN, MAX)
        num2 = random.randint(MIN, MAX)
        
        print('What is ' + str(num1) + ' + ' + str(num2) + '?')
        answer = int(input('Your answer: '))

        if answer == num1 + num2:
            CORRECT_NOW += 1
            print("Correct! You've gotten " + str(CORRECT_NOW) + " correct in a row.")
        else:
            print('Incorrect. The expected answer is ' + str(num1 + num2))
            CORRECT_NOW = 0
    
    print('Congratulations! You mastered addition.')


if __name__ == '__main__':
    main()
