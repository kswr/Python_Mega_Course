# both strings and listst are sequences of items

c = ["H", 4, "Hello"]
print(c)
c.append(4)
print(c)
c.remove("H")
print(c)
c.remove(4) # removes first occurence
print(c)
print(dir(c))
c.remove(c[2]) # remove third element

# "" - empty string
# [] - empty list
