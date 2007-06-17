# -*- coding: utf8 -*-
"""Character recognition module"""
from frame import Frame
from neuralnetwork import NeuralNetwork
import Image, ImageEnhance
from numpy.oldnumeric  import * ##I am using matrix implementation


class CharFrame(Frame) :
        """Class like class frame, but size is 30x30 and character recognition is added """
        def recognize (self) :
            """method uses neural layer to recognize character"""
            #FIXME: _very slow, it should be solved in a different way
            recognitionVector=[]
            for x in range(30):
                for y in range(30):
                    recognitionVector.append(float(self.getPixel(x,y))/4.0)
            neuralNet=[]
            for letter in range(5):
                neuralNet.append(NeuralNetwork(900,50,1))
                neuralNet[letter].loadFactors(str(letter)+'.bin')
            outputList=[]
            for neur in neuralNet:
                outputList.append(neur.getOutput(array(recognitionVector)))
            result=[]
            stringi='aąbcćdeęfghijklłmnńoóprtsśtuvwxyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUVWXYZŹŻ'
            charList=list(stringi)+['_' for i in range(100)]
            for i in range(len(outputList)):
                result.append((outputList[i],charList[i]))
            result.sort()
            result.reverse()
            return result
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
	#you can use this section to test your module
	f=open('1lin7.bmp','rb')
	a=CharFrame(f)
	print a.recognize()

    
    
    
