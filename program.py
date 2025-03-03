"""
-------------------------------------------------------------------------------
script for collatz conjecture
-------------------------------------------------------------------------------
"""

import math
import time
import matplotlib.pyplot as plt

print("Hello, the program you are about to use is to check the Collatz Conjecture.")
time.sleep(2)
print("Are you familiar(f) with it or do you need an introduction(i)?")
intro = input(">")
while intro not in ["f", "i"]:
    print('You have to enter either "f" for familiar or "i" for introduction.')
    intro = input(">")
if intro == "i":
    print("The Collatz Conjecture is one of the most famous unsolved problems in mathematics.")
    time.sleep(2)
    print("The problem is very simple. It says that whatever positive number")
    time.sleep(2)
    print("you choose, by applying two rules it will always end up with four.")
    time.sleep(2)
    print("The two rules are:")
    time.sleep(1)
    print("If the number is =")
    time.sleep(1)
    print("Even ? Divide by two.")
    time.sleep(1)
    print("Odd ? Multiply by three and add one.")
    time.sleep(2)
    print("But what happens after reaching four ?")
    time.sleep(2)
    print("4 / 2 = 2")
    time.sleep(1)
    print("2 / 2 = 1")
    time.sleep(1)
    print("1 x 3 + 1 = 3 + 1 = 4")
    time.sleep(2)
    print("So we can see that it ends up in a 4, 2, 1 loop.")
    time.sleep(2)
    print(" ")
    time.sleep(1)
    print("Now that you're familiar with the problem, let's start testing!")
    time.sleep(1)
    print("__________________________________________________________________")
    time.sleep(1)
