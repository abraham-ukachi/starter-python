##############################
# Name: Job23 - Aller plus loin 1
# Script: job23.py
# Author: Abraham Ukachi <abraham.ukachi@laplateforme.io>
# version: 0.0.1 (alpha)
#
# Usage:
#   1-|>  python3 job23.py
#
#   2-|>  import job23 as j23
#    -|>
#    -|>  word = "think"
#    -|>  modWord = j23.getModifiedWord(word)
#    -|>  print(modWord)
#     |
#    =|o-> "thkin"
#
##############################
# IMPORTANT: This code is a work in progress and subject to major changes until version 0.1
##############################

#========== Job 23 ===============
#     >>> DESCRIPTION <<<
#~~~~~~~~~ (French) ~~~~~~~~~~~~~~
#
# - Créer un programme job23.py qui demandera à l’utilisateur de renseigner un mot \
#   et un seul, sans espace ni aucun autre caractère que les 26 lettres de \
#   l’alphabet (sans accent ni majuscule).
# - Votre programme devra modifier ce mot, en y changeant de place certains caractères \
#   (ou tous) afin de donner un mot plus “loin” dans l’ordre alphabétique que le mot \
#   renseigné par l'utilisateur.
# 
# - Attention:
#   Le nouveau mot doit être le mot le plus proche possible, dans l’ordre alphabétique, \
#   du mot original ! Par exemple, “abcde” donnerait “abced”. “acedb” est aussi “valide” \
#   mais n’est PAS le plus proche du mot original dans l’ordre alphabétique.
#
#~~~~~~~~~~ (English) ~~~~~~~~~~~~
# ??? TODO: Add english translation ???
#=================================

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MOTTO: I'll always do more 😜!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# Importing modules...
import re # <- python's built-in RegEx module
import itertools # <- python's buit-in iteration tool / module


# Let's define some constants, shall we? ;)

# - Error Message constants
ERR_MSG_ONE_WORD = "one_word"
ERR_MSG_NO_SPACE = "no_space"
ERR_MSG_ONLY_ALPHA = "only_alpha"
# - Prompt Sign constants
PROMPT_SIGN_DEFAULT = "\x1b[1m\x1b[34mI\x1b[0m " # <- (bold + blue)
PROMPT_SIGN_IN = "\x1b[1m\x1b[32m>>\x1b[0m " # <- (bold + green)
PROMPT_SIGN_OUT = "\x1b[1m\x1b[34m<<\x1b[0m " # <- (bold + blue)
PROMPT_SIGN_ERR = "\x1b[1m\x1b[31m<<\x1b[0m " # <- (bold + red)
# - Log messages constants
LOG_MSG_WELCOME = "welcome"
LOG_MSG_WORD = "word"
LOG_MSG_MOD_WORD = "mod_word"
# - Other constants
LANG = "en" # <- default language set to "english", duh!

# Initialize the `errorMsg` object/dict with english (EN) and french (FR)
errorMsg = { "en" : {}, "fr": {} } # <- hhmmm, so tempting to import some `json` here ;-)
errorMsg["en"][ERR_MSG_ONE_WORD] = "Only 1 word is allowed"
errorMsg["en"][ERR_MSG_NO_SPACE] = "Spaces are not allowed"
errorMsg["en"][ERR_MSG_ONLY_ALPHA] = "Only lowercased alphabets (a-z) are allowed"

# TODO: Add error messages in "fr" (French)

# Initialize the `logMsg` object too
logMsg = { "en": {}, "fr": {} }
logMsg["en"][LOG_MSG_WELCOME] = "Welcome to Job{}"
logMsg["en"][LOG_MSG_WORD] = "Enter a word:"
logMsg["en"][LOG_MSG_MOD_WORD] = "Your new word is \x1b[1m\x1b[32m%s\x1b[0m"

# TODO: Add log messages in "fr" (French)



# Defining private & public functions...

# ========== PRIVATE FUNCTIONS

def _showWelcomeMessage(msg, job = 23):
    """
    Displays a welcome message for the current job

    :param { str } msg: the message to be displayed
    :param { int } job: the job number
     """
    print("\x1b[2m") # <- everything should be in gray color
    print("=" * 33) # <- top/open style
    print("# \t  ✺◟(•‿•)◞✺" + "\t\t#")
    print("# \t" + msg.format(job) + "\t#")
    print("=" * 33) # <- bottom/close style
    print("\x1b[0m") # <- stop coloring



