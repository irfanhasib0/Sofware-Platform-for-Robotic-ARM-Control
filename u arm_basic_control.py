import numpy as np
import cv2
from ser_w import *
from puma import *
from puma_mdl import *
import time




from joy_window_2 import *

    


ix=200
iy=300
m_x=0
m_y=0
event0=0
track=1
auto_track=0
move=1
clk_track=0


def mouse_tk(event,x,y,flags,param):
    global ix,iy,event0,m_x,m_y,track,move,clk_track
    event0=event
    
    
    m_x=x
    m_y=y
    if (event == cv2.EVENT_LBUTTONDOWN)and((m_x/32)<18)and((m_y/24)>=0)and((m_y/24)<=18):
        ix= x
        iy= y
    if ((event == cv2.EVENT_LBUTTONDOWN)and((m_x/32)>=18)and((m_y/24)<=1)):
        if track==1:
         track=0                                  
        elif track==0:
         track=1

    if ((event == cv2.EVENT_LBUTTONDOWN)and((m_x/32)>=18)and((m_y/24)>=18)):
        if move==1:
         move=0                                  
        elif move==0:
         move=1
    
    if ((event == cv2.EVENT_LBUTTONDOWN)and((m_x/32)>=18)and((m_y/24)>=8)and((m_y/24)<=10)):
        if clk_track==1:
         clk_track=0                                  
        elif clk_track==0:
         clk_track=1
        
        
      


frame=np.ones((480,640,3),np.uint8)

jx=100
jy=100
jz=90
prev_jx=300
prev_jy=200
def nothing(x):
    pass
cv2.namedWindow('irfan hasib1')
#cv2.namedWindow('frame')
cv2.createTrackbar('R','irfan hasib1',0,640,nothing)
cv2.createTrackbar('G','irfan hasib1',0,480,nothing)

g=1
x=250
y=250
w=100
h=100
t_win = (x,y,w,h)
term_crit1 = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
val_thr=40
cv2.setTrackbarPos('R','irfan hasib1',val_thr)
ratio=40
cv2.setTrackbarPos('G','irfan hasib1',ratio)
while(1):
    t1=time.time()
    jx=cv2.getTrackbarPos('R','irfan hasib1')
    jy=cv2.getTrackbarPos('G','irfan hasib1')
    
    window=np.ones((800,800,3),np.uint8)
    window=window*125
    ##color
    
    
    

    ##joy_window
##    jx,jy,jz,track,move,clk_track=joy_get(jx,jy,jz,track,move,clk_track,speed)
##    l=np.sqrt((jx-prev_jx)*(jx-prev_jx)+(jy-prev_jy)*(jy-prev_jy))
##   
##    jx=int(.5*jx+.5*prev_jx+.5*(jx-prev_jx))
##    jy=int(.5*jy+.5*prev_jy+.5*(jy-prev_jy))
##    prev_jx=jx
##    prev_jy=jy

    
        
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
  
    
    k = cv2.waitKey(6) & 0xff
    
    
    

    #if cm==1:
     # __ ,rame = cap.read()
    
    #image=rame.copy()
    ##contour
    #jx=jx+1
    #jy=jy+1
    time.sleep(.1)
    if jx<40:
        jx=40
    if jy<40:
        jy=40
    if jx>600:
        jx=600
    if jy>440:
        jy=440
    if jz>160:
        jz=160
    if jz<40:
        jz=40
    
    cv2.setMouseCallback('irfan hasib',mouse_tk)
    frame2=cv2.resize(frame,(640,480))
    
# Drawing grid        
    
    div=60
    for i in range(1,11):
           cv2.line(frame2, (div*i,0), (div*i,480), (255,0,0),1)
    for j in range(1,8):   
           cv2.line(frame2, (0,div*j), (640,div*j), (255,0,0),1)
    cv2.rectangle(frame2, (270,210), (330,270), (255,0,0),1)
    cv2.rectangle(frame2, (0,0), (640,480), (255,0,0),10)
    
    cv2.putText(frame2,'irfan hasib',(10,420), font,.5,(0,255,0),1)


