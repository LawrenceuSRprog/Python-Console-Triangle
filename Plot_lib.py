# Plot_lib.py

# =================================================
'''
Overview
========

The method "build_image(coords)" produces a right 
angled triangle starting from the origin. The three
sides are called: Ramp, Wall and Ground. This the 
point at the top of the ramp forms the "wall" by 
"dropping" to the x-axis and defining "ground" as 
the distance back from there to the origin.

The maximum possible x and y available are determined
    ------------------------
by 10 rows above and below the "ORIGIN" which also has
20 columns before and after it.

'''
# =================================================
'''
    First Section - Going from the point 
                           (at the top of the ramp)
        (dropping) down and (horizontally) back to
        the orign. At this stage of the program
        they are each parrallel to an axis and 
        represented as whole numbers.
'''
# =================================================

def go_drop(from_pt):
       x,ybegin,yfinal=from_pt[0],from_pt[1],10
       if yfinal<ybegin: yfinal,ybegin=ybegin,yfinal
       
       return [tuple([x,y])for y in \
              range(ybegin,yfinal) ] +[tuple([x,10])]

def go_back(from_pt):
       y,xbegin,xfinal=10,from_pt[0],20

       if xfinal<xbegin: xfinal,xbegin=xbegin,xfinal
       
       return [tuple([x,y])for x in \
                        range(xbegin,xfinal) ]
# =================================================
'''
    Second Section - What ever the requested scale,
    the "target" is picked as if the radius reaches
    the maximum possible x and y available.
    
    The line which joins the origin is called the 
    ramp and it is built from steps which ultimately
    must be presented as whole numbers.

'''
# =================================================
    
def take_one_step(from_origin,delta_pair):
     return [from_origin[0]+delta_pair[0],
             from_origin[1]+delta_pair[1]]

def steps_from_origin(target):
      x_col,y_row=target
      from_origin = [float(x_col-20) ,float(y_row-10)]
      delta_pair = [from_origin[0]/25, \
                          from_origin[1]/25]

      return [ [float(20),float(10) ] for i in range(25) ], \
                                            tuple(delta_pair)

def steps_towards(target):
     steps_in_ramp,step_delta=steps_from_origin(target)
 
     for index  in range(24):
          steps_in_ramp[index+1]=\
                        take_one_step(step_delta,
                                 steps_in_ramp[index])
     return steps_in_ramp

def replace_with_whole(pair):
      return [round(pair[0]),round(pair[1])]

def fitted_standard_colrow(coords):
      xprod,yprod,length=coords

      return tuple(
         [20+round(20*xprod/length),
          10-round(10*yprod/length)])

def begin_ramp(coords):
       target=fitted_standard_colrow(coords) 
       return [replace_with_whole(pair) for pair \
                         in steps_towards(target)], \
                         replace_with_whole(target)

# =================================================
'''
    Main Section -  The "public" function
'''
# =================================================

def build_image(coords):
      ramp_series,apex= begin_ramp(coords)
      wall,ground=go_drop(apex), go_back(apex) 
      return ramp_series+wall+ground

# =================================================
'''
    Final Section - Testing when run as stand-alone
    When run normally - the "Trang_server_obj" would 
    NOT be available. However it is allowed here so
    that the "graphics" intention can be evaluated.

'''
# =================================================

def builder_params(thedeg,length,slope_desc):            
      ang=math.pi*thedeg/180
      coords = tuple( [length*math.cos(ang), 
             length*math.sin(ang),
             length])
             
      return build_image(coords)

def hubof_basictest(thedeg,length,slope_desc):
      import Trang_server_obj as Trang        
      fake_svr=Trang.Trang_server()
      
      image=builder_params(thedeg,length,slope_desc)
      fake_svr.accept_image(image)
      
      print(fake_svr.show_paper())
      fake_svr=None
      input(slope_desc)
        
def Plotter_basictest():
      thedeg,length,slope_desc=45.0,100.0, \
                    "==== Slope is North-East ===="
      hubof_basictest(thedeg,length,slope_desc)
      #
      thedeg,length,slope_desc=135.0,100.0, \
                     "==== Slope is North-West ===="
      hubof_basictest(thedeg,length,slope_desc)
      #     
      thedeg,length,slope_desc=-135.0,100.0, \
                    "==== Slope is South-West ===="
      hubof_basictest(thedeg,length,slope_desc)
      #
      thedeg,length,slope_desc=-30.0,100.0, \
                     "==== Slope is South East===="
      hubof_basictest(thedeg,length,slope_desc)
      
# ========================================
if __name__ == "__main__":
    import math 
    Plotter_basictest()
