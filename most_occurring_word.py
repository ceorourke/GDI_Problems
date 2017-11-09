def most_common_word(phrase):
    """Returns the word(or words) which occur most often"""

    counts = {}
    most = 0
    phrase = strip_punctuation(phrase)
    for word in phrase.split():
        counts[word] = counts.get(word, 0) + 1
        if counts[word] > most:
            most = counts[word]

    results = [word for word in counts if counts[word] == most]

    return results

def strip_punctuation(phrase):
    """Helper function that strips punctuation from phrase"""

    punctuation = {'?','.',',','!','(', ')', '{', '}'} # anything else you want
    new_phrase = ""
    for letter in phrase:
        if letter not in punctuation:
            new_phrase += letter

    return new_phrase

#################################TEST CASES####################################

phrase = "How much wood would a wood chuck chuck \
          if a wood chuck could chuck wood?"

print most_common_word(phrase) #=> ["wood", "chuck"]

phrase = "cat cat cat cat dog"

print most_common_word(phrase) #=> ["cat"]

phrase = "how, much? wood! wood, chuck? chuck."
print most_common_word(phrase) #=> ["wood", "chuck"]