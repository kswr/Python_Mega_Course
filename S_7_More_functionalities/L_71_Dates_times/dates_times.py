import datetime # managing time objects
import time # delaying operations in Python

def create_file():
    """This function creates file with datestamp and empty string"""
    with open(now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", "w") as file:
        file.write("")

now = datetime.datetime.now() # grabs time from the computer

yesterday = datetime.datetime(2018,2,5,11,0,0,0)

print(now-yesterday)

print(type(now-yesterday))

delta = now-yesterday # timedelta object

print(delta.total_seconds())

# strftime ref http://strftime.org/
print(now.strftime("%Y-%m-%d-%H-%M-%S-%f"))
create_file()

# create timedelta for 2 days
days2 = datetime.timedelta(days=2)
print(now+days2)

# time
lst = [] # empty list

for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(1)

for i in lst:
    print(i)
