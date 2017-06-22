# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:20:14 2017

@author: abensaad
"""

def setcoords():
    L=[]
    print("saisissez les coordonnées: absisse et ordonnées séparée par un espace, deux points séparés par une virgule")
    ch=input()
   L=ch.split(',')
   for i in range (len(L)):
        L[i]=L[i].split(' ')
    geo_json_geometry["coordinates"]=[L]
    
def settime():
   print("Saisissez la date de début: format aaa-mm-jjThh:mm:ss.000Z")
   ch=input()   
