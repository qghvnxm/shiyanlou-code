#!/usr/bin/env python3
sticks = 21

print("There are 21 sticks, you can take 1-3 number of sticks at a time.")
print("Whoever will take the last stick will loose")

while True:
    print("Sticks left: " , sticks)
    sticks_taken = int(input("Take sticks(1-3):"))
    if sticks == 1:
        print("You took the last stick, you loose")
        break
    if sticks_taken >= 4 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("Computer took: " , (5 - sticks_taken) , "\n")
    sticks -= 5
