print("Hello, the program you are about to use is to check the Collatz")
print("Conjecture, one of the most famous unsolved problems in mathematics.")
print("The problem is very simple. It says that whatever positive number")
print("You choose, by applying two rules it will always end up with four.")
print("The two rules are:")
print("If the number is =")
print("Even ? Divide by two.")
print("Odd ? Multiply by three and add one.")
print("But what happens after reaching four ?")
print("4 / 2 = 2")
print("2 / 2 = 1")
print("1 x 3 + 1 = 3 + 1 = 4")
print("So we can see that it ends up in a 4, 2, 1 loop.")
print("")
print("Now that you're familiar with the problem, let's start testing!")
print("__________________________________________________________________")
restart_level = "beginning"
while restart_level == "beginning":
    print("What should be the starting point ?")
    while True:
        starting_point = input(">")
        try:
            starting_point = int(starting_point)
            print(f"Ok, the program will start at {starting_point}.")
            break
        except:
            print("You have to enter a positive number with no decimals.")
    verified_set = {1, 2, 4}
    verified_set_2 = {1, 2, 4}
    current_set = {1, 2, 4}
    steps = 0
    print("How do you want the program to run ? Options:")
    print("Long (the program will go through each step until it reaches 4)")
    print("Short (if the program goes through a step it already met before, it will stop and go on to next number)")
    while True:
        full_short = input(">")
        try:
            full_short in ["Long", "Short"]
            if full_short == "Long":
                print("Ok, the program will run through"
                      " every step and show you how many there are.")
                break
            elif full_short == "Short":
                print("Ok, the program will go to the next number"
                      "if it meets a step it already went through.")
                break
            raise Error
        except:
            print("you have to enter on of the two options (Long/Short)")
    restart_level = "ended"
    while restart_level == "ended":
        print("How many times do you want the program to repeat ?")
        while True:
            repeat_range = input(">")
            try:
                repeat_range = int(repeat_range)
                print(f"Ok, the program will repeat {repeat_range} times.")
                break
            except:
                print("You have to enter a positive number with no decimals.")
        for i in range(int(repeat_range)):
            current_number = starting_point
            if full_short == "Long":
                verified_set_2.add(int(starting_point))
            print(current_number)
            while current_number not in verified_set:
                if (int(current_number) % 2) == 0:
                    current_number = int(current_number) // 2
                else:
                    current_number = int(current_number) * 3 + 1

                print(int(current_number))
                current_set.add(int(current_number))
                steps += 1
            if full_short == "Short":
                verified_set.update(current_set)
                print(verified_set)
            elif full_short == "Long":
                print(f"Number of steps before reaching 4 : {steps}")
            starting_point = int(starting_point) + 1
            steps = 0

        if full_short == "Short":
            final_list = list(verified_set)
        else:
            final_list = list(verified_set_2)
        final_list.sort()
        print(f"These are all the numbers that were verified : {final_list}")
        print("Do you want to run the program another time (Options : yes/no) ?")

        while True:
            restart = input(">")
            if restart not in ["yes", "no"]:
                print("You have to enter one of the two options (yes/no).")
            else:
                break
        if restart == "yes":
            print("Do you want to restart from beginning or from where you ended (Options : beginning/ended)?")
            while True:
                restart_level = input(">")
                if restart_level not in ["beginning", "ended"]:
                    print("Your answer must be one of the two options (beginning/ended)")
                else:
                    break
            if restart_level == "ended":
                print("That means the program will start at the number it")
                print("ended with, keep the same running mode (Short/Long)")
                print("and keep the same verified list. You will only be ")
                print("asked how many times it should run.")
            elif restart_level == "beginning":
                print("That means the program will run again completely, as" 
                      " if it was the first time you ran the program.")
        else:
            print("Ok, the program will stop now.")
            break
exit()
