#!/usr/bin/env python

# -*- coding: utf-8 -*-

# 3/21/2020, Noah Cristino (https://github.com/noahcristino)

import os
import re
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
directories=["biorxiv_medrxiv","comm_use_subset", "noncomm_use_subset"]
papers=[]
for directory in directories: #loops thru 3 dataset directories
    print("processing directory: "+directory)
    path=directory+"/"+directory #json files are within dir/dir/*.json
    for jsonfile in tqdm(os.listdir(path)): #loop thru all json files
        jsoned = json.load(open(path+"/"+jsonfile)) #load into json obj
        title=jsoned['metadata']['title'] #store paper title
        try:
            author=jsoned['metadata']['authors'][0]['first']+" "+jsoned['metadata']['authors'][0]['last'] #store 1st author name
        except:
            author="" #empty if cannot find author
        papertext="" 
        for text in jsoned['body_text']: #body text is truncated into a list
            if "copyright" in text['text'] or "All rights reserved" in text['text']: #skip copyright and useless text
                continue
            else:
                papertext=papertext+text['text']+" "
        papers.append([title, author, papertext]) #add scrapped json data to array
pd.set_option('display.max_colwidth', None) #remove max columnwidth from pandas DataFrame
pandaframe = pd.DataFrame(papers, columns=['title','author','papertext']) #convert papers (array) -> pandaframe (DataFrame)
incubationtimes=[]
for idx,txt in enumerate(pandaframe['papertext']): #search through all papertext
    if "incubation" in txt: #looking for keyword 'incubation'
        resultframe=pandaframe.loc[[idx]] #if keyword found create result DataFrame
        for line in str(resultframe['papertext']).split(". "): #split papertext into sentences
            if "incubation" in line: #find all sentences with keyword
                times=re.findall(r'([0-9]+,*\.*[0-9]*) *-* *(?:days|day)', line) #search for time references in days within matched sentences (allows for weird punctuation found within some papers)
                for time in times: #loop thru matched times
                    incubationtimes.append(int(float(time))) #convert to ints and add to array (float then int to prevent invalid literal errors)
delidxs=[] #store an array of indices to remove
remcnt=0 
for idx,time in enumerate(incubationtimes): #loop thru incubation times
    if time > 24 or time < 2: #remove extreme data points
        delidxs.append(idx) #add index of extreme point to array
for index in delidxs: #loop thru indices to remove
    del incubationtimes[index-remcnt] #remove from array (remcnt variable accounts for incides shifting -1 once some are removed)
    remcnt=remcnt+1
y = np.array(incubationtimes) #array -> numpy array

plt.hist(y); #histogram plot
plt.grid(axis='y', alpha=0.75) 

plt.xlabel('Time (days)')

plt.ylabel('Frequency')

plt.title('Corona Virus Incubation Time')

plt.text(23, 45, r'avg: '+str(y.mean())) #display average

plt.axvline(y.mean(), color='k', linestyle='dashed', linewidth=1) #avg line
plt.show() #show plot
