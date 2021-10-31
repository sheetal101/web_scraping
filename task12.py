import json
from typing import Text
import requests
from bs4 import BeautifulSoup

movie_url='https://www.rottentomatoes.com/m/toy_story_4'
url=requests.get(movie_url)
a=BeautifulSoup(url.text,"html.parser")
 
def scrape_movie_cast(movie_url):
    url=requests.get(movie_url)
    a=BeautifulSoup(url.text,"html.parser")
    main=a.find("div",class_="castSection")
    main1=main.find_all("div",class_="media-body")
    actors_list=[]
    name_list=[]
    for i in main1:
        # d={}
        text=i.span.text
        get_name=text.strip()
        # d['Name']=get_name
        actors_list.append(get_name)
    with open ("task12.json", 'w') as task12_file:
        json.dump(actors_list, task12_file, indent=4)
        task12_file.close()   
    return actors_list
scrape_movie_cast(movie_url)


    

