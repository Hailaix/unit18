def print_upper_words(words, starts_with):
    """Prints all words in a list that start with any of the characters in the second list"""
    for word in words:
        for char in starts_with:
            if word.upper().startswith(char.upper()): #.upper used for case insenstivity
                print(word.upper())
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"])