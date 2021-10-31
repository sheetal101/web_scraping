import json 
file=open("task1.json",'r')
movies=json.load(file)
def group_by_year():
    dic={}
    for i in movies:
        movies_list=[]
        year=i["Year"]
        if year not in dic:
            for j in movies:
                if year==j["Year"]:
                    movies_list.append(j)
            dic[year]=movies_list
    return dic    
group_by_year()
dec=group_by_year()
def group_by_decade(movies): 
    moviesdec={}
    list1=[]
    for i in movies:
        a=int(i)
        mod=a%10
        decade=a-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for j in list1:
        moviesdec[j]=[]
    for k in moviesdec:  
        dec10=k+9
        for x in movies:
            if int(x)<=dec10 and int(x)>=k:
                for v in movies[x]:
                    moviesdec[k].append(v)
                
    with open("task3.json","w+")as file2:
        json.dump(moviesdec,file2,indent=6)
        c=json.dumps(moviesdec)
        # print(c)
group_by_decade(dec)
