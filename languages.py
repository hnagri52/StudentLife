import json
import requests


data = None
data_store = []

user_info_raw = {}
user_info_sorted = {}

frontend_languages = ["html", "css", "js", "react.js", "angular", "django", "ruby", "php", "jquery","go"]
backend_languages = ["c", "c++", "c#", "java", "python", "swift", "android", "react-native", "node.js", "express.js", "sql", "nosql", "mongodb","arduino","mysql","objective-c","ml","ai","r","elixir"]

languages = ["java", "python", "c++", "c#", " c ", "go", "html", "css", "javascript", "node.js", "react-native", "react.js", "express.js", "sql", "arduino", "mysql", "nosql", "objective-c", "swift", "android", "ml", "ai", "ruby", "js", " r ", "elixir", "php", "mongodb", "jquery", "angular", "django"," c,",",c "," c/","/c "]


def extract_languages():
    with open("slack_scrapper/msg.json", "r") as f:
        data = json.load(f)
    
    
    for item in data["data"]:
        user_info_raw[item['user'] ] = item['text']
        user_info_sorted[item['user']] = None
    '''
    for key, value in user_info_raw.items():
        print("{0} is the key: and {1} is the value" .format(key, value))
           # print(item['user'])'''
    skip=0
    for k, v in user_info_raw.items():
        user_languages = []
        for language in languages:
            v = str(v)
            v = v.lower()
           # print(v.find(language))
    
            if v.find(language) != -1:
                #fixing c strings
                if language.find(" ")!= -1:
                    language= language.replace(" ", "")
                if language.find("/")!= -1:
                    language=language.replace("/","")
                if language.find(",")!= -1:                  
                     language=language.replace(",","")
                     
                     
                #fix javasrcipt+js  as well as.js  
                if language == "javascript":
                    language="js"
                if language=="js":
                    index=v.find(language)
                    if v[index-1]==".":
                        skip=1 #to avoid node.js etc
                
                if not skip:
                    user_languages.append(language)
                skip=0
        user_info_sorted[k] = user_languages
    
    '''
    for k,v in user_info_sorted.items():
        if len(v)>0:
            #print("THis has an item!!")
            print (k, v)
       # print("{0} is the key: and {1} is the value".format(k, v))
     '''  

    return {"data": user_info_sorted}
