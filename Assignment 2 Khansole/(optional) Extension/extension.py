"""
Python program that reads in a number from the user and 
then displays the Hailstone sequence for that number
"""

def main():
    number = int(input("Enter a number: ")) #user input
    counter = 0

    while(True):
        if number == 1:
            break
        else:                   #iterate until number becomes 1
            temp = number
            counter += 1
            if number % 2 != 0:     #if number is odd
                number = number * 3 + 1
                print(str(temp) + ' is odd, so I make 3n + 1: ' + str(number))
            else:                   #if number is even
                number //= 2
                print(str(temp) + ' is even, so I take half: ' + str(number))

    print('The process took ' + str(counter) + ' steps to reach 1')

if __name__ == "__main__":
    main()
