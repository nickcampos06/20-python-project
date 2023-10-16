import math
#import math module for log calculations
def main():
    keep_going = True
    total_result = 0
    latest_result = 0.0
    num_of_calculations = 0
#initiate starting variables for future calculation and loop
    while keep_going:
#initiate a loop that will continue calculating until user stops
        print(f"Current Result: {latest_result}\n")
        menu_choice = menuChoice(total_result, num_of_calculations)
#print the latest result and call on menu function
#send arguments that will be used for average calculations
        if menu_choice == 0:
            keep_going = False
            print("\nThanks for using this calculator. Goodbye!")
#end the program if user chooses to
        else:
            number1, number2 = getOperands()
#call on function to get operands
            latest_result = makeCalculation(menu_choice, number1, number2, latest_result)
#call on function to make calculations and store the result
            total_result += latest_result
#keep track of the sum of all the total for average 
        num_of_calculations += 1
#keep track of the number of calculations for average

def menuChoice(total_result, num_of_calculations):
    valid_menu_choice = False
#initiate loop
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")
#print menu options
    while not valid_menu_choice:
        menu_choice = int(input("\nEnter Menu Selection: "))
#keep loop going until user choses a valid menu option
        if menu_choice >= 0 and menu_choice <= 6:
            valid_menu_choice = True
#make sure the loop doesn't repeat if menu choice is valid
        elif menu_choice == 7:
            average(total_result, num_of_calculations)
#call of average if user selects 7 and ensure loop continues
        else:
            print("\nError: Invalid selection!")
#print error message if bad menu choice and continue loop
    return menu_choice
#return menu option

def getOperands():
    number1 = input("Enter first operand: ")
    number2 = input("Enter second operand: ")
    print("")
    return number1, number2
#get operand from user and return it
#keep as string in case user chose RESULT

def makeCalculation(menu_choice, number1, number2, latest_result):
    if number1 == "RESULT":
        number1 = latest_result
    if number2 == "RESULT":
        number2 = latest_result
#assign number1 or number2 the appropriate value if user chooses RESULT
    
    number1 = float(number1)
    number2 = float(number2)
#convert both numbers to floating point nums

    if menu_choice == 1:
        return number1 + number2
    elif menu_choice == 2:
        return number1 - number2
    elif menu_choice == 3:
        return number1 * number2
    elif menu_choice == 4:
        return number1 / number2
    elif menu_choice == 5:
        return number1 ** number2
    elif menu_choice == 6:
        return math.log(number2, (number1))
#choose the appropriate procedure based on the operation chose by user
#return result

def average(total_result, num_of_calculations):
    if num_of_calculations < 2:
        print("Error: No calculations yet to average!")
#if not enough calculations were performed, print an error
    else:
        print(f"\nSum of calculations: {total_result:.2f}")
        print(f"Number of calculations: {num_of_calculations}")
        print(f"Average of calculations: {total_result / num_of_calculations :.2f}\n")
#print the information for average

if __name__ == '__main__':
    main()
#run main if program is ran independently