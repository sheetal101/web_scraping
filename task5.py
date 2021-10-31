import json
import requests
from task1 import scrape_top_list
from task4 import scrap_movie_details

top_movies = scrape_top_list()
movies_detail=top_movies
def get_movie_list_details():
    list_for_details=[]
    for i in movies_detail:
        for j in i:
            if "Url" in j:
                movie_url=scrap_movie_details(i["Url"])
                list_for_details.append(movie_url)
                # list_for_details.append(scrap_movie_details(i["Url"]))
    # print(list_for_details)
        # print(i["Url"])
    file=open("task5.json",'w+')
    json.dump(list_for_details, file, indent=4)

    return list_for_details
    
get_movie_list_details()
