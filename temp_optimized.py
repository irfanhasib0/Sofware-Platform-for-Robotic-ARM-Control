
#roi copy
#pid
#color matching
import numpy as np
import cv2
from ser_w import *
from back_sub1_3 import *
from blue_detect_2 import *
from puma import *
from puma_mdl import *
from edge_lib import *
from k_mn import *
from temp_bg_op import *

import time




from joy_window import *
pygame.joystick.init()
    


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
        
        
      
cap = cv2.VideoCapture(1)





w=30
h=30
tx=72
ty=52
row=160
col=120
ret ,frame = cap.read()

roi = frame[ty:ty+h, tx:tx+w]
template =  cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
F1=cv2.FONT_HERSHEY_COMPLEX
F2=cv2.FONT_HERSHEY_COMPLEX_SMALL
F3=cv2.FONT_HERSHEY_DUPLEX
F4=cv2.FONT_HERSHEY_PLAIN
F5=cv2.FONT_HERSHEY_SCRIPT_COMPLEX
F6=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
F7=cv2.FONT_HERSHEY_SIMPLEX
F7=cv2.FONT_HERSHEY_TRIPLEX
F8=cv2.FONT_ITALIC

method=eval(methods[5])
m=5
prev_d0=0
prev_d1=0
dv=1
all_show=1



jx=300
jy=200
prev_jx=300
prev_jy=200
t3=0
sx=10
sy=10
cx=0
cy=0
nx=0
ny=0
prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
f=1
speed=4
ex=0
ey=0
t=0
def nothing(x):
    pass
cv2.namedWindow('irfan hasib1')
#cv2.namedWindow('frame')
cv2.createTrackbar('R','irfan hasib1',0,100,nothing)
cv2.createTrackbar('G','irfan hasib1',0,10,nothing)