restart_level = "b"
while restart_level == "b":
    print("What do you want to do ? Options :")
    time.sleep(1)
    print("""Single number (s) = This will only test one number and 
will generate a graphic with all the steps.""")
    print("""Multiple numbers (m) = This will test a series of numbers.
You will be able to choose many parameters like 
the amount of numbers to test and which one to start with.""")
    single_many = input(">")
    while single_many not in ["s", "m"]:
        print("You have to enter one of the two options (s/m).")
        single_many = input(">")
    if single_many == "m":
        print("What should be the starting point ?")
        while True:
            starting_point = input(">")
            starting_point = starting_point.replace(" ", "")
            try:
                starting_point = int(starting_point)
                print(f"Ok, the program will start at {starting_point}.")
                break
            except ValueError:
                print("You have to enter a positive number with no decimals.")
        verified_set = {1, 2, 4}
        verified_set_2 = {1, 2, 4}
        current_set = {1, 2, 4}
        steps = 0
        print("How do you want the program to run ? Options:")
        print("Long(l) = the program will go through each step until it reaches 4. ")
        print("Short(s) = if the program goes through a step it already met before,")
        print("           it will stop and go on to next number (Faster).")
        full_short = input(">")
        while full_short not in ["l", "s"]:
            print("you have to enter on of the two options (l/s)")
            full_short = input(">")
        if full_short == "l":
            print("Ok, the program will run through")
            print("every step and show you how many there are.")
        elif full_short == "s":
            print("Ok, the program will go to the next number")
            print("if it meets a step it already went through.")
        restart_level = "e"
        presentation = False
        while restart_level == "e":
            restart_level = ""
            print("How many times do you want the program to repeat ?")
            while True:
                repeat_range = input(">")
                repeat_range = repeat_range.replace(" ", "")
                try:
                    repeat_range = int(repeat_range)
                    print(f"Ok, the program will repeat {repeat_range} times.")
                    break
                except ValueError:
                    print("You have to enter a positive number with no decimals.")
            total_sqrt1 = math.sqrt(int(repeat_range))
            total_sqrt = math.ceil(int(total_sqrt1))
            while total_sqrt ** 2 < total_sqrt1 ** 2:
                total_sqrt += 1
            if not presentation:
                print("")
                time.sleep(1)
                print("____________________________________________________________________")
                print("")
                time.sleep(1)
                if full_short == "l":
                    print("Here is an example of what the program will look like:")
                    time.sleep(3)
                    print("3  <-- first number")
                    time.sleep(2)
                    print("""__
10 |
5  |
16 | ---- The steps before reaching four
8  |
4  |
--- """)
                    time.sleep(4)
                    print("{3, 10, 5, 16, 8}  <-- All the numbers verified before reaching four")
                    time.sleep(3)
                elif full_short == "s":
                    print("Here is an example of what the program will look like:")
                    time.sleep(3)
                    print("3  <-- first number")
                    time.sleep(2)
                    print("""__
10 |
5  |
16 | ---- The steps before reaching a number already verified
8  |
4  |
--- """)
                    time.sleep(4)
                    print("{3, 10, 5, 16, 8}  <-- All the numbers verified this time")
                    time.sleep(3)
                print("")
                print("_____________________________________________________________")
                print("")
                presentation = True
            current_array = []
            position = 0
            for i in range(int(repeat_range)):
                position += 1
                current_number = starting_point
                if full_short == "l":
                    verified_set_2.add(int(starting_point))
                print(current_number)
                while current_number not in verified_set:
                    current_array.append(int(current_number))
                    if (int(current_number) % 2) == 0:
                        current_number = int(current_number) // 2
                    else:
                        current_number = int(current_number) * 3 + 1

                    print(int(current_number))
                    current_set.add(int(current_number))
                    steps += 1
                if full_short == "l":
                    plt.xticks([])
                    plt.yticks([])
                    plt.subplot(int(total_sqrt), int(total_sqrt), int(position))
                    plt.plot(current_array)
                    plt.title(f"Number = {starting_point}", fontsize=5)
                if full_short == "s":
                    verified_set.update(current_set)
                    print(current_set)
                elif full_short == "l":
                    print(f"Number of steps before reaching 4 : {steps}")
                starting_point = int(starting_point) + 1
                steps = 0
            final_list = []
            if full_short == "s":
                final_list = list(verified_set)
            elif full_short == "l":
                final_list = list(verified_set_2)
                plt.show()
            final_list.sort()
            print(f"These are all the numbers that were verified : {final_list}")
    else:
        print("What is the number you want to test ?")
        while True:
            test_number = input(">")
            test_number = test_number.replace(" ", "")
            try:
                test_number == int(test_number)
                print(f"Ok, the program will test the number {test_number}.")
                break
            except ValueError:
                print("You have to enter a positive number with no decimal.")
        print("This is an example of what the program will look like :")
        time.sleep(2)
        print("3 <--- Your number")
        time.sleep(1)
        print("""__
10 |
5  |
16 |
8  | ----- All the steps
4  |
2  |
1  |
---""")
        time.sleep(2)
        print("Then the program will generate a graphic of all the steps.")
        time.sleep(3)
        current_number = test_number
        current_array = []
        while current_number != 1:
            current_array.append(int(current_number))
            print(current_number)
            if (int(current_number) % 2) == 0:
                current_number = int(current_number) // 2
            else:
                current_number = int(current_number) * 3 + 1
        plt.plot(current_array)
        plt.xlabel("Number of steps")
        plt.ylabel('Value of steps')
        plt.title(f"Trajectory of the Collatz Conjecture starting with {test_number}")
        plt.show()
    print("Do you want to run the program another time [yes(y)/no(n)] ?")

    while True:
        restart = input(">")
        if restart not in ["y", "n"]:
            print("You have to enter one of the two options (y/n).")
        else:
            break
    if restart == "y":
        if single_many == "m":
            print("Do you want to restart from beginning(b) or from where you ended(e)?")
            while True:
                restart_level = input(">")
                if restart_level not in ["b", "e"]:
                    print("Your answer must be one of the two options (b/e)")
                else:
                    break
            if restart_level == "e":
                print("That means the program will start at the number it")
                time.sleep(3)
                print("ended with, keep the same running mode (Short/Long)")
                time.sleep(3)
                print("and keep the same verified list. You will only be ")
                time.sleep(3)
                print("asked how many times it should run.")
                time.sleep(3)
            elif restart_level == "b":
                print("That means the program will run again completely, as")
                time.sleep(3)
                print(" if it was the first time you ran the program.")
                time.sleep(3)
    else:
        print("Ok, the program will stop now.")
        break
exit()
