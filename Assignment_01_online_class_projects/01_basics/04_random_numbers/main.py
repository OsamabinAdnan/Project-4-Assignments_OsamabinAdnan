#  Random number generator

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

import random

def main():
    for i in range(1, 10):
        print(random.randint(1, 100), end=' ')

main()