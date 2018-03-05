import cv2
import numpy as np
#from matplotlib import pyplot as plt




nx=0
ny=0



def edge_corner(img,m_x,m_y,nx,ny):

    
    
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray1 = cv2.equalizeHist(gray)
    
    edges = cv2.Canny(gray1,100,255)
    
    
    gray = np.float32(gray)


    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst =cv2.dilate(dst,None)

    

    
    #ret, dst = cv2.threshold(dst,128,255,0)
    dst = np.uint8(dst)

    #lines = cv2.HoughLinesP(dst,1,np.pi/180,240,30,100)
    #for x1,y1,x2,y2 in lines[0]:
     #   cv2.line(dst,(x1,y1),(x2,y2),255,2)
    dst_c=dst.copy()
    N = cv2.moments(dst_c)
    if N['m00']>50000:
     nxt = int(N['m10']/N['m00'])
     nyt = int(N['m01']/N['m00'])
     cv2.circle(dst,(nxt,nyt),50,255,6)
    dst1=dst_c[m_y:m_y+50,m_x:m_x+50]
    try:N = cv2.moments(dst1)
    except:N=cv2.moments(dst_c)
    if N['m00']>50000:
     nx = int(N['m10']/N['m00'])+m_x
     ny = int(N['m01']/N['m00'])+m_y
     #cv2.circle(dst,(nx,ny),10,255,1)
    cv2.rectangle(dst, (nx,ny), (nx+60,ny+60), 255,6)
    cv2.rectangle(dst, (m_x,m_y), (m_x+60,m_y+60), 255,6)
    #dst1=dst[m_y:m_y+100,m_x:m_x+100]
    #track_window=m_x,m_y,w,h
    
   
    #cv2.rectangle(dst, (x,y), (x+w,y+h), 255,6)

    ed=cv2.resize(dst,(160,120))
    
    #cv2.imshow('subpixel5.png',dst)
    return nx,ny,ed,N['m00']
