import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.medium.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt(dt.now().year, dt.now().month, dt.now().day,
                                                               dt.now().hour) < dt(dt.now().year, dt.now().month,
                                                                                   dt.now().day, 16):
        print("Working hours")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("Fun hours")
    time.sleep(5)

# to schedule this to start at boot, use task scheduler on Windows, or cron on Mac/Linux
