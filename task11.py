import json

task5_data=open("task5.json", 'r')
data=json.load(task5_data)

def analyse_movies_genre():
    genre_dic={}
    genre_list=[]
    genre=[]
    for movie in data:
        if 'Genre' in movie:
            gen=movie['Genre']
            genre.append(gen)
    for i in genre:
        for j in i:
            if j!='&':
                genre_list.append(j)
    new_genre_list=[]
    for i in genre_list:
        if ',' in i:
            a=i[:-1]
            new_genre_list.append(a)
    for index in new_genre_list:
        c=0
        for index_1 in new_genre_list:
            if index==index_1:
                c+=1
        if index not in genre_dic:
            genre_dic[index]=c
    
    with open ("task11.json", 'w') as task11_file:
        json.dump(genre_dic, task11_file, indent=4)
    task11_file.close()   

analyse_movies_genre()
