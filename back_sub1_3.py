import numpy as np
import cv2
import time

#cap = cv2.VideoCapture(0)


#ret,frame = cap.read()
#prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
t_w=(0,0,640,480)
kernel = np.ones((5,5),np.uint8)
prev_x=0
prev_y=0
cx=0
cy=0
cm=0
cn=0
nx=0
ny=0
def bck(frame,prev_gray,cx,cy,nx,ny,m_x,m_y):
    #t1=time.time()
    
    #ret, frame = cap.read()
    
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    
    ret,thr = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    #contours,hierarchy = cv2.findContours(thr, 1, 2)

    #cnt = contours[0]
    #(x,y),radius = cv2.minEnclosingCircle(cnt)
    #center = (int(x),int(y))
    #radius = int(radius)
    #cv2.circle(thr,center,radius,255,2)


    fm1=np.subtract(gray,prev_gray)
    #cv2.imshow('new',thr)
    
    fm2= cv2.erode(fm1,kernel,1)
    
    fm= cv2.erode(fm2,kernel,1)
    prev_gray=gray




    M = cv2.moments(fm)

    if M['m00']>1000:
     cx = int(M['m10']/M['m00'])
     cy = int(M['m01']/M['m00'])
    #if M['m00']<100000:
    # cm = cx
    # cn = cy
    #thr2=thr.copy()
    thr1=thr[m_y:m_y+50,m_x:m_x+50]
    
    try:N = cv2.moments(thr1)
    except:N=cv2.moments(thr)
    if N['m00']>10000:
     nx = int(N['m10']/N['m00'])+m_x
     ny = int(N['m01']/N['m00'])+m_y
    #if N['m00']<100000:
     #nm = nx
     #nn = ny

    
    x=cx
    y=cy
    #tx=int(0.5*x+0.5*prev_x+0.1*(x-prev_x))
    #prev_x=tx
    #ty=int(0.5*y+0.5*prev_y+0.1*(y-prev_y))
    #prev_y=ty
    #cv2.rectangle(frame,(tx,ty),(tx+30,ty+30),255,3)
    
    cv2.rectangle(fm,(cx,cy),(cx+30,cy+30),255,3)
    cv2.rectangle(thr,(nx,ny),(nx+10,ny+10),255,1)
    #cv2.rectangle(thr,(m_x,m_y),(m_x+50,m_y+50),(nx+30,ny+30),255,1)
    

    #cv2.rectangle(frame,(nx,ny),(nx+30,ny+30),(0,0,255),3)
    #cv2.rectangle(fm,(cm,cn),(cm+30,cn+30),255,3)

    #cv2.imshow('frame',frame)
    #cv2.imshow('fm',thr)
    #k = cv2.waitKey(30) & 0xff
    #prev_gray=gray
    #if k == 27:
    #    break
    #t2=time.time()
    #print M['m00']
    #print cx,cy
    #print(t2-t1)
    return prev_gray,fm,thr,cx,cy,nx,ny,M['m00'],N['m00']


    
