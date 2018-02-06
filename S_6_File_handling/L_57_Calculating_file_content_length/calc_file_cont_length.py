file = open("fruits.txt",'r')
fruits = file.readlines()
fruits = [i.rstrip("\n") for i in fruits]
# print(fruits)
for i in fruits:
    print(len(i))
