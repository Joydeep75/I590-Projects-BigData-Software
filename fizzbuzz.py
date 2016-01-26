# This program is based on python 2.7 and the
# program assumtion is user is entering a valid input.
# Hence data validation section is not added.

## Author: Joydeep Ghatak
## Python version: 2.7

# Take the user input 
input_num = raw_input("Please enter a valid positive number ::  ")

# Function creation for business logic
def fizzbuzz(input_num): 
    print "The input number is ", input_num

    # 'for' loop for iteration between 1 to n
    for num in range (1,int(input_num) + 1):

        # 'if-elif-else' loop for find out business logic
        if (num %2 == 0 and num % 3 == 0):
            print "fizzbuzz", num
        elif (num % 3) == 0:
            print "buzz", num
        elif (num %2 == 0):
            print "fizz", num
        else:
            print num

fizzbuzz(input_num)


