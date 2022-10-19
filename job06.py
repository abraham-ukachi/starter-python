##############################
# Name: Job06 - Les boucles infinies
# Script: job06.py
# Author: Abraham Ukachi <abraham.ukachi@laplateforme.io>
# version: 0.0.1 (alpha)
#
# Usage:
#   1-|> python3 job06.py
#
#   2-|> import job06 as j6
#    -|> j6.launchPrompt(">>>")
#
##############################
# IMPORTANT: This code is a work in progress and subject to major changes until version 0.1
##############################

#========== Job 06 ===========
#     >>> DESCRIPTION <<<
#~~~~~~~~~ (French) ~~~~~~~~~~
#
# - Créez un script job06.py
# - Lorsque l’utilisateur va lancer le script, un prompteur devra s’afficher “>”, 
#   et le programme devra attendre un input. 
# - Si l’input entré est “Bonjour”, le programme devra répondre “Bonjour à toi”.
# - Si l’input entré est “Au revoir”, le programme devra quitter.
#
#~~~~~~~~~ (English) ~~~~~~~~~
#
# - Create a job06.py script
# - When the user launches the script, a prompter must be displayed “>”, 
#   and the program must wait for an input. 
# - If the input entered is “Hello”, the program must answer “Hello to you”
# - If the input entered is “Goodbye”, the program must exit.
#
#=============================

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MOTTO: I'll always do more 😜!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# Let's define some constants, shall we? ;)

# - Prompt Status constants
PROMPT_STATUS_ACTIVE = "active"
PROMPT_STATUS_DISABLED = "disabled"
# - Log messages constants
LOG_MSG_WELCOME = "welcome"
LOG_MSG_HELLO = "hello"
LOG_MSG_BYE = "bye"
LOG_MSG_REPLY = "reply"

# - Emoji constants
EMOJI_WAVING_HAND = "\U0001F44B"
EMOJI_GRINNING_FACE = "\U0001F600"
EMOJI_LOUDLY_CRYING_FACE = "\U0001F62D"

# - Other constants
LANG = "en" # <- default language set to "english", duh!

# Initialize the `logMsg` object too
logMsg = { "en": {}, "fr": {} }
### [ English ]
logMsg["en"][LOG_MSG_WELCOME] = "Welcome to Job{}"
logMsg["en"][LOG_MSG_HELLO] = "Hello"
logMsg["en"][LOG_MSG_BYE] = "Goodbye"
logMsg["en"][LOG_MSG_REPLY] = "Hello to you"
### [ French ]
logMsg["fr"][LOG_MSG_WELCOME] = "Bienvenu au Job{}"
logMsg["fr"][LOG_MSG_HELLO] = "Bonjour"
logMsg["fr"][LOG_MSG_BYE] = "Au revoir"
logMsg["fr"][LOG_MSG_REPLY] = "Bonjour à toi"


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
    

# Define the `_updatePromptStatus` function
def _updatePromptStatus(promptStatus):
    """
    Updates the current prompt code

    :param { str } prompStatus
    """
    # make __promptStatus__ a global variable
    global __promptStatus__
    # Initialize the `__promptStatus__` variable with the given `promptStatus`
    __promptStatus__ = promptStatus


# Method used to handle the user's input
def _handleUserInput(value):
    """
    Handles the user's input 

    :param { str } value
    """
    
    # If the given `value` is hello (in either french or english)..
    if value.lower() == logMsg[LANG][LOG_MSG_HELLO].lower():
        # ...print out the appropriate reply
        print("\x1b[32m%s\x1b[0m" % logMsg[LANG][LOG_MSG_REPLY])

    elif value.lower() == logMsg[LANG][LOG_MSG_BYE].lower():
        # ...show a ':waving_hand:' emoji
        print("{} {}".format(EMOJI_WAVING_HAND, EMOJI_LOUDLY_CRYING_FACE))
        # exit or interrupt the prompt
        interruptPrompt()
    else:
        # just echo-like the `value` in gray
        print("\x1b[2m%s\x1b[0m" % value)
    



# ====== END OF PRIVATE FUNCTIONS ==========




# ======== PUBLIC FUNCTIONS

# Define the `getCurrentPromptStatus` function
def getCurrentPromptStatus():
    """
    Returns the current prompt status

    :return { str } currentPromptStatus
    """
    
    # Intialize the `currentPromptStatus` variable
    currentPromptStatus = ""

    try:
        currentPromptStatus = __promptStatus__
    except NameError:
        currentPromptStatus = PROMPT_STATUS_DISABLED

    # return the `currentPromptStatus`
    return currentPromptStatus


# Define the `launchPrompt` function
def launchPrompt(sign = ">"):
    """
    Launches a custom prompt

    :param { str } sign
    :return { bool } : `True` if the prompt was launched successfully
    """

    # get the prompt's current status
    promptStatus = getCurrentPromptStatus()
    
    # Do nothing if the prompt has already been lauched
    # or if it's status is active
    if promptStatus == PROMPT_STATUS_ACTIVE: 
        return False

    # Update the prompt status to 'active'
    _updatePromptStatus(PROMPT_STATUS_ACTIVE)
    
    # While the current prompt status is ACTIVE...
    while getCurrentPromptStatus() == PROMPT_STATUS_ACTIVE:
        # ...get the user input as `value`
        value = input("\x1b[1m\x1b[36m%s\x1b[0m " % sign) # <- sign_color:(bold + green)
        # handle the user input
        _handleUserInput(value)




# Define the `interruptPrompt` function
def interruptPrompt():
    """
    Interrupts, cancels or disables the prompt
    """
    # Update the prompt status to "disabled"
    _updatePromptStatus(PROMPT_STATUS_DISABLED)


# ====== END OF PUBLIC FUNCTIONS ===========



# Define our main function
def main():
    """
    The main function of Job06 - Les boucles infinies
    """
    # Create a welcome message as `welcomeMsg`
    welcomeMsg = logMsg[LANG][LOG_MSG_WELCOME]
    # Show the welcome message to the world
    _showWelcomeMessage(welcomeMsg, 6)

    # launch our custom prompt
    launchPrompt()




# if `job06.py` is being run directly...
if __name__ == "__main__":
    # ...call our main function
    main()
else:
    # do something else :)
    pass

