# Triangle_Code.py
'''
============= abcdef=================================
a   
b   
c   
d
e  
f
=====================================================
'''

'''
Draw a triangle from center of circle.
=====================================

Descibe with two args:
    deg --> anti clockwise angle in degrees
  scale --> radius of circle

Output list of points:
      0 --> the center!
      1 --> outer point on edge
      2 --> like {1} on x-Axis

'''

import math 
import Ovec_lib as ovl
import Plot_lib as plt
import Trang_server_obj as Trang
       
def asked_user():
      ask=("Angle above x-axis (0-360) > ",
             "Units away from Org. (10-999) > ")
             
      thedeg,length=float(input(ask[0])), \
                     float(input(ask[1]))
                     
      ang=math.pi*thedeg/180
                     
          
      return tuple( [length*math.cos(ang), \
             length*math.sin(ang),
             length])

def WritePlot_hub(user_display,coords):        
      image = plt.build_image(coords)
      user_display.accept_image(image)
      
      numeric_labels = ovl.build_labels(coords)
      user_display.accept_labels(numeric_labels)
      
      print(user_display.show_paper()) 
      # background=created_paper()
                
def WriteAndPlot():        
      user_display=Trang.Trang_server()
      coords = asked_user()
      WritePlot_hub(user_display,coords)
       
if __name__ == "__main__":
    WriteAndPlot()