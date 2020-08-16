# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:02:17 2019

@author: jrbrad
"""

import matplotlib.pyplot as plt

f = open('mnistEg.txt','r')
pixels = f.readlines()
f.close()

""" Clean and convert Data """
for i in range(len(pixels)):
    pixels[i] = pixels[i].strip()
    pixels[i] = pixels[i].split(',')
    pixels[i] = [int(pixels[i][j]) for j in range(len(pixels[i]))]

plt.imshow(pixels, cmap='gray')        
plt.show() 