# [23/3] Exception handling in Python

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError: # always specify type of error exception
        return ("You are dividing by zero")
    except TypeError:
        return ("Wrong data type")

print(divide(2,0))
print("End of the program")
