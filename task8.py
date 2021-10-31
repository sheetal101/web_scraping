from typing import Text
import requests
import os
from task1 import scrape_top_list

task1=scrape_top_list()
data=task1[:10]


for i in data:
    print(i['Movie'])
    text_path='/home/dell31/Documents/WebScraping/movies.text'+i["Movie"]+'text'
    if os.path.exists(text_path):
        pass
    else:
        file=open('/home/dell31/Documents/WebScraping/movies.text'+i["Movie"]+'text', 'w')
        # file=open(text_path, 'w')
        get_data=requests.get(i["Url"])
        a=file.write(get_data.text)
        file.close()
        