def reverse_string(astring):
    """Recursively reverse a string"""

    if len(astring) == 1:
        return astring

    return astring[-1] + reverse_string(astring[:-1])

astring = "IlovebigO" #=> "ObigevolI"
print reverse_string(astring)
astring = "yoblleH" #=> "Hellboy"
print reverse_string(astring)