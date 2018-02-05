planet = input("What planet are you from? ")

print(planet)

def currency_converter(rate, euros):
    dollars = float(rate) * float(euros)
    return dollars

r = input("Input rate: ")
e = input("Input euros: ")

print(currency_converter(r,e))
