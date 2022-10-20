##############################
# Name: Job07 - Fizz Buzz
# Script: job07.py
# Author: Abraham Ukachi <abraham.ukachi@laplateforme.io>
# version: 0.0.1 (alpha)
#
# Usage:
#   1-|> python3 job07.py
#
#   2-|> import job07 as j7
#    -|> j7.printFizzBuzz(5, 15, "Fizz", "Buzz", "FizzBuzz")
#    -|>
#    =|o-> [1, 2, 'fizz', 4, 'Buzz',...,14, 'FizzBuzz',...]
#
##############################
# IMPORTANT: This code is a work in progress and subject to major changes until version 0.1
##############################

#========== Job 07 ===========
#     >>> DESCRIPTION <<<
#~~~~~~~~~ (French) ~~~~~~~~~~
#
# - Écrire un programme qui parcourt les nombres entiers de 1 à 100. 
# - Pour les multiples de trois, afficher "Fizz" au lieu du nombre et pour 
#   les multiples de cinq afficher "Buzz". 
# - Pour les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".
#
#~~~~~~~~~ (English) ~~~~~~~~~
#
# - Write a program that scans whole numbers from 1 to 100. For multiples of three, 
# - display "Fizz" instead of the number and for multiples of five display "Buzz". 
# - For numbers that are multiples of three and five, display "FizzBuzz".
#
#=============================

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MOTTO: I'll always do more 😜!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# Let's define some constants, shall we? ;)

# - Log messages constants
LOG_MSG_WELCOME = "welcome"
LOG_MSG_BUSY = "busy"
LOG_MSG_DONE = "done"

# - Other constants
LANG = "en" # <- default language set to "english", duh!

# Initialize the `logMsg` object too
logMsg = { "en": {}, "fr": {} }
### [ English ]
logMsg["en"][LOG_MSG_WELCOME] = "Welcome to Job{}"
logMsg["en"][LOG_MSG_BUSY] = "Fizzbuzzing from {} to {}..."
logMsg["en"][LOG_MSG_DONE] = "Done"

### [ French ]
logMsg["fr"][LOG_MSG_WELCOME] = "Bienvenu au Job{}"
logMsg["fr"][LOG_MSG_BUSY] = "Fizzbuzzing de {} à {}..."
logMsg["fr"][LOG_MSG_DONE] = "Fini"


# ======== PRIVATE FUNCTIONS

# Define a welcome message
def _showWelcomeMessage(msg, job):
    """
    Displays a welcome message for the current job
    
    :param { str } msg: the message to be displayed
    :param { int } job: the job number
    """
    print("\x1b[2m") # <- everything should be in gray color
    print("=" * 33) # <- top/open style
    #print("#")
    print("# \t  ✺◟(•‿•)◞✺" + "\t\t#")
    print("# \t" + msg.format(job) + "\t\t#")
    # print("#")
    print("=" * 33) # <- bottom/close style
    print("\x1b[0m") # <- stop coloring
      


# ====== END OF PRIVATE FUNCTIONS ==========





# ======== PUBLIC FUNCTIONS


# Define the `printFizzBuzz` function
def printFizzBuzz(start, end, fizz = "Fizz", buzz = "Buzz", fizzBuzz = "FizzBuzz"):
    """
    Prints a list of numbers ranging from the given `start` to the given `end`,
    in which the following rule is applied to the numbers:
        - multiples of three(3) are substituted with the given `fizz`;
        - multiples of five(5) are substituted with the given `buzz`;
        - multiples of both three(3) and five(5) are substituted with the given `fizzBuzz`
    
    :param { int } start
    :param { int } end
    :param { str } fizz
    :param { str } buzz
    :param { str } fizzBuzz
    """

    # Tell the world that we're about to do some fizz-buzzin'
    print("\x1b[34m%s\x1b[0m\n" % logMsg[LANG][LOG_MSG_BUSY].format(start, end))

    # Initialize a fizzBuzz list 
    fizzBuzzList = []

    # offset/increment `end` by 1 to include it in the list (read job description)
    end += 1
    
    # For each number between `start` to `end` (say, 1 to 100)...
    for num in range(start, end):
        # Hey there!! First, let me explain what I'm about to do:
        # - According to the "Math Gods", any natural number that has `0` as a reminder 
        #   after being divided by `n`

        # So.., if the current number is a multiple of both 3 and 5...
        if (num % 3) == 0 and (num % 5) == 0:
            # ...add `fizzBuzz` to the list
            fizzBuzzList.append(fizzBuzz)
        elif (num % 5) == 0:
            # ...add `buzz` to the list
            fizzBuzzList.append(buzz)
        elif (num % 3) == 0:
            # ..add `fizz` to the list
            fizzBuzzList.append(fizz)
        else:
            # just add the 'boring' number to the list :)
            fizzBuzzList.append(num)

    # TODO: Highlight the important values in `fizzBuzzList`

    # print the fizzBuzz list
    print(fizzBuzzList)

    # Tell the world that we are done print the fizz buzz list
    print("\n\x1b[34m...%s\x1b[0m" % logMsg[LANG][LOG_MSG_DONE])
        


# ====== END OF PUBLIC FUNCTIONS ===========



# Define our main function
def main():
    """
    The main function of Job07 - Fizz Buzz
    """
    # Create a welcome message as `welcomeMsg`
    welcomeMsg = logMsg[LANG][LOG_MSG_WELCOME]
    # Show the welcome message to the world
    _showWelcomeMessage(welcomeMsg, 7)
    
    # Let's do some "fizzing" & "buzzing" from 1 to 100
    # by calling the `printFizzBuzz()` function
    printFizzBuzz(1, 100)



# if `job07.py` is being run directly...
if __name__ == "__main__":
    # ...call our main function
    main()
else:
    # do something else :)
    pass

