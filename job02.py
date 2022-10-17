##############################
# Script: job02.py
# Author: Abraham Ukachi <abraham.ukachi@laplateforme.io>
# version: 0.0.1 (alpha)
#
# Usage:
#   1- python3 job02.py
##############################


#========== Job 02 ===============
#
#~~~~~~~~~ (French) ~~~~~~~~~~~~~~
# - Créez un script job02.py qui dans un premier temps va afficher \
# “Bonjour, comment t’appelles tu ? ”
# - L’utilisateur devra ensuite entrer son prénom.
# - Déclarez une variable prenom, qui prendra la valeur saisie par l’utilisateur.
# - A l’aide d’une fonction system, “Bonjour prenom” (prenom étant la valeur de la variable
# du même nom)
#
#~~~~~~~~~~ (English) ~~~~~~~~~~~~
# ??? 
#=================================

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MOTTO: I'll always do more 😜!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# Create a welcome message
welcomeMessage = "Bonjour, comment t'appelles tu ? "

# Let's greet the user with our `welcomeMessage`, shall we?

# Define a variable `firstname`(ie. prenom) 
# and assign the user's input / answer to `welcomeMessage`
firstname = input(welcomeMessage)

# Print the word "Bonjour" followed by his/her `firstname` 
# in yellow, and using the % operator 
print("Bonjour \x1b[33m%s\x1b[0m" % firstname)
