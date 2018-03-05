import pygame
import time
import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk
import os
root = Tk()
rm=Frame(root,height="800",width="200",bg="#888")
rm.pack() #packs window to the left
#lm= tk.Label(root)
#lm.place(x=300,y=0)
#lm.pack()
os.environ['SDL_WINDOWID'] = str(root.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'


class jst:
    
    os.environ['SDL_WINDOWID'] = str(root.winfo_id())

    jx=300
    jy=200
    jz=90
    j1=0
    j2=0
    j3=0
    speed=4
    pygame.init()
    pygame.joystick.init()


    
    def __init__(self):
        jst.joy_get(self)
    def joy_get(self):
        
        #pygame.init()
        pygame.event.get()
        # Get count of joysticks
        joystick_count = pygame.joystick.get_count()
        # For each joystick
        for i in range(joystick_count):
            joystick = pygame.joystick.Joystick(i)
            joystick.init()
            # Usually axis run in pairs, up/down for one, and left/right for
            # the other.
            axes = joystick.get_numaxes()
            #print axes
            axis = float(joystick.get_axis( 2 ))
            axis=int(axis*100)
            if  axis>=1 and jst.jx<640:
                jst.jx=jst.jx+axis/jst.speed
            
            if  axis<=-1 and jx>0:
                jst.jx=jst.jx+axis/jst.speed
            axis = float(joystick.get_axis( 3 ))
            axis=int(axis*100)
            if axis>=1 and jy<480:
                jst.jy=jst.jy+axis/speed
            if axis<=-1 and jy>0:
                jst.jy=jst.jy+axis/speed
            axis = float(joystick.get_axis( 0 ))
            axis=int(axis*100)
            if axis>=1 and jst.jy<480:
                jst.jz=jst.jz+axis/(jst.speed*4)
            if axis<=-1 and jst.jy>0:
                jst.jz=jst.jz+axis/(jst.speed*4)
              #print axis

     
            
            buttons = joystick.get_numbuttons()
            

            
            button = joystick.get_button( 1 )
                
            if button==1 and jst.jx<640:
                    jst.jx=jst.jx+10
            button = joystick.get_button( 3 )
            if button==1 and jst.jx>0:
                    jst.jx=jst.jx-10
            button = joystick.get_button( 2 )
            if button==1 and jst.jy<480:
                    jst.jy=jst.jy+10
            button = joystick.get_button( 0 )
            if button==1 and jst.jx>0:
                    jst.jy=jst.jy-10
            button = joystick.get_button( 5 )
            if button==1 and jst.j1==0:
                    jst.j1=1
                    time.sleep(.5)
            elif button==1 and j1==1:
                    jst.j1=0
                    time.sleep(.5)
            button = joystick.get_button( 7 )
            if button==1 and jst.j2==0:
                    jst.j2=1
                    time.sleep(.5)
            elif button==1 and jst.j2==1:
                    jst.j2=0
                    time.sleep(.5)
            button = joystick.get_button( 4 )
            if button==1 and jst.j3==0:
                    jst.j3=1
                    time.sleep(.5)
            elif button==1 and jst.j3==1:
                    jst.j3=0
                    time.sleep(.5)
                       
              
             
                

#while(1):
#    jt=jst()
#    jt.joy_get()
#    print jt.jx
