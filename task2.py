from task1 import scrape_top_list
import json

def group_by_year():
    task1_data=open("task1.json", 'r')
    data=json.load(task1_data)
    dict={}
    for i in data:
        year_list=[]
        a=i['Year']
        if a not in dict:
            for j in data:
                if j['Year']==a:
                    year_list.append(j)
            dict[a]=year_list
            # print(dict)
    task2=open("task2.json", 'w')
    json.dump(dict, task2, indent=4)
    task2.close()
group_by_year()
