from bs4 import BeautifulSoup
import requests
import json
from task1 import scrape_top_list


def scrap_movie_details(Url):
    Req = requests.get(Url)
    soup = BeautifulSoup(Req.text, 'html.parser')
    maindiv = soup.find_all('li', class_='meta-row clearfix')
    movie_name = soup.find('h1', class_="scoreboard__title").text

    d = {}
    d["Movie Name"] = movie_name
    d['Url'] = Url
    for i in maindiv:
        list_of_data = []
        a = i.text
        b = a.split()
        # print(b)
        if "Rating:" in b:
            d['Rating'] = (b[1])
        if "Genre:" in b:
            gen = (b[1::])
            d['Genre'] = gen
        if "Language:" in b:
            d['Language'] = [(b[-1])]
        if "Runtime:" in b:
            l=[]
            for my_var in b:
                if my_var != "Runtime:":
                    time=my_var.strip()[:-1]
                    l.append(int(time))
                for i in range(len(l)):
                    if i==0:
                        hrs=l[i]*60
                    elif i==1:
                        hrs=l[0]*60+l[i]
            d['Runtime']=hrs
        if "Producer:" in b:
            d["Producer"]=b[1:]
        if "Director:" in b:
            director_list=[]
            for director in b:
                if director!="Director:":
                    director_list.append(director)
            e=""
            for new in director_list:
                for dusra_variable in new:
                    if dusra_variable==" ":
                        continue
                    else:
                        e+=dusra_variable
                    sp=e.split(',')          
            d['Director']=sp
    with open ("task4.json", 'w') as task4_file:
        json.dump(d, task4_file, indent=4)
    task4_file.close()   

    return d
scrap_movie_details("https://www.rottentomatoes.com/m/coco_2017")
