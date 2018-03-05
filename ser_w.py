import serial
import time
g=1
s=1
try:ser = serial.Serial('COM23', 9600, timeout=0)
except:g=0
def serial_write(x,y):
    s=1
    #x = eval(raw_input("Enter X coordinate: "))
    #y = eval(raw_input("Enter Y coordinate: "))
    X=(chr(x))
    Y=(chr(y))
    
    print X
    
    print x
    print Y
    print y
    #if ser.read()=='a':
    ser.write(X)
    #if ser.read()=='b':
    ser.write(Y)
    

    #time.sleep(.1)
    #if(x=='q'):
     #break
def serial_write_ang(x,y,z,m,n):
    s=1
    try:ser.flushInput()
    except:0
    try:ser.flushOutput()
    except:0
    #x = eval(raw_input("Enter X coordinate: "))
    #y = eval(raw_input("Enter Y coordinate: "))
    X=(chr(x))
    Y=(chr(y))
    Z=(chr(z))
    M=(chr(m))
    N=(chr(n))
    
    
   
   
    #if ser.read()=='a':
    try:ser.write(X)
    except:return
    #if ser.read()=='b':
    ser.write(Y)
    ser.write(Z)
    ser.write(M)
    ser.write(N) 
    

    #time.sleep(.1)
    #if(x=='q'):
     #break
