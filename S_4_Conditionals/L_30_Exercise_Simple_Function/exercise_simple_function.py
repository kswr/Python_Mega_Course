# Exercise - Simple function [30/4]

def celc_to_fahr(celcius):
    fahrenheit = celcius * 9/5 + 32
    return fahrenheit

print(celc_to_fahr(100))
print(celc_to_fahr(10))

def length(string):
    len = string.__len__()
    return len

print(length("Hello world"))

print(len("Hello world"))
