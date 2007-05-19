# -*- coding: utf8 -*-
"""Module docstring"""

import Image, ImageEnhance
#import math

class Frame :
    """Class docstring"""
    
    def __init__(self,f=None,new=False) :
            if new:
                self.matrix=Image.new('1',(1,1))
            else:
                self.matrix=Image.open(f)
            pass
    def putPixel (self, x, y) :
            """Method sets the pixel colour to black (for single-band images)"""
            self.matrix.putpixel((x,y),0)

    def getPixel (self, x, y) :
            """Method returns integer for single-band images (255:white, 0:black) and n-tuple for n-band images"""
            value = self.matrix.getpixel((x,y))
            return value

    def rotate (self,angle) :
            """Rotates an image by an angle"""
            self.matrix=self.matrix.rotate(angle)
            pass

    def blackWhite (self) :
            """Converts an image to single-band binary image"""
            
##
##            enhancer = ImageEnhance.Contrast(self.matrix)
##
##            for i in range(8):
##                factor = i / 4.0
##                enhancer.enhance(factor).convert('1').show("Contrast %f" % factor)
##            self.matrix=self.matrix.point(lambda i: 122.5*(math.tanh(2*i-256)+1))

            self.matrix = ImageEnhance.Contrast(self.matrix)
            self.matrix = self.matrix.enhance(2.5)
            
            self.matrix=self.matrix.convert('1')

    def hLineHistogram (self, number) :
            """Returns the sum of black pixels in the horizontal line of particular number"""
            count=0
            for i in range(self.matrix.size[0]):
                if self.getPixel(i,number)<=128:
                    count+=1
            return count
    def vLineHistogram (self, number) :
            """Returns the sum of black pixels in the vertical line of particular number"""
            count=0
            for i in range(self.matrix.size[1]):
                if self.getPixel(number,i)<=128:
                    count+=1
            return count
            pass
    def vLinesHistogram (self) :
            """Returns the list of results from vLineHistogram (self, number) for all pixel columns"""
            v_histogram=[]
            for number in range(self.matrix.size[0]):
                v_histogram.append(self.vLineHistogram (number))
            return v_histogram
            pass
    def hLinesHistogram (self) :
            """Returns the list of results from vLineHistogram (self, number) for all pixel columns"""
            h_histogram=[]
            for number in range(self.matrix.size[1]):
                h_histogram.append(self.hLineHistogram (number))
            return h_histogram
            pass
    def reScale (self, xSize, ySize) :
            """method docstring"""
            self.matrix=self.matrix.resize((xSize, ySize))
            pass
    
    def clear (self) :
            """Clears single black pixels"""
            for x in range((self.matrix.size[0]-1)):
                for y in range((self.matrix.size[1]-1)):
                    if self.matrix.getpixel((x,y))<=128 and self.matrix.getpixel((x+1,y))>128 and self.matrix.getpixel((x-1,y))>128 and self.matrix.getpixel((x,y+1))>128 and self.matrix.getpixel((x,y-1))>128:
                        self.matrix.putpixel((x,y),255)

            pass
    
    def leftCut(self) :
        """Cuts the image from the left to the beginning of text"""
        l_cut_point=0
        for i in range(self.matrix.size[0]-1):
                if self.hLineHistogram(i) >= 5: #0.001*self.matrix.size[1]:
                    l_cutpoint = i
                    break
        self.matrix=self.matrix.crop((l_cutpoint,0,self.matrix.size[0],self.matrix.size[1]))
        return self
        pass

    def vCut(self):
        """Cuts the sides of the image to the text borders"""
        self.leftCut()
        self.matrix=self.matrix.rotate(180)
        self.leftCut()
        self.matrix=self.matrix.rotate(180)
        return self
        pass
    
    def upperCut (self) :
            """Cuts the image from the upper side to the beginning of text"""
            u_cut_point=0
            for i in range(self.matrix.size[1]-1):
                if self.hLineHistogram(i) >= 5: #0.01*self.matrix.size[0]:
                    u_cutpoint = i
                    break
            self.matrix=self.matrix.crop((0,u_cutpoint,self.matrix.size[0],self.matrix.size[1]))
            return self
            pass
    def hCut(self) :
        """Cuts the image from the upper side to the beginning of text"""
        self.upperCut()
        self.matrix=self.matrix.rotate(180)
        self.upperCut()
        self.matrix=self.matrix.rotate(180)
        return self
        pass
    
    def hLineChangeHistogram (self, number) :
            """method docstring"""
            count=0
            for i in range(self.matrix.size[0]-1):
                if (self.getPixel(i,number)<=128 and self.getPixel(i+1,number)>128) or (self.getPixel(i,number)>128 and self.getPixel(i+1,number)<=128):
                    count+=1
            return count
            pass
    
    def hLinesChangeHistogram (self) :
            """method docstring"""
            h_change_histogram=[]
            for number in range(self.matrix.size[1]):
                h_change_histogram.append(self.hLineChangeHistogram(number))
            return h_change_histogram
            pass
        
    def vLineChangeHistogram (self, number) :
            """method docstring"""
            count=0
            for i in range(self.matrix.size[1]-1):
                if (self.getPixel(number,i)<=128 and self.getPixel(number,i+1)>128) or (self.getPixel(number,i)>128 and self.getPixel(number,i+1)<=128):
                    count+=1
            return count
            pass
    def vLinesChangeHistogram (self) :
            """method docstring"""
            v_change_histogram=[]
            for number in range(self.matrix.size[0]):
                v_change_histogram.append(self.vLineChangeHistogram(number))
            return v_change_histogram
            pass

    def getSize(self):
        return self.matrix.size
        return width,high

    def makeWhite(self, x, y) :
        self.matrix.putpixel((x,y),255)

        
##########        test methods            ##########

        
    def showPicture(self) :
            self.matrix.show()
            
    def savePicture(self,filename,format):
            """dodałem ją, gdyż do testów będzie bardzo potrzebna, a jej implementacja nie powinna Ci nastręczyć trudnosci"""
            self.matrix.save(filename,format)
		

if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
	#you can use this section to test your module
    f=open("200digram2.jpg",'rb')
    im=Frame(f)
    im.blackWhite()
    im.clear()
    print im.getSize()
    im=im.hCut()
    im=im.leftCut()
    print im.getSize()
    im.showPicture()
    pass
##    im=Frame(new=True)
##    im.showPicture()
