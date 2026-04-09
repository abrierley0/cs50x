# SPELLCHECKER IN PYTHON

# Demonstrates readability, fewer lines of code, more functionality built-in to Python
# But, uses more R.A.M and is slower and you lose control of the memory
# Harder to make mistakes with Python
# Switching to object-oriented languages

# Make words a set - mathematical definition, no duplicates
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