g=1
x=250
y=250
w=100
h=100
t_win = (x,y,w,h)
term_crit1 = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
val_thr=20
cv2.setTrackbarPos('R','irfan hasib1',val_thr)
ratio=8
cv2.setTrackbarPos('G','irfan hasib1',ratio)
while(1):
    val_thr=cv2.getTrackbarPos('R','irfan hasib1')
    ratio=cv2.getTrackbarPos('G','irfan hasib1')
    
    window=np.ones((800,1200,3),np.uint8)
    window=window*125
    ##color
    mask,res=color_det(frame)
    
    
    t1=time.time()
    ##joy_window
    jx,jy,track,move,clk_track=joy_get(jx,jy,track,move,clk_track,speed)
    l=np.sqrt((jx-prev_jx)*(jx-prev_jx)+(jy-prev_jy)*(jy-prev_jy))
   
    jx=int(.5*jx+.5*prev_jx+.5*(jx-prev_jx))
    jy=int(.5*jy+.5*prev_jy+.5*(jy-prev_jy))
    prev_jx=jx
    prev_jy=jy
    t2=time.time()
    
        
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
  

    k = cv2.waitKey(6) & 0xff
    
    
    __ ,rame = cap.read()
    image=rame.copy()
    ##contour
    res_cnt,cnt,cnt_t=new(rame,val_thr)
    
    rr=cv2.resize(res_cnt,(640,480))
    r=float(ratio*0.10)
    
    rame=cv2.addWeighted(rr,r,rame,1-r,0)
    prev_gray,fm,thr,cx,cy,nx,ny,fmm,thrm=bck(rame,prev_gray,cx,cy,nx,ny,jx,jy)
    
    if jx<40:
        jx=40
    if jy<40:
        jy=40
    if jx>600:
        jx=600
    if jy>440:
        jy=440
    frame=cv2.resize(image,(160,120))
    ex,ey,ed,em=edge_corner(rame,jx,jy,ex,ey)
    t_win=jx,jy,100,100    
    ed_m=cv2.resize(ed,(640,480))
    #ed_m=cv2.resize(rr,(640,480))
    cv2.imshow('kjhkh',rr[:,:,0])
    ret, t_win = cv2.CamShift(rr[:,:,0], t_win, term_crit1)

    
    cam_x,cam_y,cam_w,cam_h=t_win
    #cam_w=100
    #cam_h=100
    
    
    
    

   
    cv2.setMouseCallback('irfan hasib',mouse_tk)
    frame1=frame.copy()
    
    if event0==1:
      tx=ix/4
      ty=iy/4
      prev_d0=ix/4
      prev_d1=iy/4
      #ret ,frame = cap.read()
      roi = frame1[ty:ty+h, tx:tx+w]
      if f==0:
        f=1
      elif f==1:
        f=0
      template =  cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    elif f==1 and t==10 :
      roi = frame1[cam_y/4:cam_y/4+30, cam_x/4:cam_x/4+30]
      #roi[:,:,0] = cv2.equalizeHist(roi[:,:,0])
      #roi[:,:,1] = cv2.equalizeHist(roi[:,:,1])
      #roi[:,:,2] = cv2.equalizeHist(roi[:,:,2])
      
      
    roi_n=cv2.resize((roi),(120,120))
    cv2.rectangle(roi_n,(0,0),(120,120),(255,0,0),6)
    try:window[560:680, 960:1080 ] =roi_n
    except:0
      
    if l>0:
        t=0
    if l==0 and t<100:
        t=t+1
    
    if track==0:
    
      tx=jx/4
      ty=jy/4
      prev_d0=jx/4
      prev_d1=jy/4
      #ret ,frame = cap.read()
      roi = frame1[ty:ty+h, tx:tx+w]
      template =  cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
     

    if k==97:#a
      w=60
      h=60
      tx=290
      ty=210
      #ret ,frame = cap.read()
      roi = frame1[ty:ty+h, tx:tx+w]
      template =  cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
      cv2.rectangle(frame, (270,210), (330,270), (255,255,0),3)
      

    
    

    
    frame2=cv2.resize(frame,(640,480))


    mx=0
    for cn in cnt_t:
      N = cv2.moments(cn)
      if N['m00']>100 and N['m00']<160000:
         nx = int(N['m10']/N['m00'])
         ny = int(N['m01']/N['m00'])
         #x1,y1,w1,h1 = cv2.boundingRect(cn)
         #cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)
         if N['m00']>mx:
             xx=nx
             yy=ny
             mx=N['m00']
             cnt_mx=cn
         x1,y1,w1,h1 = cv2.boundingRect(cn)
         cv2.rectangle(frame2,(x1,y1),(x1+w1,y1+h1),(0,225,225),2)
    #cv2.drawContours(frame2, cnt_t, -1, (0,255,0), 1)




    
    if track==1:
        
       res = cv2.matchTemplate(frame,roi,method)
       p,n,d,c=cv2.minMaxLoc(res)
       d0=int(0.5*d[0]+0.5*prev_d0+0.1*(prev_d0-d[0]))
       d1=int(0.5*d[1]+0.5*prev_d1+0.1*(prev_d1-d[1]))
       cv2.putText(window,'Object tracking:%d'%int(p*1000),(800,540), font,.6,(0,255,0),1)
       res1=cv2.resize(res,(160,120))
       window[560:680, 800:960,0 ] =res1*250
       window[560:680, 800:960,1 ] =res1*250
       window[560:680, 800:960,2 ] =res1*250
       prev_d0=d[0]
       prev_d1=d[1]
       #cv2.imshow('roi',roi)   
       #cv2.imshow('res',res)
       
       if m==5:
         tx=d0
         ty=d1
       elif m==4:
         tx=d0
         ty=d1
       else: 
         tx=c[0]
         ty=c[1]
    
       tx=(tx/4)*4
       ty=(ty/4)*4
       tx_n=tx/8+3
       ty_n=ty/6+3
       cv2.rectangle(frame2, (tx*4,ty*4), (tx*4+120,ty*4+120), (0,0,255),2)
       cv2.putText(frame2,'Target found...',(tx*4+60,ty*4+60), font,.6,(0,255,0),1)
       cv2.line(frame2, (tx*4+60,0), (tx*4+60,480), (0,0,255),1)
       cv2.line(frame2, (0,ty*4+60), (640,ty*4+60), (0,0,255),1)
       cv2.putText(frame2,'Obj_tracking.....',(10,120), font,.6,(0,0,255),1)
       cv2.rectangle(frame2, (600,10), (630,40), (0,0,255),1)
       cv2.putText(frame2,'Track on',(580,60), font,.4,(0,0,255),1)
    

  
         
            
       
    
    


    #lines = cv2.HoughLinesP(prev_gray,1,np.pi/180,100,300,100)
    #for x1,y1,x2,y2 in lines[0]:
     #   cv2.line(frame2,(x1,y1),(x2,y2),(0,255,0),2)
    
    if dv==1:    
        div=60
        for i in range(1,11):
           cv2.line(frame2, (div*i,0), (div*i,480), (255,0,0),1)
        for j in range(1,8):   
           cv2.line(frame2, (0,div*j), (640,div*j), (255,0,0),1)
        cv2.rectangle(frame2, (270,210), (330,270), (255,0,0),1)
        cv2.rectangle(frame2, (0,0), (640,480), (255,0,0),10)
    
    cv2.putText(frame2,'irfan hasib',(10,420), font,.5,(0,255,0),1)
    cv2.putText(frame2,'%d'%int(1000*(t2-t1)),(10,180), font,.6,(0,0,255),1)
    cv2.putText(frame2,'%d'%int(1000*t3),(10,200), font,.6,(0,0,255),1)
