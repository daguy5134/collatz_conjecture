while True:
    print("What should be the starting point ?")
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
while True:
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
                print("That means the program will start at the number it"
                      "ended with, keep the same running mode (Short/Long)"
                      "and keep the same verified list. You will only be"
                      "asked how many times it should run.")
    else:
        break
exit()
