"""
Ancient Strategy Game of Nimm or Tiouk Tiouk or Tsynshidzi
"""

def main():
    TOTAL_STONES = 20
    Remove = 0

    while(True):
        print('There are ' + str(TOTAL_STONES) + ' stones left')
        print('Player 1 would you like to remove 1 or 2 stones? ', end = '')
        while(Remove != 1 and Remove != 2):
            Remove = int(input())
            if Remove != 1 and Remove != 2:
                Remove = int(input('Please enter 1 or 2: '))
        TOTAL_STONES = TOTAL_STONES - Remove
        Remove = 0
        if TOTAL_STONES <=0:
            print('\nPlayer 2 wins!')
            break

        print('\nThere are ' + str(TOTAL_STONES) + ' stones left')
        print('Player 2 would you like to remove 1 or 2 stones? ', end = '')
        while(Remove != 1 and Remove != 2):
            Remove = int(input())
            if Remove != 1 and Remove != 2:
                Remove = int(input('Please enter 1 or 2: '))
        TOTAL_STONES = TOTAL_STONES - Remove
        Remove = 0
        print()
        if TOTAL_STONES <=0:
            print('Player 1 wins!')
            break

if __name__ == '__main__':
    main()
