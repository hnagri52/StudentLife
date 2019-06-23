# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 03:33:00 2019

@author: gilld
"""
import operator
import languages
def match_maker():
    data_all=languages.extract_languages()
    # i have a list of people
    my_data=["python","C","js","arduino","C++"]
    match_scores={}
    user_stats={}
    back=languages.backend_languages
    front=languages.frontend_languages
    front_count=0
    back_count=0
    length=len(my_data)
    
    data={}
    for k,v in data_all.items():
        if len(v)>0:
            #print("THis has an item!!");
            data[k]= v



    for x in my_data:
        x=x.lower()
        if x in front:
            front_count+=1
        elif x in back:
            back_count+=1
        else:
             print("please map "+x)
    my_front_percent=front_count /length*100
    my_back_percent=back_count /length*100
    
    for k,v in data.items():
        front_count=0
        back_count=0
        for x in v:
            if x in front:
                front_count+=1
            elif x in back:
                back_count+=1
            else:
                 print("please map "+x)
        
        front_percent=front_count /len(v)*100
        back_percent=back_count /len(v)*100 
        user_stats[k]=[front_percent,back_percent]
        
        
        
    for k,v in data.items(): 
        user=user_stats[k]
        for percent_match in range(100,0,-1): 
            if my_front_percent+user[0]>=percent_match and my_back_percent+user[1]>=percent_match:
                user_stats[k].append(percent_match)
                break
        gap=100-percent_match
        gap50=gap*.5
        score_per=gap50/length
        for language in v:
            if language in my_data:
                #lanaguage similarities can cover 50% of the gap
                user[2]+=score_per
        match_scores[k]=user[2]
    
    sorted_scores = sorted(match_scores.items(), key=operator.itemgetter(1))
    
    
    first=sorted_scores[-1]
    second=sorted_scores[-2]
    third=sorted_scores[-3]
    
    best_match=[first,second,third]
    
    message=""
    for user in best_match:
        message+=user[0]+" is your best match with a score of "+str(user[1])
        message+="\nTheir stats for frontend % backend % and match score respectively are "
        for x in user_stats[user[0]]:
            message+=str(x)+", "
        message+="and their skills are "
        for x in data[user[0]]:
            message+=x+" "
        message+="\n"
        
    print (message)
    return message