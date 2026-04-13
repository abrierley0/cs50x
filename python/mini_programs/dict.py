# SPELLCHECKER IN PYTHON

# Make words a mathematical set
words = set()

# Make words lowercase and check if in words
def check(word):
    return word.lower() in words

# Load dictionary
def load(dictionary):
    with open(dictionary) as file:
        words.update(file.read().splitlines())
    return True

# Size of the list of words
def size():
    return len(words)

# Python handles memory and unloading for you
def unload():
    return True