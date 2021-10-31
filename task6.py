import json

task5_data=open("task5.json", 'r')
data=json.load(task5_data)
# print(data)

def analyse_movies_language():
    l=[]
    dic={}
    l1=[]
    for i in data:
        if 'Language' in i:
            var=i['Language']
            l.append(var)
    for i in l:
        for j in i:
            l1.append(j)
    for lang in l1:
        c=0
        for lang1 in l1:
            if lang==lang1:
                c+=1
        if "(" in lang and ")"  in lang:
            a=lang[1:-1]
            if a not in dic:
                dic[a]=c
        else:
            if lang not in dic:
                if lang!='language' and lang!='Kingdom)':
                    dic[lang]=c       
    # print(dic)
    
    with open ("task6.json", 'w') as task6_file:
        json.dump(dic, task6_file, indent=4)
    task6_file.close()   
    
analyse_movies_language()
