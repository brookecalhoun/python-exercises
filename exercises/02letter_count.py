# Write a function called `letter_count` to count the letter
# occurrence in a string. Use a dictionary.
#
# You can iterate over a string one letter at a time using
# a for loop.
#
# for letter in "alpha":
#   put the letter in our dictionary
#       # Do I already have the letter in the dictionary?
#           # update count of that letter by 1
#       # Or is it the first time I'm adding it to the dictionary
#           # add to dictionary with value 1
#           dd = {
#               'a' : 2
#               'l' : 1
#               'p' : 1
#               'h' : 1
#               }
# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.
#
# dd = {}
#
# dd["foo"] = 1
# dd["foo"] += 1
# if "foo" in dd:
#   print(dd["foo"])
#
# Careful. Python requires that you insert a key into a dictionary
# before you try to modify it's value. If you try to access a dictionary
# at a key that hasn't been added you'll get an error and the program will
# crash. Remember to use an if statement to see if a key is "in" a dictionary
# before you try to read it!
#
# d2 = {}
# d2["foo"]
# > KeyError: 'foo'
#
# Example function call:
#
# letter_count('banana')
#
# > {'a': 3, 'b': 1, 'n': 2}

def letter_count(word):
    unique_letters = {}

    for letter in word:
        # Do I already have the letter in the dictionary?
        if letter in unique_letters:
            # Update the count at that letter, increase it by 1
            unique_letters[letter] += 1
        # Or is it the first time i'm adding it to the dictionary?
        else:
            # add it to the dictionary with the value 1
            unique_letters[letter] = 1

    return unique_letters
    
print(letter_count('banana'))

