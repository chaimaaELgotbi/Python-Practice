# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:37:12 2021

@author: Chaimaa
"""
import csv
import pandas as pd
import numpy as np
import json

f = open("donee.csv","r")

lecture = csv.reader(f,delimiter=";")

f= open ("Taille.json" , "w")


liste=[]
for i in lecture:
      temp={}
      temp["Poids"]=i[0]
      temp["Age"]=i[1]
      temp["Taille"]=i[2]
      liste.append(temp)
      print (temp)
json.dump(liste,f)
f.close()

     

    
    
