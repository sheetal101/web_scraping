import json


task5_data=open("task5.json", 'r')
data=json.load(task5_data)

def analyse_movies_directors():
    dic={}
    l=[]
    new_list=[]
    for i in data:
        if "Director" in i:
            var=i['Director']
            l.append(var)
    for i in l:
        for j in i:
            new_list.append(j) 
    for d1 in new_list:
        c=0
        for d2 in new_list:
            if d1==d2:
                c+=1
        if d1 not in dic:
            dic[d1]=c
    print(dic)

    with open ("task7.json", 'w') as task7_file:
        json.dump(dic, task7_file, indent=4)
    task7_file.close()   


analyse_movies_directors()