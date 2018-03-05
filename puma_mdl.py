import cv2
import numpy as np
#import matplotlib as plt
import time

from puma import *

a=0
b=0
c=0
x=0
y=0
z=0
i=0
win1=np.ones((180,200,3),np.uint8)
win2=np.ones((180),np.uint8)
#cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
pa=0
pb=0
p=0
def draw_puma(x,a,b,c):
  
    win=np.ones((480,640,3),np.uint8)
    
   
   
    
    a=np.deg2rad(a)
    b=np.deg2rad(b)
    c=np.deg2rad(c)
    #b=(np.pi-b)
    b=-b
    
    cv2.line(win,(0,0),(0+valc(a)+valc(b+a),0+vals(a)+vals(b+a)), (0,255,0),1)
   
    cv2.line(win,(0,0),(0+valc(a),0+vals(a)), (255,0,0),6)
    cv2.line(win,(0+valc(a),0+vals(a)),(0+valc(a)+valc(b+a),0+vals(a)+vals(b+a)), (0,0,255),6)
    cv2.line(win,(0,0),(0+valc(c),0+vals(c)), (0,255,0),2)
    #cv2.line(win1,(x-5,pa),(x,int(np.rad2deg(a))), (0,0,255),1)
    #cv2.line(win1,(x-5,pb),(x,int(np.rad2deg(b))), (255,0,0),1)
    #win2[x]=int(np.rad2deg(a))
    
    #pa=int(np.rad2deg(a))
    #pb=int(np.rad2deg(b))
    win1=win[0:100,0:200]
    wn=np.flipud(win1)
    
    
    
    #cv2.rectangle(win, (100,100), (400,400), (0,0,255),2)
     
    return wn
    
    

    
