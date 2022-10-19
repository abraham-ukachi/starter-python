##############################
# Name: Job05 - Les boucles For
# Script: job05.py
# Author: Abraham Ukachi <abraham.ukachi@laplateforme.io>
# version: 0.0.1 (alpha)
#
# Usage:
#   1-|> python3 job05.py
#
#   2-|> import job05
#    -|> job05.printRange(-10, 5, 0.2)
#
##############################
# IMPORTANT: This code is a work in progress and subject to major changes until version 0.1
##############################

#========== Job 05 ===========
#     >>> DESCRIPTION <<<
#~~~~~~~~~ (French) ~~~~~~~~~~
#
# - Créez un script job05.py
# - L’utilisateur devra entrer deux valeurs en input.
# - A l’aide d’une boucle for et d’une fonction system, 
#   affichez uniquement les nombres se trouvant entre l’input 1 et l’input 2. 
# - Le programme doit toujours partir de l’input 1 et aller jusqu’à l’input 2.
# - Si les deux sont égaux, le programme devra écrire “Valeurs égales”.
#
#~~~~~~~~~ (English) ~~~~~~~~~
#
# - Create a job05.py script
# - The user must enter two input values. 
# - Using a for loop and a system function, 
#   display only the numbers between input 1 and input 2. 
# - The program should always start from input 1 and go to input 2. 
# - If both are equal, the program should write “Equal values”
#
#=============================

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MOTTO: I'll always do more 😜!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Import the built-in `time` module
import time

# Let's define some constants, shall we? ;)
# - Error Message constants
ERR_MSG_SAME_VAL = "same_val"
# - Prompt Sign constants
PROMPT_SIGN_DEFAULT = "\x1b[1m\x1b[34m?\x1b[0m " # <- (bold + blue)
PROMPT_SIGN_IN = "\x1b[1m\x1b[32m>>\x1b[0m " # <- (bold + green)
PROMPT_SIGN_OUT = "\x1b[1m\x1b[34m<<\x1b[0m " # <- (bold + blue)
PROMPT_SIGN_ERR = "\x1b[1m\x1b[31m<<\x1b[0m " # <- (bold + red)
# - Log messages constants
LOG_MSG_WELCOME = "welcome"
LOG_MSG_VAL1 = "val1"
LOG_MSG_VAL2 = "val2"
LOG_MSG_BUSY = "busy"
LOG_MSG_DONE = "done"

# - Other constants
LANG = "en" # <- default language set to "english", duh!


# Initialize the `errorMsg` object/dict with english(EN) and french(FR)
errorMsg = { "en": {}, "fr": {} }
errorMsg["en"][ERR_MSG_SAME_VAL] = "value 1 & 2 are the same"

# TODO: Add error messages in "fr" (french)

# Initialize the `logMsg` object too
logMsg = { "en": {}, "fr": {} }
logMsg["en"][LOG_MSG_WELCOME] = "Welcome to Job{}"
logMsg["en"][LOG_MSG_VAL1] = "Enter your first value:"
logMsg["en"][LOG_MSG_VAL2] = "Enter your second value:"

logMsg["en"][LOG_MSG_BUSY] = "printing numbers between {} and {}..."
logMsg["en"][LOG_MSG_DONE] = "...done"


# TODO: Add log messages in "fr" (French)


# === PUBLIC FUNCTIONS

