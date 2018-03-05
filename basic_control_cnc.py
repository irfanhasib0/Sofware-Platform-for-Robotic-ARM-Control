import numpy as np
import cv2

#import pygame
from puma import *
from puma_mdl import *
import time
from joy_window_jst import *
from ser_w_class import serl





win=np.ones((800,800,3),np.uint8)




class r:
    global m_x,m_y,ex
    window=np.ones((800,800,3),np.uint8)
    w=30
    h=30
    tx=72
    ty=52
    row=160
    col=120
    cm=1


    frame=np.ones((480,640,3),np.uint8)
    frame1=np.ones((480,640,3),np.uint8)
    frame2=np.ones((480,640,3),np.uint8)
    roi=np.ones((30,30,3),np.uint8)

    #method=eval(methods[5])
    m=5
    prev_d0=0
    prev_d1=0
    dv=1
    all_show=1



    jx=300
    jy=200
    jz=90
    track=0
    move=0
    clk_track=0
    prev_jx=300
    prev_jy=200
    speed=4
    #m_x=0
    #m_y=0
    ix=200
    iy=300
    m_x=0
    m_y=0
    event=0
    track=1
    auto_track=0
    move=1
    clk_track=0

    
    
    t3=0
    sx=10
    sy=10
    cx=0
    cy=0
    nx=0
    ny=0
    prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f=1
    ex=0
    ey=0
    t=0
    

    g=1
    x=250
    y=250
    w=100
    h=100
    t_win = (x,y,w,h)
  
    def __init__(self):
        
        
        
        r.window=np.ones((800,800,3),np.uint8)
        r.window=r.window*125
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        k = cv2.waitKey(6) & 0xff
        #cv2.setMouseCallback('tk',r.mouse_tk)
        r.frame1=r.frame.copy()
        
        
        ##joy_window######################
        r.t1=time.time()
        jt=jst()
        r.t2=time.time()
        r.t3=r.t2-r.t1
        
      
        ##################################


        

        
        
        
             
        
         
        
        
        
        
        
    #######draw frame
        
        r.frame2=cv2.resize(r.frame,(640,480))
        if r.dv==1:    
            div=60
            for i in range(1,11):
               cv2.line(r.frame2, (div*i,0), (div*i,480), (255,0,0),1)
            for j in range(1,8):   
               cv2.line(r.frame2, (0,div*j), (640,div*j), (255,0,0),1)
            cv2.rectangle(r.frame2, (270,210), (330,270), (255,0,0),1)
            cv2.rectangle(r.frame2, (0,0), (640,480), (255,0,0),10)
        cv2.putText(r.frame2,'irfan hasib',(10,420), font,.5,(0,255,0),1)
        cv2.putText(r.frame2,'%d'%int(1000*(r.t2-r.t1)),(10,180), font,.6,(0,0,255),1)

    #######joystic
        cv2.line(r.frame2, (jt.jx+30,0), (jt.jx+30,480), (255,255,255),1)
        cv2.line(r.frame2, (0,jt.jy+30), (640,jt.jy+30), (255,255,255),1)
        cv2.putText(r.frame2,'Joystick..',(jt.jx+60,jt.jy+60), font,.5,(0,255,0),1)
        cv2.rectangle(r.frame2, (jt.jx,jt.jy), (jt.jx+60,jt.jy+60), (255,255,255),2)
        
    ####mouse 
       
        cv2.putText(r.frame2,'X:%d'%(m_x/32+3),(m_x,m_y), font,.6,(0,255,0),1)
        cv2.putText(r.frame2,'Y:%d'%(m_y/24+3),(m_x,m_y+20), font,.6,(0,255,0),1)
        cv2.line(r.frame2, (m_x+30,0), (m_x+30,480), (0,120,0),1)
        cv2.line(r.frame2, (0,m_y+30), (640,m_y+30), (0,120,0),1)
        


        r.t4=time.time()

    ####put data 
        r.anga,r.angb,r.angc,r.angd=get_angle(jt.jx/32,0,jt.jy/24)
        if r.anga>0:
         cv2.putText(r.window,'ang.a :%d'%int(r.anga),(640,40), font,.6,(0,255,0),1)
         cv2.putText(r.window,'ang.b :%d'%int(r.angb),(640,60), font,.6,(0,255,0),1)
         cv2.putText(r.window,'ang.c :%d'%int(r.angc),(640,80), font,.6,(0,255,0),1)
         cv2.putText(r.window,'ang.d :%d'%int(r.angd),(640,100), font,.6,(0,255,0),1)
         cv2.putText(r.window,'ang.z :%d'%int(r.jz),(640,120), font,.6,(0,255,0),1)
         r.limit=np.sqrt((r.jx/32+3)*(r.jx/32+3)+(r.jy/24+3)*(r.jy/24+3))
         r.wn=draw_puma(r.limit,r.anga,r.angb,r.angc)
        cv2.putText(r.window,'jx :%d'%int(jt.jx),(640,140), font,.6,(0,255,0),1)
        cv2.putText(r.window,'jx :%d'%int(jt.jy),(640,160), font,.6,(0,255,0),1)
        
        r.t5=time.time()
        cv2.putText(r.window,'time :%d'%int(r.t5*1000-r.t4*1000),(640,180), font,.6,(0,255,0),1)
        r.sx=jt.jx/32+3
        r.sy=jt.jy/24+3
        sr=serl(int(97),int(jt.jx/10),int(jt.jy/10),int(jt.jx/10),int(jt.jx/10))
              

        if (r.move==1):
            #if r.g==0:
                #from ser_w import *
                
            
            
            cv2.rectangle(r.frame2, (600,440), (630,470), (0,0,255),-1)
            cv2.putText(r.frame2,'Arm activated...',(10,140), font,.6,(0,0,255),1)
            cv2.putText(r.frame2,'Move on...clk',(560,420), font,.4,(125,125,125),1)

                   #serial_write(m_x/32+3,m_y/24+3)
           
            
          
                            
                
                   
            #time.sleep(1)       
            cv2.putText(r.frame2,'Arm activated...',(10,140), font,.6,(0,0,255),1)
            cv2.putText(r.frame2,'Move on...deflt',(560,420), font,.4,(125,125,125),1)
                
        if r.move==0:
                cv2.putText(r.frame2,'Arm deactivated...',(10,140), font,.6,(0,0,255),1)
                cv2.putText(r.frame2,'connect serial...',(560,420), font,.4,(0,0,255),1)
        

        
        
        r.window[0:480, 0:640 ] = r.frame2
        
        
        #window[50:170, 690:850 ] =roi1
        
        
        r.window[520:640, 100:260,0 ] =0
        r.window[520:640, 100:260,1 ] =0
        r.window[520:640, 100:260,2 ] =0
        r.window[520:620, 360:560 ] =r.wn
        
        div=8
        for i in range(0,21):
               cv2.line(r.window, (100+div*i,640), (100+div*i,650), (255,0,0),1)
        for j in range(0,16):   
               cv2.line(r.window, (260,520+div*j), (270,520+div*j), (255,0,0),1)
        #cv2.putText(r.window,'joystic mapping:%d'%int(r.l),(90,510), font,.5,(255,0,0),1)
        cv2.putText(r.window,'t:%d'%int(r.t),(250,510), font,.5,(255,0,0),1)
        cv2.line(r.window, (jt.jx/4+100,635), (jt.jx/4+100,660), (0,0,255),1)
        cv2.putText(r.window,'X:%d'%r.jx,(jt.jx/4+100,670), font,.6,(0,255,0),1)
        cv2.line(r.window, (255,jt.jy/4+520), (280,jt.jy/4+520), (0,0,255),1)
        
        cv2.putText(r.window,'Y:%d'%jt.jy,(270,jt.jy/4+520), font,.6,(0,255,0),1)
        cv2.rectangle(r.window, (90+jt.jx/4,510+r.jy/4), (jt.jx/4+110,jt.jy/4+530), (125,125,125),2)
        #cv2.imshow('irfan hasib',r.window)
        
        
        
        
        if ex == 1:
           return