# Define the `_isOneWord` function
def _isOneWord(txt):
    """
    Returns True if the given `txt` is one word
     
    @private
    :param { str } txt
    :return { bool } isOneWord
    """
    
    # Do nothing if the given `txt` is empty
    if len(txt.strip()) == 0:
        return False # IDEA: return False instead ?
    
    # Initialize `isOneWord` variable to False
    isOneWord = False
     
    # Split the words using regular expressions 
    # and whitespace characters as matches or separators
    splitWords = re.findall('\w+', txt) # <- ANOTHER_WAY: txt.split(" ")
    # ^^^^^^^^^ `\w`: matches any word character (equivalent to [a-zA-Z0-9_])
    #            `+`: matches the previous token between one and unlimited times, 
    #                 as many times as possible, giving back as needed (greedy)
    
    # If the length of the `splitWords` is exactly equal to 1...
    if len(splitWords) == 1:
        # ...set `isOneWord` to True
        isOneWord = True
    
    # return the value of `isOneWord`
    return isOneWord
    

# Define the `_hasNoSpace` function
def _hasNoSpace(txt):
    """
    Returns True if the given `txt` has no space

    @private
    :param { str } txt
    :return { bool } hasNoSpace
    """

    # Initialize the `hasNoSpace` variable
    hasNoSpace = False
    
    # Looking for spaces in `txt`...

    # Find all available spaces in `txt` using the `re` RegEx module
    foundSpaces = re.findall('\s', txt)

    # If no spaces were found...
    if len(foundSpaces) == 0:
        # ...set `hasNoSpce` to True
        hasNoSpace = True

    # return the current value of `hasNoSpace`
    return hasNoSpace




# Define the `_onlyAlphaChars` function 
# NOTE: We could have probably only used this function for this assignment,
# But, I wanted to point out specific errors or rules and handle them seperately.
def _onlyAlphaChars(txt):
    """
    Returns True if the given `txt` contains 
    only characters between `a` and `z` (case sensitive)

    :param { str } txt
    :return { bool } onlyAlphaChars
    """
    
    # Initialize the `onlyAlphaChars` variable
    # Set `onlyAlphaChars` to False
    onlyAlphaChars = False

    # Define the regular expression variable as `regex`
    regex = '^[a-z]+$'
    # ^^^^^ `^`: asserts position at the start of the string
    #       `[a-z]+`: match the characters between `a` and `z` 
    #                (ie. lowercased & without special characters)
    #       `$`: asserts position at the end of the string
    
    
    # Using `regex`...
    # If the characters in `txt` match characters between `a` and `z`..
    if re.match(regex, txt):
        # ...set `onlyAlphaChars` to True
        onlyAlphaChars = True
    
    # return the current value of `onlyAlphaChars`
    return onlyAlphaChars
        

# Define the `_printSortedCombos` function
def _printSortedCombos(sortedCombos, word = "", wordLimit = 5, delay = 0.1):
    """
    Prints out the given `sortedCombos`.
    NOTE: This function is used for debugging purposes

    :param { list } sortedCombos
    :param { str } word
    :param { int } wordLimit
    :param { float } delay
    """
    
    # get the total number of words in the list
    total = len(sortedCombos)
    # calculate the number of lines to be printed 
    # based on the given `wordLimit` and `total`
    lines = int(total / wordLimit)
    
    # initialize the `currentIndex` variable
    currentIndex = 0

    # set the `wordHighlighted` variable to False
    wordHighlighted = False

    
    # For each line...
    for line in range(lines):
        # ...calculate the start index
        startIndex = line * wordLimit
        # calculate the end index
        endIndex = currentIndex + wordLimit
        
        # slice the `sortedCombos` list with `startIndex` and `endIndex`
        slicedList = sortedCombos[startIndex:endIndex]

        # stringify or join the list with '|' as `txt`
        txt = "|".join(slicedList)

        # if there's a word, found in `txt`, and it hasn't been highlighted yet...
        if len(word) > 0 and word in txt and wordHighlighted == False:
            # ...highlight the word
            txt = txt.replace(word, "\x1b[0m\x1b[36m{}\x1b[0m\x1b[2m".format(word))
            # inform this loop that we've highlighted the word already by setting
            # `wordHighlighted` to True
            wordHighlighted = True
        
        # print the sliced list, gray and enclosed in '|'
        print("\x1b[2m|{}|\x1b[0m".format(txt))
        
        # update the current index
        currentIndex = endIndex
    

# ======== END OF PRIVATE FUNCTION 



# ========== PUBLIC FUNCTIONS