#jpystic
    cv2.line(frame2, (jx+30,0), (jx+30,480), (255,255,255),1)
    cv2.line(frame2, (0,jy+30), (640,jy+30), (255,255,255),1)
    cv2.putText(frame2,'Joystick..',(jx+60,jy+60), font,.5,(0,255,0),1)
    cv2.rectangle(frame2, (jx,jy), (jx+60,jy+60), (255,255,255),2)
    
##
    cv2.putText(frame2,'X:%d'%tx_n,(10,40), font,.6,(0,0,255),1)
    cv2.putText(frame2,'Y:%d'%ty_n,(10,60), font,.6,(0,0,255),1)
    cv2.putText(frame2,'X:%d'%(m_x/32+3),(m_x,m_y), font,.6,(0,255,0),1)
    cv2.putText(frame2,'Y:%d'%(m_y/24+3),(m_x,m_y+20), font,.6,(0,255,0),1)


    cv2.drawContours(res_cnt, cnt, -1, (0,0,255), 2)


    
    
    
##mouse    
    cv2.line(frame2, (m_x+30,0), (m_x+30,480), (0,120,0),1)
    cv2.line(frame2, (0,m_y+30), (640,m_y+30), (0,120,0),1)


    if clk_track==1:
               cv2.putText(frame2,'Click tracking on...',(10,160), font,.6,(0,0,255),1)
               cv2.putText(frame2,'clk_track on...',(580,220), font,.4,(125,125,125),1)
               cv2.line(frame2, (ix+30,0), (ix+30,480), (125,255,125),3)
               cv2.line(frame2, (0,iy+30), (640,iy+30), (125,255,125),3)
               cv2.rectangle(frame2, (ix,iy), (ix+60,iy+60), (255,255,255),2)
               cv2.rectangle(frame2, (600,220), (630,250), (0,0,255),2)
   
    t4=time.time()
    anga,angb,angc,angd=get_angle(jy/32+3,0,jx/24+3)
    
    
    
    
    if anga>0:
     cv2.putText(window,'ang.a :%d'%int(anga),(740,40), font,.6,(0,255,0),1)
     cv2.putText(window,'ang.b :%d'%int(angb),(740,60), font,.6,(0,255,0),1)
     cv2.putText(window,'ang.c :%d'%int(angc),(740,80), font,.6,(0,255,0),1)
     limit=np.sqrt((jx/32+3)*(jx/32+3)+(jy/24+3)*(jy/24+3))
     wn=draw_puma(limit,anga,angb,angc)
    cv2.putText(window,'jx :%d'%int(jx/32+3),(740,100), font,.6,(0,255,0),1)
    cv2.putText(window,'jx :%d'%int(jy/32+3),(740,120), font,.6,(0,255,0),1)
    
    t5=time.time()
    cv2.putText(window,'time :%d'%int(t5*1000-t4*1000),(740,140), font,.6,(0,255,0),1)

    if (move==1):
        
        
        cv2.rectangle(frame2, (600,440), (630,470), (0,0,255),1)
        if g==0:
            
            from ser_w import *
        if g==1:
            if g==1 and clk_track==1:
               anga,angb,angc,angd=get_angle(ix/32+3,0,iy/24+3)
               
               sx=ix/32+3
               sy=iy/24+3
               cv2.putText(frame2,'Arm activated...',(10,140), font,.6,(0,0,255),1)
               cv2.putText(frame2,'Move on...clk',(560,420), font,.4,(125,125,125),1)
           
            elif g==1 and auto_track==1:
               anga,angb,angc,angd=get_angle(tx_n/32+3,0,ty_n/24+3)
               
               sx=ix/32+3
               sy=iy/24+3
               cv2.putText(frame2,'Arm activated...',(10,140), font,.6,(0,0,255),1)
               cv2.putText(frame2,'Move on...trck',(560,420), font,.4,(125,125,125),1)
            
               
      
            elif g==1 and track==1 and clk_track==0 and auto_track==0:
               cv2.putText(frame2,'Arm activated...',(10,140), font,.6,(0,0,255),1)
               cv2.putText(frame2,'Move on...clk',(560,420), font,.4,(125,125,125),1)

               #serial_write(m_x/32+3,m_y/24+3)
               sx=jx/32+3
               sy=jy/24+3
               if anga>0:
                 serial_write_ang(int(anga),int(angb),int(angc),0,0)
               
               
               cv2.putText(frame2,'Arm activated...',(10,140), font,.6,(0,0,255),1)
               cv2.putText(frame2,'Move on...deflt',(560,420), font,.4,(125,125,125),1)
            
        if g==0:
            cv2.putText(frame2,'Arm deactivated...',(10,140), font,.6,(0,0,255),1)
            cv2.putText(frame2,'connect serial...',(560,420), font,.4,(0,0,255),1)
    

    #frame2[:,:,0]=frame2[:,:,0]
    #frame2[:,:,1]=frame2[:,:,2]
    #frame2[:,:,2]=frame2[:,:,2]
    
    window[0:480, 0:640 ] = frame2
    roi1=cv2.resize(roi,(160,120))
    fm1=cv2.resize(fm,(160,120))
    thr1=cv2.resize(thr,(160,120))
    
    #window[50:170, 690:850 ] =roi1
    cv2.putText(window,'Edge density:%d'%int(em),(750,180), font,.6,(0,255,0),1)
    window[200:320, 800:960,0 ] =ed
    window[200:320, 800:960,1 ] =ed
    window[200:320, 800:960,2 ] =ed
    eh=0
    ew=0
    #cv2.line(window, (ex,0), (ex,480), (0,255,125),1)
    #cv2.line(window, (0,ey), (640,ey), (0,255,125),1)
    cv2.line(window, (0,0), (ex-eh,ey-ew), (0,255,0),1)
    cv2.line(window, (640,0), (ex+eh,ey-eh), (0,255,0),1)
    cv2.line(window, (640,480), (ex+eh,ey+ew), (0,255,0),1)
    cv2.line(window, (0,480), (ex-eh,ey+ew), (0,255,0),1)
    cv2.circle(window,(ex,ey), 20, (0,255,0), 1)
    cv2.rectangle(window, (cam_x,cam_y), (cam_x+cam_h,cam_y+cam_w), (0,0,0),2)
    cv2.line(window, (0,0), (cam_x,cam_y), (0,0,0),1)
    cv2.line(window, (640,0), (cam_x+cam_h,cam_y), (0,0,0),1)
    cv2.line(window, (640,480), (cam_x+cam_h,cam_y+cam_w), (0,0,0),1)
    cv2.line(window, (0,480), (cam_x,cam_y+cam_w), (0,0,0),1)
    

    
    cv2.putText(window,'Object density:%d'%int(thrm),(750,380), font,.6,(0,255,0),1)
    res_cnt=cv2.resize(res_cnt,(160,120))
    window[400:520, 800:960] =res_cnt



    cv2.putText(window,'MOvement tracking:%d'%int(fmm),(600,500), font,.6,(0,255,0),1)
    window[520:640, 600:760,0 ] =fm1
    window[520:640, 600:760,1 ] =fm1
    window[520:640, 600:760,2 ] =fm1
    
    window[520:640, 100:260,0 ] =0
    window[520:640, 100:260,1 ] =0
    window[520:640, 100:260,2 ] =0
    window[520:620, 360:560 ] =wn
    
    div=8
    for i in range(0,21):
           cv2.line(window, (100+div*i,640), (100+div*i,650), (255,0,0),1)
    for j in range(0,16):   
           cv2.line(window, (260,520+div*j), (270,520+div*j), (255,0,0),1)
    cv2.putText(window,'joystic mapping:%d'%int(l),(90,510), font,.5,(255,0,0),1)
    cv2.putText(window,'t:%d'%int(t),(250,510), font,.5,(255,0,0),1)
    cv2.line(window, (jx/4+100,635), (jx/4+100,660), (0,0,255),1)
    cv2.putText(window,'X:%d'%jx,(jx/4+100,670), font,.6,(0,255,0),1)
    cv2.line(window, (255,jy/4+520), (280,jy/4+520), (0,0,255),1)
    
    cv2.putText(window,'Y:%d'%jy,(270,jy/4+520), font,.6,(0,255,0),1)
    cv2.rectangle(window, (90+jx/4,510+jy/4), (jx/4+110,jy/4+530), (125,125,125),2)
    #window[170:261, 850:981,0 ] =res
    #window[170:261, 850:981,1 ] =res
    #window[170:261, 850:981,2 ] =res
    

    cv2.imshow('irfan hasib',window)
    
    #cv2.imshow('fr',thr)
    
    
    
    
    #fm =  cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    
    #cv2.imshow('fft',img_s)
    
       #serial_write(ix/32,iy/24)
    t3=time.time()
    t3=t3-t1
    if k == 27:
       break
    
        

cv2.destroyAllWindows()
cap.release()
pygame.quit ()

