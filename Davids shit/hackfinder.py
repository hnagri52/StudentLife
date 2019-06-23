# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 18:49:41 2019
hack finder


@author: gilld
"""

import json

def get_hacks():
    #adding my text file
   #name, link, startdate, enddate, location
    sources=["hacks raw text 2018.txt","hacks raw text 2019.txt"]
    hacks=[]
    for x in range (2):    
        
        wordfile=open(sources[x],"r")
        index=0
        done_event=0
        lines=wordfile.readlines()
        for my_line in lines:
            
            #extract event name
            index = my_line.find("title")
            if index != -1 : 
                startdex= index+7
                enddex= my_line.find('"',startdex)
                name=my_line[startdex:enddex]
                startdex=my_line.find('"',enddex+1)+1
                enddex=my_line.find('"',startdex)
                link=my_line[startdex:enddex]
                
            index = my_line.find("startDate")
            if index != -1 : 
                startdex= index+20
                enddex= my_line.find('"',startdex)
                startdate=my_line[startdex:enddex]
                
            index = my_line.find("event-logo")
            if index != -1 : 
                startdex= my_line.find('"',index)
                startdex= my_line.find('"',startdex+1)+1
                enddex= my_line.find('"',startdex+1)
                logo_link=my_line[startdex:enddex]
                
            index = my_line.find("endDate")
            if index != -1 : 
                startdex= index+18
                enddex= my_line.find('"',startdex)
                enddate=my_line[startdex:enddex]
            
            index = my_line.find("city")
            if index != -1 : 
                startdex= my_line.find('>',index)+1
                enddex= my_line.find('<',startdex)
                city=my_line[startdex:enddex]
                
            index = my_line.find("state")
            if index != -1 : 
                startdex= my_line.find('>',index)+1
                enddex= my_line.find('<',startdex)
                state=my_line[startdex:enddex]
                done_event=1
                
            if done_event:
                done_event=0
                hacks.append({"name":name, "start date": startdate, "end date":enddate, "city":city, "state":state, "link":link, "logo":logo_link})
            
        wordfile.close()
    data = {"data": hacks}
    print(data)
    return data

get_hacks()