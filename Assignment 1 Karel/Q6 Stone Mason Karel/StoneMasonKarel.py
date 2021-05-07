from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
    while front_is_clear():
        turn_left()
        drop()
        turn_reverse()
        if left_is_clear():            
            next_avenue()
    turn_left()
    drop()


def drop():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()

def next_avenue():
    turn_left()
    for i in range(4):
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_reverse():
    turn_left()
    turn_left()
    while front_is_clear():
        move()

if __name__ == '__main__':
    run_karel_program('SampleQuad2.w')
