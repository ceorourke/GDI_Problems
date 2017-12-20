class Dictionary(object):
    """A dictionary object."""

    def __init__(self):
        self._dictionary = set()

    def add_word(self, word):
        """Add item to dictionary"""

        self._dictionary.add(word)

    def does_word_exist(self, word):
        """Returns whether a word is in the dictionary"""

        if word in self._dictionary:
            return True
        return False

a_dict = Dictionary()
print a_dict.does_word_exist('pudding')
a_dict.add_word('pudding')
print a_dict.does_word_exist('pudding')

# TBH I didn't quite understand this question, not sure if I
# solved it correctly. Seems odd that a dictionary would just
# be a list of words (with no definitions) but the question
# didn't mention anything about definitions or where to put them