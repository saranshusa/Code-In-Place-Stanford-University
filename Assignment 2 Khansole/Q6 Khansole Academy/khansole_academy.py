"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random

MIN = 10
MAX = 99 

def main():
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)

    print('What is ' + str(num1) + ' + ' + str(num2) + '?')
    answer = int(input('Your answer: '))

    if answer == num1 + num2:
        print('Correct!')
    else:
        print('Incorrect. The expected answer is ' + str(num1 + num2))

if __name__ == '__main__':
    main()
