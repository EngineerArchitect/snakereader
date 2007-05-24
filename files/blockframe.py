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
          self.hCut()

          for treshold in range (20,0,-1):
               if self.findCutpoint(treshold)>0: ## later: pixels per character            
                    cutpoint=self.findCutpoint(treshold)
               

          line=LineFrame(new=True)
          
          line.matrix=self.matrix.crop((0,0,self.matrix.size[0],cutpoint-1))
          self.matrix = self.matrix.crop((0,cutpoint,self.matrix.size[0],self.matrix.size[1]))
          return line
                         
          
     def findCutpoint(self,treshold):
          """finds the hight of a sigle line"""
          cutpoint=1
          for i in range (self.matrix.size[1]):
               if self.hLineHistogram(i)>treshold:
                    cutpoint+=1
               else:
                    break
          return cutpoint
     def extractLines(self):
          """returns a list of all lines in the text"""
          lines=[]
          while self.matrix.size[1]!=0:
               a=self.extractLine()
               lines.append(a)
               a.showPicture()
##               print self.matrix.size[1]
          return lines
          pass
        
        
if __name__ == "__main__":
     #this runs, when code is running as an own program, not as a module
     
     
     f=open("p.jpg",'rb')
     im=BlockFrame(f)
     im.blackWhite()
     im.clear()
     l=im.extractLines()
     
##     
##     
##     im.showPicture()
##     im.upperCut()
##for i in range (50):
##     print im.findCutpoint(i)
