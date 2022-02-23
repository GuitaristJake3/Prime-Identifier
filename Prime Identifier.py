def validation(userinput):
    while True:
        try:
            userinput = int(input("Enter a positive integer:"))     # A given value is tested to see if it is an integer
        except:
            print("Only whole numbers are permitted!")              # If a different data type is input instead,                           
            print("Please try again.")                              # the code loops back and waits for a new input
            continue                                                
        if userinput == 0 or userinput == 1:                        # Special considerations that exclude forbidden values
            print("0 and 1 are neither prime nor composite!")       
            print("Please try again.")                              # If either condition is met, the code
            continue                                                # loops back and waits for a new input
        elif userinput < 0:                                         
            print("Negative numbers are not considered prime.")     # Excludes negative values outside factor_list range
            print("Please try again.")
            continue
        else:                                                       # Breaks out of loop if validation conditions are met
            return userinput

def prime_check(userinput):
    factor_list = [userinput]                                       # Factor list created including userinput number
    for divisor in range(1, userinput):                             # 1 is always added as the second factor
        if userinput % divisor == 0:                                # Each divisor that leaves no remainder is added to list
            factor_list.append(divisor)
        if divisor >= 0.5 * userinput:                              # All quotients above half the user input will be between
            break                                                   # 1 and 2 so there is no reason to continue the loop
    if len(factor_list) == 2:                                       # Checks if any factors are found besides 1 and userinput
        print("This number is prime!")
    else:
        factor_list.sort()                                          # Sorts factors numerically ascending, if found
        print("This number is not prime. Its factors are " + str(factor_list) + ".")

while True:
    prime_check(validation(input))                                  # The prime checking code is called, using the value
    while True:                                                     # returned by calling the validation function                                                           
        repeat = input("Test another number? [y/n]")
        if repeat != "y" and repeat != "n":                         # User can call the prime checking code again
            print("Please enter a valid character.")                # which also has validation to only accept y/n
            continue
        elif repeat == "y":                                         # Break from loop and back to calling prime_check function
            break
        elif repeat == "n":                                         # Terminate program
            quit()