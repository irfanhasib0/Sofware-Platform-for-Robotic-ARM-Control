import numpy as np
import cv2



def k_means(img1):
# convert to np.float32
  img=cv2.resize(img1,(80,60))
  Z = img.reshape((-1,3))
  Z = np.float32(Z)
  #cv2.imshow('',Z)
  # define criteria, number of clusters(K) and apply kmeans()
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
  K = 5
  ret,label,center=cv2.kmeans(Z,K,criteria,5,cv2.KMEANS_PP_CENTERS)

  # Now convert back into uint8, and make original image
  center = np.uint8(center)
  
  
   
  res = center[label.flatten()]
  res2 = res.reshape((img.shape))
  #for x,y in zip(center):
   # cv2.circle(img,(x,y), 10, (0,0,255),1)
  res3=cv2.resize(res2,(640,480))
  cv2.imshow('res2',res3)
  
  return res3
  
cv2.destroyAllWindows()
