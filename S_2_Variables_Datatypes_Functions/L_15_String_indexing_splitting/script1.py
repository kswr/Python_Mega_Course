c = "here"
# index from 0, splitting from first to less than last element
# splitting can reach non existing elements (on positive and negative ranges)
# can't call single element out of range
print(c[0]) # H
print(c[-0]) # H
print(c[-1]) # e
print(c[8]) # error
print(c[0:1]) # H
print(c[0:2]) # He
print(c[0:]) # Here
print(c[:3]) # Her
print(c[-100:-1]) # Her - won't get last char
print(c[-100:]) # Here
print(c[-100:0]) # Empty
print(c[-100:8]) # Here - only from positive indexing
