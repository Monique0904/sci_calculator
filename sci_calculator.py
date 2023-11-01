import math

# holds the value of current result
result = 0.0
# holds the value of calculations
num_of_calc = 0
# holds the menu options
menu = ("Calculator Menu\n---------------\n0. Exit Program\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division"
        "\n""5. Exponentiation\n6. Logarithm\n7. Display Average")

# a list is created to hold the results of the calculations, values within the list are converted from str to int
every_result = []
every_result = [int(i) for i in every_result]

# the current result is printed for the user along with the menu and they are prompted for an input
print(f"Current Result: {result}")
print(f"\n {menu}")
user_selection = int(input("\nEnter Menu Selection:"))

# if the user menu selection is not between 0 and 7 error message printed and user is prompted for another selection
if not 0 <= user_selection <= 7:
    print("\nError: Invalid selection!")
    user_selection = int(input("\nEnter Menu Selection:"))

# runs while the variable value is greater than or equal to 0 but less than or equal to 7
while 0 <= user_selection <= 7:

    # prints goodbye and breaks out of the loop if user chooses to exit program
    if user_selection == 0:
        print("\nThanks for using this calculator. Goodbye!")
        break

    # only prompts for user input if users menu selection is between 1 and 7
    if 0 < user_selection < 7:
        user_num1 = float(input("Enter first operand:"))
        user_num2 = input("Enter second operand:")

        # accepts string 'RESULT' for user_num2 and sets the variable result equal to the result of previous result
        if user_num2 == 'RESULT':
            user_num2 = result

    # if users input is equal to 1 the two values will be added together and printed
    # adds result of operation to the list every_result
    # adds one to the variable keeping track of the number of calculations

    if user_selection == 1:
        result = user_num1 + float(user_num2)
        round(result, 2)
        print(f"\nCurrent Result: {result}")
        every_result.append(result)
        num_of_calc += 1

    # if users input is equal to 2 the two values will be subtracted and printed
    elif user_selection == 2:
        result = user_num1 - float(user_num2)
        round(result, 2)
        print(f"\nCurrent Result: {result}")
        every_result.append(result)
        num_of_calc += 1

    # if users input is equal to 3 the two values will be multiplied and printed
    elif user_selection == 3:
        result = user_num1 * float(user_num2)
        round(result, 2)
        print(f"\nCurrent Result: {result}")
        every_result.append(result)
        num_of_calc += 1

    # if users input is equal to 4 the two values will be divided and printed
    elif user_selection == 4:
        result = user_num1 / float(user_num2)
        round(result, 2)
        print(f"\nCurrent Result: {result}")
        every_result.append(result)
        num_of_calc += 1

    # if users input is equal to 5, the first input will be the base and the second is the exponent
    elif user_selection == 5:
        result = user_num1 ** float(user_num2)
        round(result, 2)
        print(f"\nCurrent Result: {result}")
        every_result.append(result)
        num_of_calc += 1

    # if users input is equal to 6 user_numb1 becomes base of the log, user_numb2 becomes the argument for the operator
    elif user_selection == 6:
        result = math.log(float(user_num2) , user_num1)
        print(f"\nCurrent Result: {result}")
        every_result.append(result)
        num_of_calc += 1

    # runs if menu selection is 7 and calculates the average of calculations
    else:
        if result == 0:
            print("\nError: No calculations yet to average!")
            user_selection = int(input("\nEnter Menu Selection:"))
            continue

        # sets sum_of_calc equal to the sum of all the results and defines avg_calc as the average of results
        # the sum, number, and average of calculations are the printed, user is prompted to input a menu number
        # program goes to the top of the while loop and compares the value to the loop condition

        else:
            sum_of_calc = sum(every_result)
            avg_calc = sum_of_calc / num_of_calc
            print(f"Sum of calculations: {sum_of_calc}")
            print(f"Number of calculations: {num_of_calc}")
            print(f"Average of calculations: {(math.ceil(avg_calc*100)/100)}")
            user_selection = int(input("\nEnter Menu Selection:"))
            continue

    # once operation is run, menu will be printed again and user will be prompted to select a menu number for values 1-7
    print(f"\n {menu}")
    user_selection = int(input("\nEnter Menu Selection:"))