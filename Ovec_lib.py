# Ovec_lib.py
# =================================================
'''
Overview
========

The method "number_matrix" shows a number in a 
“Console-style” output of one char per pixel. The 
function takes an integer and returns eight rows of chars 
which represent EXACTLY three figures. When the size of the
number is less than 100 it is padded with leading zeros. 
When the size is more than 999, it only shows the FIRST 
three figures. Negative numbers have EXACTLY 2 figures -
since the first is the leading minus.

== Examples ==  -7 ==> -07  72 ==> 072  5923 ==> 592

Algorithm
=========
The dictionary provides 8*5-pixel patterns for the 11 chars
it supports; these are the “minus” and digits (0 to 9).
Allowing 2 pixels in between each char gives totals:

   WIDTH: (5+2) + (5+2) +5 = 17 chars
   HEIGHT: 8 chars
'''
# =================================================
'''
    First Section - Pixel Dictionary 
                    ================
         + -  and digits 0 to 9
'''
# =================================================

def dic_pixel_font():
 
  return {'1':['   11',
               ' 1111',
               '11 11',
               '   11',
               '   11',
               '   11',
               '   11',
               '   11'],
       
          '2':[' 222 ',
               '22 22',
               '2  22',
               '   22',
               '   22',
               '  22 ',
               ' 22  ',
               '22222'],
       
           '3':[' 333 ',
               '33 33',
               '3  33',
               '   33',
               ' 3333',
               '   33',   
               '33 33',
               ' 333 '],
               
          '4':['  44 ',
               ' 44  ',
               '44   ',
               '44 44',
               '44 44',
               '44444',
               '   44',
               '   44',],
       
           '5':['55555',
                '55   ',
                '55   ',
                '55   ',
                '  555',
                '    5',   
                '    5',
                '5555 '],
       
          '6':['   66',
               '  66 ',
               '.66  ',
               '6666 ',
               '66666',
               '6  66',
               '6  66',
               '66666'],
       
           '7':['77777',
                '   77',
                '   7 ',
                '  77 ',
                '  7  ',
                ' 77  ',   
                ' 7   ',
                '77   '],
              
       
           '8':[' 888 ',
                '8   8',
                '8   8',
                ' 888 ',
                ' 888 ',
                '8   8',
                '8   8',   
                ' 888 '],
               
          '9':['99999',
               '9  99',
               '9  99',
               '9  99',
               ' 9999',
               '  99 ',
               ' 99  ',
               '99   '],
       
           '0':[' 000 ',
                '00 00',
                '0   0',
                '0   0',
                '0   0',
                '0   0',   
                '00 00',
                ' 000 '],
       
          '-':['     ',
               '     ',
               '     ',
               '     ',
               '#####',
               '     ',
               '     ',
               '     '],                 
                
          '+':['     ',
               '     ',
               '  ## ',
               '  ## ',
               '#####',
               '  ## ',
               '  ## ',
               '     ']                            
                
                }
                
# =================================================
'''
    Second Section - Pixel Matrix
                     ============
    Represents the orignal number as three figures
    forming a matrix of characters 8 rows * 17 cols
'''
# =================================================
         
def each_pixel_line(row,fig_trio):
        spacer,d_xo=2*" ",dic_pixel_font()
        return str(d_xo[fig_trio[0]][row]+spacer+ \
            d_xo[fig_trio[1]][row]+spacer+ \
            d_xo[fig_trio[2]][row])
      
def pixel_matrix(fig_trio):
       return [each_pixel_line(r,fig_trio) for r in range(8) ]
       
def number_matrix(number,limit_of2=False):
       return pixel_matrix(made_into3figs(number, \
                                        limit_of2))
                                        

def reduce_suffix(numx,maintain_2=True):
     base,num=1000,abs(float(numx))
     if maintain_2 : base=100
     if numx<0: base=100
     while num>=base: num/=10
     return int(round(num))
                 
         
def made_into3figs(numx,limit_of2):
      see_digit,prefix=2,"+"
      if limit_of2==False and numx>0:
           see_digit,prefix=3,""
      if numx<0: prefix="-"
      rhs="000000"+str(reduce_suffix(numx, \
                    maintain_2=limit_of2))
      return prefix+rhs[-see_digit:]
      
# =================================================
'''
    Main Section -  The "public" function
    There are three return values:
    
    picture_right is boolean: 
      True - the image goes to the right of the paper
      False - the image goes to the left of the paper
      
    number_matrix produced for x display
    number_matrix produced for y display
'''
# =================================================

def build_labels(coords):      
      xprod,yprod,_ignore=coords
      
      print(" * * * Debug ==> Values look like",
            int(xprod),",",int(yprod))
                  
      signs_required = bool( xprod<0 or yprod<0 )     
            
      picture_right= bool(xprod >= 0)      
      return picture_right, \
        number_matrix(xprod,limit_of2=signs_required),\
        number_matrix(yprod,limit_of2=signs_required)     
        
# =================================================
'''
    Final Section - Testing when run as stand-alone
'''
# =================================================
def num_pattern_basictest():   
      
      print("*** Should be 258 **")
      print("abcdefghij123456789")
      number=25775
      plate=number_matrix(number)
      for pl in plate:print (pl)
      print("abcdefghij123456789")
      
      print("*** Should be +51 **")
      print("abcdefghij123456789")
      number=512
      plate=number_matrix(number,limit_of2=True)
      for pl in plate:print (pl)
      print("abcdefghij123456789")
        
      print("*** Should be 091 **")
      print("abcdefghij123456789")
      number=91
      plate=number_matrix(number)
      for pl in plate:print (pl)
      print("abcdefghij123456789")
      
      print("*** Should be -03 **")
      print("abcdefghij123456789")
      number=-3
      plate=number_matrix(number)
      for pl in plate:print (pl)
      print("abcdefghij123456789")
  
# ===========================================
if __name__ == "__main__":
     num_pattern_basictest()
