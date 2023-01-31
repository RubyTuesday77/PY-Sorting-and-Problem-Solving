#4: Write an algorithm that takes in a string and sorts the words in the string in alphabetical order. The comparison should be case-insensitive.
    #Sample input: 'I love software engineering'
    #Sample output: ['engineering', 'I', 'love', 'software']
    #Note that a key parameter will need to be used here in order for the sorting to be case-insensitive (sort in alphabetical order regardless of whether string is uppercase or lowercase).

string = 'I love software engineering'
sorted_words = sorted(string.split(), key = str.lower)

print(sorted_words)