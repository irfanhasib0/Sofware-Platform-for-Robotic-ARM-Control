import cv2
import numpy as np




       


lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
lower_green = np.array([50,50,50])
upper_green = np.array([70,255,255])
def color_det(frame):
    

    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    hu=hsv[10,10,0]
    l = np.array([0,50,50])
    m = np.array([hu,50,50])
    h = np.array([255,50,50])
      
    #mask1 = cv2.inRange(hsv, l,m-10 )
    #mask2 = cv2.inRange(hsv, m+10, h)
    #mask = cv2.bitwise_and(mask1,mask1, mask= mask2)
    # define range of blue color in HSV
    #lower_blue = np.array([110,50,50])
    #upper_blue = np.array([130,255,255])
   

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    #res = cv2.bitwise_and(frame,frame, mask= mask2)

     # define range of blue color in HSV
    #lower_blue = np.array([0,50,50])
    #upper_blue = np.array([10,255,255])

    # Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    #res1 = cv2.bitwise_and(frame,frame, mask= mask)


    #cv2.imshow('frame',frame)
    #cv2.imshow('frame1',mask)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    #cv2.imshow('res1',res1)
    
    
     
    
    return mask,res
    
  
             


