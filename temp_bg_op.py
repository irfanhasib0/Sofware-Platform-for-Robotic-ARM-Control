import numpy as np
import cv2
ix=0
iy=0
event0=0

def mouse(event,x,y,flags,param):
    global ix,iy,event0
    event0=event
    if event == cv2.EVENT_LBUTTONDOWN:
        ix= x
        iy= y
        



a=0
b=0
w=60
h=60
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
#ret ,frame = cap.read()
#prev_roi = frame[b:b+h, a:a+w]
roi_bc=np.ones((10,10),np.uint8)
roi_bc=roi_bc*127
method=eval(methods[5])
F1=cv2.FONT_HERSHEY_COMPLEX
def new(frame,val):
    
    #cv2.setMouseCallback('img2',mouse)
    fm=frame.copy()
    
    
    roi_bc=cv2.resize(frame,(10,10))
    
  
    frame=cv2.resize(frame,(160,120))
    res = cv2.matchTemplate(frame,roi_bc,method)
    m,n,d,c=cv2.minMaxLoc(res)
    #cv2.imshow('res_back',res)
    
    frame1=frame.copy()
    nn=np.ones((120,160,3),np.uint8)
    #k = cv2.waitKey(6) & 0xff
    res1=res*200
    res1=cv2.resize(res1,(160,120))
    nn[:,:,0]=res1
    nn[:,:,1]=res1
    nn[:,:,2]=res1
    
    
    gray = cv2.cvtColor(nn, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.equalizeHist(gray)
    
    
    ret,thr = cv2.threshold(gray,val,255,cv2.THRESH_BINARY)
    thr1=thr.copy()
    
    cnt, hierarchy = cv2.findContours(thr1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    thr=cv2.resize(thr,(640,480))
    thr2=thr.copy()
    cnt_t, hierarchy = cv2.findContours(thr2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    #cv2.imshow('frame',fm)
    #cv2.waitKey(1)
    
    

    
    #new = cv2.bitwise_and(frame,frame, mask= thr)
    #cv2.imshow('thr',thr)
    #cv2.waitKey(1)

    
            
    

    return nn,cnt,cnt_t

    
        

        

