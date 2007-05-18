# -*- coding: utf8 -*-
"""Module docstring"""
import Image
from frame import Frame
from lineframe import LineFrame
class BlockFrame(Frame) :
     """class docstring"""
##     def __init__(self) :#init może zniknąć
##          pass
     def findLevel (self) :
          """method docstring"""
          pass
     def extractLine (self):
          """returns one line from the text"""
          self.upperCut()
          cutpoint=0
          for i in range (self.matrix.size[1]):
               if self.hLineHistogram(i)>9:
                    cutpoint+=1
               else:
                    break
          line=LineFrame("200digram2.jpg")
          line.matrix=self.matrix.crop((0,0,self.matrix.size[0],cutpoint))
          self.matrix = self.matrix.crop((0,cutpoint,self.matrix.size[0],self.matrix.size[1]))
          return line
          pass
     def extractLines(self):
          pass
        
        
if __name__ == "__main__":
     #this runs, when code is running as an own program, not as a module
     
     
     f=open("200digram2.jpg",'rb')
     im=BlockFrame(f)
     im.blackWhite()
     im.clear()
     im.extractLine().showPicture()
     
     
     im.showPicture()
     pass
