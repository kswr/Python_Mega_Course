file = open('example.txt','w')
file.write("Line 1\n")
file.write("Line 2\n")
file.close()

file = open('example1.txt','w')
list = ["Line 1", "Line 2", "Line 3"]
for item in list:
    file.write(item+"\n")

file.close()