# Define the `isValid` function
def isValid(txt):
    """
    Returns True if the given `txt` is just one word without spaces, 
    special & uppercase characters; only the 26 alphabets between [a] and [z]
    
    :param { str } txt
    :return { bool } result
    """

    # Intialiaze the `result` variable by setting it to False
    result = False

    # if `txt` is one word, has no space and contains only lowercased alphabets...
    if _isOneWord(txt) and _hasNoSpace(txt) and _onlyAlphaChars(txt):
        # ...set the result to True
        result = True

    # Return the `result`
    return result;


# Define the `getModifiedWord` funtion
# TODO: Rename `getModifiedWord()` to `getModWord()` or `getNewWord()`
def getModifiedWord(word):
    """
    This function generates all posible combinations to the given `word` alphabetically,
    and returns the closest permutation to the given `word`.
    
    :param { str } word
    :return { str } modifiedWord
    """
        
    # Initialize the `modifiedWord` variable
    modifiedWord = ""
    
    # Get a list of all permutations of `word`,
    # using the permutation() function in the `itertools` module we imported
    permutations = list(itertools.permutations(word))
    # neatly join each permutation into a `combos` list
    combos = [''.join(permutation) for permutation in permutations]
    # sort the `combos` alphabetically
    sortedCombos = sorted(combos)

    # DEBUG: print out `sortedCombos`
    _printSortedCombos(sortedCombos, word)

    # get the current location of `word` in the `sortedCombos` list
    wordIndex = sortedCombos.index(word)
    
    # get the closest word index
    closestWordIndex = wordIndex + 1
    
    # If there's no word after the original `word`...
    if (wordIndex >= len(sortedCombos)):
        # ...use the index before the `word` as the closest
        closestWordIndex = wordIndex - 1
    
    # Update the `modifiedWord` with the word at the closest word index in `sortedCombos`
    modifiedWord = sortedCombos[closestWordIndex]
    
    ###### TODO: Remove this code snippet later - maybe ? ########
    # Convert `word` to a list and assign it to a variable `li`
    # li = list(word) # <- ie. "mango" will return => ['m', 'a', 'n', 'g', 'o']
    # Get the total number of characters as `totalChar`
    # totalChar = len(li) - 1 # <- we do not want to swap the last character.
    #
    # For each character's index/position in the list `li` (say, 'm' at 0)...
    #for i in range(0, totalChar): 
    #    # ...for each index or from a range 
    #    # of 0..to..the total number of characters in `oldWord`
    #    for j in range(0, totalChar):
    #        # if the character at index 0 (say, 'm') 
    #        # is alphabetically lower than the character at index 2 (say, 'n')...
    #        if li[i] < li[j]:
    #            # swap their values (ie. 'm' to index 2 & 'n' to index 0) 
    #            li[i], li[j] = li[j], li[i]
    #  
    #        
    # Update the `modifiedWord`:
    # - join all the characters in the list `li` together,
    # - and assign the value to `modifiedWord`
    # modifiedWord = modifiedWord.join(li)
    ############## END CODE SNIPPET ########################

    # return the modified word
    return modifiedWord



# ===== END OF PUBLIC FUNCTIONS =========


# Define our main function
def main():
    """
    The main function of `Job23` - Aller plus loin
    """
    # First, create a welcome message
    welcomeMsg = logMsg[LANG][LOG_MSG_WELCOME]
    # Show the welcome message
    _showWelcomeMessage(welcomeMsg)
    
    # Print out our first message
    print(PROMPT_SIGN_DEFAULT + logMsg[LANG][LOG_MSG_WORD] + " \x1b[2m[a-z]\x1b[0m")
    # Now, get a word or text from the user
    word = input(PROMPT_SIGN_IN)
    
    # If the word is valid...
    if isValid(word):
        # ...get the modified word as `modWord`
        modWord = getModifiedWord(word)
        # Tell the world about this modified word :)
        print("\n" + PROMPT_SIGN_OUT + logMsg[LANG][LOG_MSG_MOD_WORD] % modWord)
    elif _isOneWord(word) == False:
        # TODO: add a comment here
        print("\n" + PROMPT_SIGN_ERR + errorMsg[LANG][ERR_MSG_ONE_WORD])
    elif _hasNoSpace(word) == False:
        # TODO: add a comment here
        print("\n" + PROMPT_SIGN_ERR + errorMsg[LANG][ERR_MSG_NO_SPACE])
    else:
        # `_onlyAlphaChars()` is False
        print("\n" + PROMPT_SIGN_ERR + errorMsg[LANG][ERR_MSG_ONLY_ALPHA])





# If `job23.py` is being run directly...
if __name__ == "__main__":
    # ...call our main function
    main()
else:
    # `job23.py` is being imported into another module")
    # do something else here
    pass

