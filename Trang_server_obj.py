# Trang_server_Trang_serverobj.py
'''
============= abcdef=================================
a   Tris becomes the class: Trang_server
b                     
c   The initial test will show square 3 points 
d   wide in the center
d   
e   self.paper_row==> self.paper_holds  
f      self.background                                            
jsdgdkgskydgdkgdkgskgskgskgskgsksksjgsjgsjgsjxjgxjjjx
'''
class Trang_server:
  # =================================================
  '''
    Initialize Section - the standard rows simulate
    graph paper with cartesian axes. It has 10 rows
    aboe and below the origin with twenty columns 
    left and right of it.
  '''
  # =================================================

  def __init__(self):
      std_row = 20*" "+"|"+20*" "
     
      self.paper_holds =[std_row for r in range(21)]
      self.paper_holds[10] = 20*"-"+"+"+20*"-"
  # =================================================
  '''
    Second Section - the "private functions" support
    "accept_labels" defined below. They are about
    overwriting the "paper" which will become the final
    display as seen on the console.
    
    For the rows, the picture of the x resuly is always
    above the x-axis (starting at row zero) and the 
    the picture of the x resuly is always below it.
    Thus, it starts at row 12.
    
    For the columns, these pictures could appear on one of:
    
    "left" -- column zero of the paper
    "right" -- column 23 of the paper
  '''
  # =================================================
  def _eachlabel_left(self,pic,offset=0): 
       for row in range(8):
             curr=self.paper_holds[row+offset]
             replaced=pic[row]+curr[19:]
             self.paper_holds[row+offset]=replaced
    
  def _eachlabel_right(self,pic,offset=0): 
       for row in range(8):
             curr=self.paper_holds[row+offset]
             replaced=curr[:22]+pic[row]
             self.paper_holds[row+offset]=replaced
   
  def _labels_left(self): 
       self._eachlabel_left(self._picX)
       self._eachlabel_left(self._picY,offset=12)
    
  def _labels_right(self):
       self._eachlabel_right(self._picX)
       self._eachlabel_right(self._picY,offset=12)
  # =================================================
  '''
    Main Section -  The "public" functions
    accepting labels,image and "showing the paper"
  '''
  # =================================================
  def accept_labels(self,numeric_labels): 
       pic_onRHS,self._picX,self._picY=numeric_labels
       if pic_onRHS:
           self._labels_left()
       else:
           self._labels_right()
           
  def accept_image(self,drawn):
      for pair in drawn:
            stargoes,rowout=pair
            was_there=self.paper_holds[rowout]
            self.paper_holds[rowout]=was_there[:(stargoes)]+\
                               "#"+was_there[(stargoes+1):]  
      return None

  def show_paper(self):
    end_row="\n"
    all_rows = [str(rol)+end_row for rol \
                          in self.paper_holds]
    
    return "".join(all_rows)
         
  # =================================================
  '''
    Final Section - Testing when run as stand-alone.
    This is the only place where the "graphics" 
    intention is "dry-run" together with the labels
    within the same "paper".
    
    test_picRight --> simulates a picture on the 
    right of the display requiring two labels on the
    left. The only alternative to this is test_picLeft
    which would show the exact opposite.
  '''
  # =================================================
    
def test_picRight():
       svr=Trang_server()

       image=[]
       for x in range(23,28):
            image.append(tuple([x,4]))
            image.append(tuple([x,8]))
 
       for y in range(5,8):
            image.append(tuple([23,y]))
            image.append(tuple([28,y]))
             
       Label_Repeat_for_x = "abcde..12345..XXXxx"
       num_x=[ Label_Repeat_for_x for i in range(8) ]
       
       Label_Repeat_for_y = "abcde..12345..YYYyy"
       num_y=[ Label_Repeat_for_y for i in range(8)]
       
       numeric_numleft=tuple([True,num_x,num_y])
       
       svr.accept_image(image)
       svr.accept_labels(numeric_numleft)
       
       print(svr.show_paper())
       _ignore=input("picture shown on RHS")

def TrangServe_basictest():
      test_picRight()
# ========================================
        
if __name__ == "__main__":
     TrangServe_basictest()