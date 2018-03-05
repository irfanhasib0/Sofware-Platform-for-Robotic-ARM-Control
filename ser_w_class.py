import serial
import time
g=1
s=1
ser = serial.Serial('COM10', 9600, timeout=0)
#except:g=0
time.sleep(2)


##class ser_w:
##  x=0
##  y=0
##  z=0
##  m=0
##  n=0
##  try:ser = serial.Serial('COM23', 9600, timeout=0)
##  except:g=0
##  #def __init__(self):
##     
##      #ser_w.serial_write_ang(self)
class serl:
    def __init__(self,x,y,z,m,n):
        self.x=x
        self.y=y
        self.z=z
        self.m=m
        self.n=n
        serl.serial_write_ang(self)
        
    def donothing():
        pass
    def serial_write_ang(self):
        s=1
        #try:ser.flushInput()
        #except:0
        #try:ser.flushOutput()
        #except:0
        #x = eval(raw_input("Enter X coordinate: "))
        #y = eval(raw_input("Enter Y coordinate: "))
            
        #if ser.read()=='a':
        try:ser.write(chr(self.x))
        except:return
        #if ser.read()=='b':
        try:ser.write(chr(self.y))
        except:return
        try:ser.write(chr(self.z))
        except:return
        try:ser.write(chr(self.m))
        except:return
        try: ser.write(chr(self.n))
        except:return
       
a=0

while(a):
  print 23476523
  
  serl1=serl(97,a,100,101,102)
  
  
  time.sleep(.01)


  
    #time.sleep(.1)
    #if(x=='q'):
     #break
