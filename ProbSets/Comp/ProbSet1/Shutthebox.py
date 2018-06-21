import box
import time
import sys
import random

#Require three total command line arguments
if len(sys.argv) != 3:
    print("You need exactly 3 arguments")
    quit()
name = sys.argv[1]
timelim = sys.argv[2]
timelimsec = int(timelim)

remaining = list(range(1, 10))
begintime = time.time()
timediff = 0

while timelimsec - timediff > 0:
    print("Numbers left: ", remaining)
    if sum(remaining) <= 6:
        dice = random.randint(1, 6)
    else:
        dice = random.randint(1, 6) + random.randint(1, 6)
    print("Roll: ", dice)
    if not box.isvalid(dice, remaining):
        print("Game Over")
        summ = sum(remaining)
        print("Score for player ", name, ":", summ ," points")
        print("Time played: ", timediff, "seconds")
        print("Better luck next time >:")
        quit()
    timediff = time.time() - begintime
    print("Seconds left: ", timelimsec - timediff)
    inputs = False
    while inputs == False:
        name_input = input("Numbers to eliminate: ")
        parsed_input = box.parse_input(name_input, remaining)
        if parsed_input:
            if sum(parsed_input) == dice:
                for i in range(1, len(parsed_input) + 1):
                    remaining.remove(parsed_input[i-1])
                inputs = True
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    print("")
    if not remaining:
        print("Score for player ", name, ": 0 points")
        print("Time played: ", timediff, "seconds")
        print("Congratulations!! You shut the box!")
        quit()
print("Game over")
sum(remaining)
print("Score for player ", name, ":", summ,"points")
print("Time played: ", timediff, "seconds")
print("Better luck next time >:")
