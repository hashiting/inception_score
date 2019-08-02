#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:31:47 2019

@author: lee
"""

import jsonlines
writer = jsonlines.open('comedy.jsonl',mode='a')
with open("url_list.jsonl", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        if len(item['genres']) > 0 and str(item['genres'][0]).find("comedy") >= 0 :
            #print(item)
            print(item['genres'][0])
            writer.write(item)

#import nltk
#from nltk.tokenize import word_tokenize
#import re
#
#
#def preprocess(text):
#    """
#    Preprocess text for encoder
#    """
#    X = []
#    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
#    for t in text:
#        sents = sent_detector.tokenize(t)
#        result = ''
#        for s in sents:
#            tokens = word_tokenize(s)
#            result += ' ' + ' '.join(tokens)
#        if result != "":
#            
#            X.append(result)
#    return X
#
#
#
#f = open('out_txts/5430__deadly-gamble-a-girl-and-her-dog-cozy-mystery.txt','r')
#x = preprocess(f)

#import pickle
#fr = open('romance_dictionary.pkl','rb')
#inf = pickle.load(fr)
#print(inf)       
#fr.close() 

#import numpy as np
#
#test=np.load('romance/Wemb.npy',encoding = "latin1")