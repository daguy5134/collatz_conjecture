true_false2 = False
try :    
        starting_point = input("What should be the starting point:")
        if isinstance(int(starting_point), int):
            true_false2 = True 
            print(f"Ok, the program will start at {starting_point}.")
except :
    while not true_false2:
        try:    
            if not isinstance(int(starting_point), int):
                raise ValueError
            else:
                true_false2 = True 
                print(f"Ok, the program will start at {starting_point}.")
        except ValueError:
            print("You have to enter a positive number with no decimals")
            starting_point = input("Enter your number again:")
verified_set = {1, 2, 4}
current_set = {1, 2, 4}
true_false = False
try :    
        repeat_range = input("How many times do you want the program to repeat :")
        if isinstance(int(repeat_range), int):
            print(f"Ok, the program will repeat {repeat_range} times.")
            true_false = True 
except :
    while not true_false:
        try:    
            if not isinstance(int(repeat_range), int):
                raise ValueError
            else:
                true_false = True 
                print(f"Ok, the program will repeat {repeat_range} times.")
        except ValueError:
            print("You have to enter a positive number with no decimals")
            repeat_range = input("Enter your number again:")
for i in range(int(repeat_range)):
    current_number = starting_point
    print(current_number)
    while current_number not in verified_set:
        if (int(current_number) % 2) == 0:
            current_number = int(current_number) // 2
        else:
            current_number = int(current_number) * 3 + 1

        print(int(current_number))
        current_set.add(int(current_number))

    verified_set.update(current_set)
    print(verified_set)
    starting_point = int(starting_point) + 1
