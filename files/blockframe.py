# -*- coding: utf8 -*-
"""Module docstring"""
#import Image, numpy, #pywt
from PIL import Image #Lisu: musiałem to dodać, bo u mnie się nie włącza
import numpy
from frame import Frame
from lineframe import LineFrame
class BlockFrame(Frame) :
     """class docstring"""
##     def __init__(self) :#init może zniknąć
##          pass
     def findLevel (self) :
          """Finds the skew of the text"""
          data = numpy.array(list(self.matrix.getdata()))
          data.shape = (self.matrix.size[1], self.matrix.size[0])
          
          data = pywt.dwt2(data,'Haar')
          return data
     def centroid(self,data):
          """Finds the centroid of given set of data"""

     def extractLine (self):
          """returns one line from the text"""
          self.hCut()

          for treshold in range (20,0,-1):
               if self.findCutpoint(treshold)>0: ## later: pixels per character            
                    cutpoint=self.findCutpoint(treshold)
               

          line=LineFrame(new=True)
          
          line.matrix=self.matrix.crop((0,0,self.matrix.size[0],cutpoint-1))
          line.vCut()
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
          i=0
          while self.matrix.size[1]!=0:
               a=self.extractLine()
               lines.append(a)
               a.matrix.save(str(i)+'.BMP')
               i+=1
##               print self.matrix.size[1]
          return lines
          pass
        
        
if __name__ == "__main__":
     #this runs, when code is running as an own program, not as a module
     
     
     f=open("p1.jpg",'rb')
     im=BlockFrame(f)
     im.blackWhite()
     im.clear()
     im.hCut()
     im.vCut()     
     im.showPicture()
     print im.findLevel()
##     a=im.matrix.tobitmap()
##     
##     print a
##     x=Image.fromstring('1',(896,253),a)
##     x.show()
##     print a[2398]
####     im.clear()
     l=im.extractLines()

######     
####        
##     im.showPicture()
##     im.upperCut()
##for i in range (50):
##     print im.findCutpoint(i)
