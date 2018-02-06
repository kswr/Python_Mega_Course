file = open("example.txt",'r')
# as long as object exists, file is "open" in Python
content = file.read()
print(content)

# move pointer to beginning
file.seek(0)
contentList = file.readlines()
print(contentList)

# remove "\n"
contentList1 = [i.rstrip("\n") for i in contentList]
print(contentList1)

# close file, not exactly necessary when not working with ips
file.close()
