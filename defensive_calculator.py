print("To submit a new equation enter 1.")      # ask user which function to use 
print("To see a list of all equations enter 2.")

user_choice = input("Enter 1 or 2: ")       # ensure if input isn't 1 or 2, the user is
while user_choice != "1" and user_choice != "2":    # prompted to enter again
    user_choice = input("Enter 1 or 2: ")

if user_choice == "1":
                                            # take first number and cast to float, break the loop if
    while True:                             # value is numerical
        try:
            first_number = float(input("Please enter a number: "))
            break
        except ValueError:                  # if a non numerical is input, display error message
            print("That wasn't a number")   # then ask again for input

    operator = input("Please enter an operator (+,-,*,/): ")
    while operator != "+" and operator != "-" and operator != "*" and operator !="/":
        operator = input("Invalid input, please enter an operator (+,-,*,/): ")     # only accept +-/*
                                                                                    # ask again for any other input
    while True:
        try:
            second_number = float(input("Please enter a number: "))
            break
        except ValueError:                  # if a non numerical is input, display error message
            print("That wasn't a number")   # then ask again for input

    if operator == "+":                             # perform calculation on input
        answer = first_number + second_number
    elif operator =="-":
        answer = first_number - second_number
    elif operator == "*":
        answer = first_number * second_number
    elif operator == "/":
        answer = first_number / second_number

    equation = (f"{first_number} {operator} {second_number} = {answer}") 
    print(equation)         # display calculation

    f = open('equations.txt', 'a')      # open file to append to
    f.write(equation + "\n")            # write the equation to txt file
    f.close()                           # close the file

elif user_choice == "2":
    while True:
        file_name = input("Enter the file name: ")      # ask user for the file name
        f = None                                        # set f to none for try loop
        try:
            f = open(file_name, 'r')                    # open file as read
            content = f.read()                          # set file contents to content
            print(content)                             
            break
        except FileNotFoundError:                       # if user input doesn't exist as file, print error message
            print(file_name + " doesn't exist")         # then ask again for input
        finally:
            if f is not None:                           # close the file
                f.close()

