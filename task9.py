import json
import time
import random

task5_data=open("task5.json", 'r')
data=json.load(task5_data)


for i in data:
    random_seconds=random.randint(1,3)
    path=open('/home/dell31/Documents/WebScraping/task9.text'+i["Movie Name"]+'text','w')
    file=path.write(str(i))
    time.sleep(random_seconds)
    path.close()

    