# Define the `printRange` function
def printRange(val1, val2, delay = 0.1):
    """
    Prints all the numbers between `val1` and `val2`,
    and always starts printing from `val1` to `val2`
    
    :param { int } val1
    :param { int } val2
    :delay { float } delay: 10 millisecond (default)
    """

    # NOTE: There are easier ways to do all this, but I just wanna do it "MY WAY" :)
    
    # Do nothing if `val1` or `val2` is not a number
    if type(val1) != int or type(val2) != int:
        return False # <- IDEA: use continue instead, hhmmmm...

    # Tell the world we're about to print numbers between `val1` and `val2`
    print("\n" + logMsg[LANG][LOG_MSG_BUSY].format(val1, val2))
    
    # Wait for twice the given `delay`
    time.sleep(delay * 2)
    
    # Calculate the difference between `val1` and `val2`:
    # if `val1` is greater than `val2`, subtract `val2` from `val1`
    # but if not, then subtract `val1` from `val2`
    diff = (val1 - val2) if (val1 > val2) else (val2 - val1)
    
    # Compute the correct incrementation b/n the given values, starting from `val1`
    # ie. if `val1` (say, 5) is greater than `val2` (say, -2), 
    #     incrementation is negative 'cause we wanna start counting from "big" to "small"
    increment = -1 if (val1 > val2) else 1

    # Now, let's print THE NUMBERSSSSS !!!! :)
    
    # DEBUG: tell dbsmaster about it :)
    # print("[4dbsmaster]: diff => {} | increment => {}".format(diff, increment))

    # For each number (num) in the difference (diff)...
    for num in range(diff):
        # ...calculate the result using the current `num` and predefined `increment`
        result = val1 + (num * increment) # <- eg. 5 + (1 * -1) => 5 + (-1) => 4
        # ^^^^^ explanation: let's say `val1` is [5], `val2` is [1], and `num` is [1],
        #           our `increment` will therefore be [-1], As a result, we'd wanna add 
        #           the product of `num` + `increment` to `val1` in order to get closer
        #           and closer to `val2` (i.e. our first result = 5 + (1 * -1) = 4)
        
        # Just to be safe & following this job's guidelines, 
        # do nothing or skip to the next iteration, if the current `result` is the same as
        # the given `val1` or `val2`
        if result == val1 or result == val2:
            continue

        # print out the stringified `result`
        print(PROMPT_SIGN_OUT + str(result))

        # wait for the specified `delay` before printing the next result
        time.sleep(delay)




# ======= END OF PUBLIC FUNCTIONS =======



# === PRIVATE FUNCTIONS

# Define the `_getValue` function
def _getValue(msg):
    """
    Returns the value/number the user enters as input.
    This method also Displays the given message `msg`

    @private
    :param { str } msg
    :return { int } value
    """
    # print the message with the default prompt
    print(PROMPT_SIGN_DEFAULT + str(msg))

    # Get the user's input as `value`
    value = input(PROMPT_SIGN_IN)

    # Convert `value` to an integer
    value = int(value)
    # Return the `value`
    return value


# Define a welcome message
def _showWelcomeMessage(msg, job):
    """
    Displays a welcome message for the current job
    
    @private
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
    

#========= END OF PRIVATE FUNCTIONS =======

# Define our main function
def main():
    """
    The main function of Job05 - Les boucles For
    """
    # Create the welcome message
    welcomeMsg = logMsg[LANG][LOG_MSG_WELCOME]
    # Show the welcome message
    _showWelcomeMessage(welcomeMsg, 5);
    
    # Value 1
    # Define value1's message as `msg1`
    msg1 = logMsg[LANG][LOG_MSG_VAL1]
    # Get the user's fist value as `val1`
    val1 = _getValue(msg1)
     
    # Value 2
    # Define value2's message as `msg2`
    msg2 = logMsg[LANG][LOG_MSG_VAL2]
    # Get the user's second value as `val2`
    val2 = _getValue(msg2)
    
    
    # If both `val1` and `val2` are the same...
    if (val1 == val2):
        # ...tell the user that both values are the same
        print("\n" + PROMPT_SIGN_ERR + errorMsg[LANG][ERR_MSG_SAME_VAL])
    else:
        # print the range between the 2 values
        printRange(val1, val2)
    
    # print("val1 => {} and val2 => {}".format(val1, val2))
    

# if `job05.py` is being run directly...
if __name__ == "__main__":
    # ...call our main function
    main()
else:
    # do something else :)
    pass

