# Functions - Advanced features [27/4]

# functions can use default arguments, which need to be passed in definition after the non-default arguments

def minutes_to_hours(seconds, minutes=70):
    hours = minutes/60 + seconds / 3600
    return hours

print(minutes_to_hours(300))

# functions can generate an output or execute procedure, and return NoneType
