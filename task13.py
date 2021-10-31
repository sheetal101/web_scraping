import json
from task4 import scrap_movie_details
from task12 import scrape_movie_cast

def movie_details_and_cast():
    task4=scrap_movie_details(Url='https://www.rottentomatoes.com/m/toy_story_4')
    data=task4
    task12=scrape_movie_cast(movie_url='https://www.rottentomatoes.com/m/toy_story_4')
    task_data=task12
    data["cast"]=task_data

    with open('Task13.json', 'w') as file:
        json.dump(data, file, indent=4)

movie_details_and_cast()