#jpystic
##    cv2.line(frame2, (jx+30,0), (jx+30,480), (255,255,255),1)
##    cv2.line(frame2, (0,jy+30), (640,jy+30), (255,255,255),1)
##    cv2.putText(frame2,'Joystick..',(jx+60,jy+60), font,.5,(0,255,0),1)
##    cv2.rectangle(frame2, (jx,jy), (jx+60,jy+60), (255,255,255),2)
    

####mouse 
   
    cv2.putText(frame2,'X:%d'%(m_x/32+3),(m_x,m_y), font,.6,(0,255,0),1)
    cv2.putText(frame2,'Y:%d'%(m_y/24+3),(m_x,m_y+20), font,.6,(0,255,0),1)
    cv2.line(frame2, (m_x+30,0), (m_x+30,480), (0,120,0),1)
    cv2.line(frame2, (0,m_y+30), (640,m_y+30), (0,120,0),1)
### jx jy 
    cv2.putText(frame2,'X:%d'%(jx/32+3),(jx,jy), font,.6,(0,0,255),1)
    cv2.putText(frame2,'Y:%d'%(jy/24+3),(jx,jy+20), font,.6,(0,0,255),1)
    cv2.line(frame2, (jx+30,0), (jx+30,480), (0,120,255),1)
    cv2.line(frame2, (0,jy+30), (640,jy+30), (0,120,255),1)


    limit=np.sqrt((jx/32+3)*(jx/32+3)+(jy/24+3)*(jy/24+3))
### Ikine
    print jx,jy,limit
    if(limit<25):
     anga,angb,angc,angd=get_angle(jx/32,0,jy/24)
    
### Drawing puma
   
    
     wn=draw_puma(limit,anga,angb,angc)
###printing angles & pos    
    if anga>0:
     cv2.putText(window,'ang.a :%d'%int(anga),(640,40), font,.6,(0,255,0),1)
     cv2.putText(window,'ang.b :%d'%int(angb),(640,60), font,.6,(0,255,0),1)
     cv2.putText(window,'ang.c :%d'%int(angc),(640,80), font,.6,(0,255,0),1)
     cv2.putText(window,'ang.d :%d'%int(angd),(640,100), font,.6,(0,255,0),1)
     cv2.putText(window,'ang.z :%d'%int(jz),(640,120), font,.6,(0,255,0),1)
 
    cv2.putText(window,'jx :%d'%int(jx/32),(640,140), font,.6,(0,255,0),1)
    cv2.putText(window,'jx :%d'%int(jy/32),(640,160), font,.6,(0,255,0),1)
    
    t2=time.time()
    cv2.putText(window,'time :%d'%int(t2*1000-t1*1000),(640,180), font,.6,(0,255,0),1)
###Sendingle on serial    
    from serial import *
    cv2.rectangle(frame2, (600,440), (630,470), (0,0,255),-1)
    cv2.putText(frame2,'Arm activated...',(10,140), font,.6,(0,0,255),1)
    cv2.putText(frame2,'Move on...clk',(560,420), font,.4,(125,125,125),1)

               #serial_write(m_x/32+3,m_y/24+3)
    
    serial_write_ang(int(anga),int(angb),int(angc),int(-1*angd),int(jz))

            
    
### adding frame on window
    
    
    window[0:480, 0:640 ] = frame2
### adding draw model on window     

    window[520:640, 100:260,0 ] =0
    window[520:640, 100:260,1 ] =0
    window[520:640, 100:260,2 ] =0
    window[520:620, 360:560 ] =wn
### drawing small window    
    div=8
    for i in range(0,21):
           cv2.line(window, (100+div*i,640), (100+div*i,650), (255,0,0),1)
    for j in range(0,16):   
           cv2.line(window, (260,520+div*j), (270,520+div*j), (255,0,0),1)

    cv2.line(window, (jx/4+100,635), (jx/4+100,660), (0,0,255),1)
    cv2.putText(window,'X:%d'%jx,(jx/4+100,670), font,.6,(0,255,0),1)
    cv2.line(window, (255,jy/4+520), (280,jy/4+520), (0,0,255),1)
    
    cv2.putText(window,'Y:%d'%jy,(270,jy/4+520), font,.6,(0,255,0),1)
    cv2.rectangle(window, (90+jx/4,510+jy/4), (jx/4+110,jy/4+530), (125,125,125),2)
    

    cv2.imshow('irfan hasib',window)
    
    
     
    if k == 27:
       break
    
        

cv2.destroyAllWindows()



