def cel_to_fahr(c):
    if (c < -273.15):
        return "Temperature to low"
    else:
        f = c * 9/5 + 32
        return f

print(cel_to_fahr(50))
print(cel_to_fahr(-300))
