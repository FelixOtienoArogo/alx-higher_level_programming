#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {abs(number) % 10}", end=" ")
if number > 0:
    print(f"Last digit of {number} is {abs(number) % 10}", end=" ")
    if abs(number) % 10 > 5:
        print(f"and is greater than 5")
    elif abs(number) % 10 == 0:
        print(f"and is 0")
    elif (abs(number) % 10) < 6 and (abs(number) % 10) > 0:
        print(f"and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {-(abs(number) % 10)}\
 and is less than 6 and not 0")
