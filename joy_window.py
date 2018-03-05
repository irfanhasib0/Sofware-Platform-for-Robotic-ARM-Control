import pygame
import time
jx=0
jy=0
j1=0
j2=0
j3=0






#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates


# Initialize the joysticks
pygame.init()




#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates


pygame.joystick.init()



#def joy_get(jx):
def joy_get(jx,jy,j1,j2,j3,speed):
    
    #pygame.init()
    pygame.event.get()
    #clock.tick(240)
    #pygame.init()# User did something
       
 

    # EVENT PROCESSING STEP
    
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
   

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
       
    
        # Get the name from the OS for the controller/joystick
        #name = joystick.get_name()
        #print name
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        #print axes
        
        
        
        axis = float(joystick.get_axis( 2 ))
        axis=int(axis*100)
        if  axis>=1 and jx<640:
            jx=jx+axis/speed
        
        if  axis<=-1 and jx>0:
            jx=jx+axis/speed
        axis = float(joystick.get_axis( 3 ))
        axis=int(axis*100)
        if axis>=1 and jy<480:
            jy=jy+axis/speed
        if axis<=-1 and jy>0:
            jy=jy+axis/speed
          #print axis

 
        
        buttons = joystick.get_numbuttons()
        

        
        button = joystick.get_button( 1 )
            
        if button==1 and jx<640:
                jx=jx+10
        button = joystick.get_button( 3 )
        if button==1 and jx>0:
                jx=jx-10
        button = joystick.get_button( 2 )
        if button==1 and jy<480:
                jy=jy+10
        button = joystick.get_button( 0 )
        if button==1 and jx>0:
                jy=jy-10
        button = joystick.get_button( 5 )
        if button==1 and j1==0:
                j1=1
                time.sleep(.5)
        elif button==1 and j1==1:
                j1=0
                time.sleep(.5)
        button = joystick.get_button( 7 )
        if button==1 and j2==0:
                j2=1
                time.sleep(.5)
        elif button==1 and j2==1:
                j2=0
                time.sleep(.5)
        button = joystick.get_button( 4 )
        if button==1 and j3==0:
                j3=1
                time.sleep(.5)
        elif button==1 and j3==1:
                j3=0
                time.sleep(.5)
                   
            
         
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        #hats = joystick.get_numhats()
        
        #for i in range( hats ):
         #   hat = joystick.get_hat( i )
        return jx,jy,j1,j2,j3
       
       

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
   

    # Limit to 20 frames per second
   
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
#pygame.quit ()

