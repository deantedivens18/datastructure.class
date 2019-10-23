# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:22:12 2019

@author: DMDivens.2018
"""
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [12, 200, 45, 1, 57, 23]
selectionSort(alist)
print(alist)

