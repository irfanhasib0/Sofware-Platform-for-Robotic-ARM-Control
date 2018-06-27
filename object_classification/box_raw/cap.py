import cv2
cap=cv2.VideoCapture(0)


i=0
while(1):
    ret,frame=cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out=cv2.resize(frame,(150,150))
    cv2.imshow('frame',out)
    
    k=cv2.waitKey(1)
    if(k==27):
        break
    if(k==97):
        name='box.'+str(i)+'.jpg'
        print(name)
        cv2.imwrite(name,out)
        i=i+1
cap.release()
cv2.destroyAllWindows()
