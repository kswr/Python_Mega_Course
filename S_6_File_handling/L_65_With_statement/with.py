# for quick opening and closing use 'with' statement, after with code block, .close() is not necessary

with open("example.txt",'w') as file:
    file.write("Line 1\n")


