# [20/3] Runtime Errors

# every error that is not a syntax error is an exception

a = 1
b = "2"
print(int(2.5))
# print(a + b) - runtime error, TypeError
print(a + float(b ))
print(str(a) + b)
# print(c) - NameError: name 'c' is not defined
c = 3
print(c)
# print(c/0) - ZeroDivisionError: division by zero
