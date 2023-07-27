# Spell Checker

This Java program implements a spell checker using a hash table. The `SpellChecker` class accepts a dictionary file in its constructor, parses the file, and stores the words in a `HashSet` for later reference. The object then uses this dictionary to check for spelling errors in a specified input file.

## SpellChecker Class

### Constructor

* `public SpellChecker(String filename)`: This constructor takes in the filename of the dictionary and initializes the spell checker. It reads the dictionary file, converts each word to lowercase, and removes all punctuation before inserting the words into the `HashSet`. The `filename` parameter is the name of the dictionary file containing a list of valid words.

### Methods

* `public List<String> getIncorrectWords(String filename)`: This method reads an input file, processes it into words, converts the words to lowercase, and removes all punctuation. It then compares each word with the words in the dictionary `HashSet`. Any word that is not found in the dictionary is considered an incorrect word and is added to the output list. The method returns a list of all incorrect words found in the input file.

* `public Set<String> getSuggestions(String word)`: This method takes an incorrectly spelled word as input and generates a set of potential suggestions for the misspelled word. The method implements three spell-checking techniques:
    1. Add one character: Adds a character at every position in the word, including the beginning and end.
    2. Remove one character: Removes one character at a time from each position in the word.
    3. Swap adjacent characters: Swaps every pair of adjacent characters in the word.
   The method returns a `Set` of all possible suggestions obtained from each of these techniques.

Enjoy spell-checking with the Spell Checker program!
