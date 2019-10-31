"""--------------------------------------------------------------------
PROGRAM INFO COMMENT
    Shawn Ballinger
    CSC119-004
    Project: bulls_cows.py
    Description: Third iteration of bulls and cows games, leaving out the comparison portion.
    Date: 10/25/19
--------------------------------------------------------------------"""

#----------------------------------------------------------------------
#
# DESCRIPTION OF THE MAIN PROGRAM - This will eventually be a game where a random 'mystery code' is
# generated and a user takes a guess at it. Matching numbers will be counted as bulls and matching numbers
# not in the same positio are cows. At least, I think that's the point of the game. 
#
#----------------------------------------------------------------------


def main():


    # Import random generator

    from random import randint


    # Generate a random four digit code with four unique integers and index.

    code = randint(1,9999)

    code0 = int(code // 1000) % 10     
    code1 = int(code // 100) % 10
    code2 = int(code // 10) % 10
    code3 = int(code % 10)



    # Initialize 'duplicate' as a boolean variable. The following blocks check each indexed integer.
    # There is no need to do a specific check for the last integer position as it is implicit in the other three.


    duplicate = 0


    # Check for duplicates of first integer

    if code0 == code1 :
        duplicate = True
    elif code0 == code2 :
        duplicate = True
    elif code0 == code3 :
        duplicate = True
    

    # Check for duplicates of the second integer

    if code1 == code0 :
        duplicate = True
    elif code1 == code2 :
        duplicate = True
    elif code1 == code3 :
        duplicate = True
   

    # Check for duplicate of the third integer

    if code2 == code0 :
        duplicate = True
    elif code2 == code1 :
        duplicate = True
    elif code2 == code3 :
        duplicate = True


    
    # If there are duplicates the code enters a loop where it will
    # generate a new code until 'duplicates' is False. 


    while duplicate == True :


        duplicate = 0                       # this resets duplicate to 0 or else it will cause an infinite loop


        # Generate random code

        code = randint(1,9999)
        print("")
        print("%0.4d" % code)
        print("")


        # Index each integer in the code

        code0 = int(code // 1000) % 10      
        code1 = int(code // 100) % 10
        code2 = int(code // 10) % 10
        code3 = int(code % 10)


        # Check for a duplicate of code0

        if code0 == code1:
            duplicate = True
        elif code0 == code2 :
            duplicate = True
        elif code0 == code3 :
            duplicate = True
    

        # Check for duplicate of code1

        if code1 == code0 :
            duplicate = True
        elif code1 == code2 :
            duplicate = True
        elif code1 == code3 :
            duplicate = True
   

        # Check for duplicate of code2

        if code2 == code0 :
            duplicate = True
        elif code2 == code1 :
            duplicate = True
        elif code2 == code3 :
            duplicate = True


    else:
        print("")
        print("Succesful non-duplicated code found: ", "%0.4d" % code)
        print("")



    #
    ## User inputs a guess and it is checked to be a number with only 4 digits with a while loop.
    # 


    userGuessInput = input("Please enter a guess at the winning 4 digit code: ")

    while userGuessInput.isdigit() == False or len(userGuessInput) != 4 :
        userGuessInput = input("Incorrect input. Please enter a 4 digit code: ")


    # The user guess is initialized indexed for later use

    guess = str(userGuessInput)

    # guess0 = int(guess[0])
    # guess1 = int(guess[1])  
    # guess2 = int(guess[2])
    # guess3 = int(guess[3])


    # Initialize bull and cow counts as integer variables

    bullCount = 0
    cowCount = 0


    # Graphics and titles as constants

    STARS_LINE = "*" * 34
    DASHES_LINE = "-" * 34
    GAME_CODE_TITLE = "GAME CODE:"
    CODE_TITLE = "CODE:"
    GUESS_TITLE = "Guess:"



    # Process and output the random code results and the user guess input number

    print("")
    print(STARS_LINE)
    print("%12s" % GAME_CODE_TITLE , "%0.4d" % code)
    print(DASHES_LINE)
    print("Enter Guess:" , guess)
    print(DASHES_LINE)
    print("%12s"  % CODE_TITLE , "%0.4d" % code, "  Bulls   Cows")
    print("%12s"  % GUESS_TITLE , guess , " %4.d  %6.d" % (bullCount, cowCount))
    print(STARS_LINE)
    print("")

    

main()


"""----------------------------------------------------------------------
_________________________________________________________________________

Test Cases
_________________________________________________________________________

Test Case 1


Succesful non-duplicated code found:  0186

Please enter a guess at the winning 4 digit code: 0923

**********************************
  GAME CODE: 0186
----------------------------------
Enter Guess: 0923
----------------------------------
       CODE: 0186   Bulls   Cows
      Guess: 0923     0       0
**********************************


_________________________________________________________________________

Test Case 2


Succesful non-duplicated code found:  4258

Please enter a guess at the winning 4 digit code: 9876

**********************************
  GAME CODE: 4258
----------------------------------
Enter Guess: 9876
----------------------------------
       CODE: 4258   Bulls   Cows
      Guess: 9876     0       0
**********************************


_________________________________________________________________________

Test Case 3


9956


5770


2353


7448


5700


1992


4564


2866


7404


1201


4840


9374


Succesful non-duplicated code found:  9374

Please enter a guess at the winning 4 digit code: 2019

**********************************
  GAME CODE: 9374
----------------------------------
Enter Guess: 2019
----------------------------------
       CODE: 9374   Bulls   Cows
      Guess: 2019     0       0
**********************************


_________________________________________________________________________

End Test Cases
_________________________________________________________________________
----------------------------------------------------------------------"""