##m_x=0
##m_y=0
##ex=0
def motion(event):
  global m_x ,m_y,ex
  m_x=event.x
  m_y=event.y
  return
def key1(event):
    print 345345
def key2(event):
    print("open")
def func(event):
   global ex
   #tkMessageBox.showinfo( "Hello Python", "Hello World")
   ex^=1
   
  
    


#rm=Frame(root,height="800",width="800",bg="#888")
#rm.pack()
rm1=Frame(root,height="800",width="800",bg="#888")
rm1.pack()
lmain = tk.Label(root)
lmain.place(x=0,y=0)
run=Button(root,text ="stop",bg="#555",fg="#fff",height="2",width="4")
run.place(x=600, y=440)
run.bind('<Button-1>', func)
def show_frame():
    global ex
    t=time.time()
    global m_x ,m_y
    r1=r()
    lmain.bind('<Motion>',motion)
    lmain.bind('<1>',key1)
    lmain.bind('<2>',key2)
    r1.m_x,r1.m_y=m_x,m_y
    if ex == 0:
      
       frame = r1.window
       cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
       img = Image.fromarray(cv2image)
       imgtk = ImageTk.PhotoImage(image=img)
       lmain.imgtk = imgtk
       #print time.time()-t
        #print r1.m_x, r1.m_y
       lmain.configure(image=imgtk)
       #lmain.after(30, show_frame)

    
while(1):
    show_frame()
    root.update()
    
    
       


#show_frame()       
#root.mainloop()
cv2.destroyAllWindows()
cap.release()
pygame.quit ()

