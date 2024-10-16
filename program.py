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
current_set = {1, 2, 4}
while True:
    print("How do you want the program to run ? Options:")
    print("Long (the program will go through each step until it reaches 4)")
    print("Short (if the program goes through a step it already met before, it will stop and go on to next number)")
    full_short = input(">")
    try:
        full_short == "Full" or "Short"
        if full_short == "Full":
            print("Ok, the program will run through" 
                  "every step and show you how many there are.")
        else: 
            print("Ok, the program will go to the next number"
                  "if it meets a step it already went through.")
        break
    except:
        print("you have to enter on of the two options (Long/Short)")
        full_short = input(">")
print("How many times do you want the program to repeat ?")
repeat_range = input(">")
while not isinstance(repeat_range, int):
    print("You have to enter a positive number with no decimals")
    repeat_range = input(">")
print(f"Ok, the program will repeat {repeat_range} times.")
for i in range(int(repeat_range)):
    current_number = starting_point
    print(current_number)
    while current_number not in verified_set:
        steps = 0
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
        print(f"Number of steps : {steps}")

    starting_point = int(starting_point) + 1
        
