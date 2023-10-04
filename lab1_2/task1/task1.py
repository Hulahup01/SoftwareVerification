"""
Task 1. Write a program that outputs an inscription to the console
Hello, world!
Andhiagain!
!!!!!!!!!!
The number of exclamation marks in the third line should be random in the range of 5-50.
"""

import random
import sys
import subprocess


def task1_solv():
    print("Hello, world!")
    print("Andhiagain!")
    print("!" * random.randint(5, 50))


if __name__ == "__main__":
    task1_solv()
