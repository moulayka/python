# -*- coding: utf-8 -*-
"""
Created on Sun May 19 01:55:08 2024

@author: DELL
"""
def Pgcd (a,b):
    if a<b:
        c = a
        a = b
        b = c    
    r = a % b
    while r!=0:
        a = b
        b = r
        r =a % b
    return b
   
def Ppcm(a,b):
    return Pgcd(a,b)*a*b


d =int( input("donnez a: "))
e =int( input("donnez b: "))
print("Le PGCD (",d,",",e,")=",Pgcd(d,e)) 
print("Le PPCM (",d,",",e,")=",Ppcm(d,e)) 
