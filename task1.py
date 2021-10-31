import bs4
import requests
from bs4 import BeautifulSoup
import json

link=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
                 
soup=BeautifulSoup(link.text, "html.parser")
def scrape_top_list():
    maindiv=soup.find('div',class_='container')
    tablebody=maindiv.find('div',class_='panel-body content_body allow-overflow')
    table=tablebody.find("table",class_="table")    
    table1=table.find_all("tr")
    ranking=0
    movie_list=[]
    for i in table1:
        find_table_data=i.find_all('td')
        e_dict={}
        for data in find_table_data:
            movie_name=i.find('a',class_="unstyled articleLink") ['href'][3:]
            year=i.find('a', class_="unstyled articleLink").text[-5:-1]
            Reviews=i.find('td', class_="right hidden-xs").get_text()
            Rating=i.find('span', class_="tMeterIcon tiny").get_text()[3:-2]
            url=("https://www.rottentomatoes.com/m/"+movie_name)
            e_dict['Movie']=movie_name
            e_dict['Year']=year
            e_dict['Reviews']=Reviews
            e_dict['Rating']=float(Rating)
            e_dict['Url']=url
            e_dict['Ranking']=ranking
        ranking=ranking+1
        for k in e_dict:
            if k!={}:
                if e_dict not in movie_list:
                    movie_list.append(e_dict)
            # else:
                # break
    # print(movie_list)
    file=open("task1.json",'w')
    json.dump(movie_list, file, indent=4)
    return movie_list
scrape_top_list()

