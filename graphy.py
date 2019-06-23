# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 00:44:20 2019

@author: gilld
"""
import languages
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

im = image.imread('python logo.png')
fig, ax = plt.subplots()
fig= plt.figure(figsize=(23,10))
data=languages.extract_languages()

skills={}
x_values=[]
performance=[]
for k,v in data.items():
    for skill in v:
        if skill not in skills:
            skills[skill]=1
        else:
            skills[skill]+=1
            
for k,v in skills.items():
     x_values.append(k)
     performance.append(v)
y_pos = np.arange(len(skills))

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, x_values)
plt.ylabel('Users')
plt.title('Programming language usage')

plt.savefig('Current usage.png')