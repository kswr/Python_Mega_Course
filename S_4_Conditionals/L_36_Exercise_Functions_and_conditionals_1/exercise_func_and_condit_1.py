# [36/4] Exercise Functions and Conditionals 1


def string_length(mystring):
    if (type(mystring) == int):
        return "Sorry, integers don't have length"
    elif (type(mystring) == float):
        return "Sorry, floats don't have length"
    else:
        return len(mystring)

print(string_length("Hello"))
print(string_length(5))
print(string_length(10.0))
