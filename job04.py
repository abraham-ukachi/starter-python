##############################
# Name: Job04 - Les boucles while
# Script: job04.py
# Author: Abraham Ukachi <abraham.ukachi@laplateforme.io>
# version: 0.0.1 (alpha)
#
#
# Usage:
#   1-|> python3 job04.py
#
#   2-|> import job04
#
##############################
# IMPORTANT: This code is a work in progress and subject to major changes until version 0.1
##############################

#========== Job 04 ===============
#
#~~~~~~~~~ (French) ~~~~~~~~~~~~~~
#
# - Créez un script job04.py
# - L’utilisateur devra entrer une valeur en input.
# - A l’aide d’une boucle while et d’une fonction system, 
#   affichez nombres se trouvant de 0 (inclus) à l’input (inlus).
#
#~~~~~~~~~~ (English) ~~~~~~~~~~~~
# 
# - Create a job04.py script
# - The user must enter an input value.
# - Using a while loop and a system function, 
#   display numbers from 0 (included) to the input (inlus).
#
#=================================

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MOTTO: I'll always do more 😜!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Import the built-in python `time` module
import time

# Let's define some constants, shall we? ;)
# - Error Message constants
ERR_MSG_NOT_NUM = "not_num"
# - Prompt Sign constants
PROMPT_SIGN_DEFAULT = "\x1b[1m\x1b[34m?\x1b[0m " # <- (bold + blue)
PROMPT_SIGN_IN = "\x1b[1m\x1b[32m>>\x1b[0m " # <- (bold + green)
PROMPT_SIGN_OUT = "\x1b[1m\x1b[34m<<\x1b[0m " # <- (bold + blue)
PROMPT_SIGN_ERR = "\x1b[1m\x1b[31m<<\x1b[0m " # <- (bold + red)
# - Log messages constants
LOG_MSG_WELCOME = "welcome"
LOG_MSG_NUMBER = "number"
LOG_MSG_BUSY = "busy"
LOG_MSG_DONE = "done"

# - Other constants
LANG = "en" # <- default language set to "english", duh!

# Initialize the `logMsg` object too
logMsg = { "en": {}, "fr": {} }

logMsg["en"][LOG_MSG_WELCOME] = "Welcome to Job{}"
logMsg["en"][LOG_MSG_NUMBER] = "What's your number: "
logMsg["en"][LOG_MSG_BUSY] = "printing numbers from {} to {}..."
logMsg["en"][LOG_MSG_DONE] = "...done"


# TODO: Add log messages in "fr" (French)


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


# Define a printToNumber function
def _printToNumber(number, delay = 0):
    """
    Prints from 0 to the given `number`

    @private
    :param { int } number
    :param { int } delay
    """
    
    # Initialize the current number variable `num` to 0
    num = 0
    # Set the maximum number as `maxVal` to the current given `number`
    maxNum = number + 1;

    # While the current number `num` is less or equal to the given `number`...
    while num < maxNum:
        # ...print out the current number
        print(PROMPT_SIGN_OUT + str(num))
        # increase the `num` by 1
        num += 1
        # wait for the specific `delay`
        time.sleep(delay)

    # Tell the world that we are done printing some numbers :-(
    print(logMsg[LANG][LOG_MSG_DONE])
    



# Define our main function
def main():
    # Display a welcome message
    welcomeMessage = logMsg[LANG][LOG_MSG_WELCOME]
    _showWelcomeMessage(welcomeMessage, 4)
    
    # get a number from the user as `value`
    value = input("\n" + PROMPT_SIGN_DEFAULT + logMsg[LANG][LOG_MSG_NUMBER])
    
    # convert the `value` to a number (ie. an integer)
    number = int(value)

    # TODO: Handle non-integer inputs or errors

    # Tell the world that we are about to print some numbers ;-)
    # from 0 to the given `value`
    print(logMsg[LANG][LOG_MSG_BUSY].format(0, number))
    
    # Set the delay to 10 ms
    delay = 0.1

    # print numbers
    _printToNumber(number, delay)



# if `job03.py` is being run directly...
if __name__ == "__main__":
    # ...call our main function
    main()
else:
    # do something else :)
    pass

