starting_point = 1
verified_set = {1, 2, 4}
current_set = {1, 2, 4}
true_false = False
while not true_false:
    try :    
        repeat_range = input("How many times do you want the program to repeat :")
        if isinstance(int(repeat_range), int):
            print("Ok, the program will repeat {repeat_range} times.")
            true_false = True
    except ValueError :
        repeat_range = input("You have to enter a positive number with no decimals :")
for i in range(int(repeat_range)):
    current_number = starting_point
    print(current_number)
    while current_number not in verified_set:
        if (current_number % 2) == 0:
            current_number = current_number / 2
        else:
            current_number = current_number * 3 + 1

        print(int(current_number))
        current_set.add(int(current_number))

    verified_set.update(current_set)
    print(verified_set)
    starting_point = starting_point + 1
        
