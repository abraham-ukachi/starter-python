##############################
# Name: Job03 - Les types et conditions
# Script: job03.py
# Author: Abraham Ukachi <abraham.ukachi@laplateforme.io>
# version: 0.0.1 (alpha)
#
# Usage:
#   1-|>  python3 job03.py
#
#   2-|>  import job03
#    -|>  job03.getAge(msg = "What's your age?", errMsg = "Try again", minAge = 18)
#
##############################


#========== Job 03 ===============
#
#~~~~~~~~~ (French) ~~~~~~~~~~~~~~
# - Créez un script job03.py qui dans un premier temps va afficher la phrase \
# “Bonjour, quel âge as tu ? ”
# - L’utilisateur devra ensuite entrer son âge.
# - Déclarez une variable “âge”, qui prendra la valeur saisie par l’utilisateur.
# - A l’aide d’une fonction system, affichez “Tu es mineur” si l’âge est \
# inférieur à 18, et “Tu es majeur” si l’âge est supérieur ou égal à 18.
#~~~~~~~~~~ (English) ~~~~~~~~~~~~
# ??? 
#=================================

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MOTTO: I'll always do more 😜!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Define the minimum age variable as `minAge`
# and initialize it with the number: 18 (per our assignment)
minAge = 18
# Intialize the `greeting` variable
greeting = "Hello" # <-FR: "Bonjour"
# Intialize the `question` variable
question = "how old are you:" # <-FR: "quel âge as tu ?"

# Create a message with `greeting` and `question` using the built-in <format> method.
# ^^^^^why? A: I just wanna do more ;)
message = "{}, {}".format(greeting, question)

# Create an error message
errorMessage = "Please, enter a valid age:" # <-FR TODO: Please, enter a valid age :

# Create a message for the minor
minorMessage = "You are a minor" # <-FR: "Tu es mineur"

# Create a message for the major
majorMessage = "You are a major" # <-FR: "Tu es major"



# Define a `getAge` function
def getAge(minAge, msg = message, errMsg = errorMessage):
    """
    Request for an `age` and return it as an integer, no matter what :)

    :param (int) minAge: The minimum age allowed;
    :param (str) msg: The message to be displayed before requesting the age;
    :param (str) errMsg: The error message 
       
    :return (int) age:
    """
    # If the message `msg` is not empty
    if len(msg) > 0:
        # Display the message with a leading `?` (in. bold + blue)
        # just like in in github's `gh` cli
        print("\n\x1b[1m\x1b[36m?\x1b[0m %s" % message)
    
    # Get the user's age as `age`
    age = input("\x1b[1m\x1b[32m>>\x1b[0m ")
    
    # Use a try/except block, 
    # to make sure the user entered a valid age (ie. number, NOT text)
    # Try to convert age from it's default string value to integer...
    try:
        # Try to convert the given `age` to a number
        age = int(age)
    except:
        # Display the error message (in. bold + red)
        print("\n\x1b[1m\x1b[31m?\x1b[0m %s" % errMsg)
        # print("\x1b[1m\x1b[31m%s\x1b[0m" % errMsg)
        # If the conversion fails (ie. the user didn't enter a number)
        # re-ask the user with the `errorMessage` 
        # by calling the `getAge` function recursively
        age = getAge(minAge, "", errorMessage)

    # Return the `age` as an integer (int) / number
    return age



# Define the `checkAge` function
def checkAge(age, minAge = minAge, minorMsg = minorMessage, majorMsg = majorMessage):
    """
    Displays the `minorMsg` or `majorMsg`, if the given `age` is lower 
    or higher than `minAge` respectively.

    :param (int) age: Current age
    :param (int) minAge: Minimum age allowed
    :param (str) minorMsg: Message to be displayed for a minor
    :param (str) majorMsg: Message to be displayed for a major
    
    :return (bool) result: `True` if the given `age` is a minor
    """
    # Set the result to `False`
    result = False

    # If `age` is lesser than the minimum age... 
    if age < minAge:
        # ...tell the world that he/she is a minor :/ (in. green + bold + white) 
        print("\x1b[1m\x1b[36m<<\x1b[0m \x1b[1m%s\x1b[0m" % minorMsg)
        # Set `result` to `True`
        result = True
    else:
        # ...tell the world that he/she is a major :)
        print("\x1b[1m\x1b[36m<<\x1b[0m \x1b[1m%s\x1b[0m" % majorMsg)
        # Set `result` to `False`
        result = False

    # return the result
    return result


# Get the user's age as `age`
age = getAge(minAge)
# Check the given `age` & display the corresponding message
checkAge(age)
