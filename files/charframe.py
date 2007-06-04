# -*- coding: utf8 -*-
"""Character recognition module"""
from frame import Frame
from neuralnetwork import NeuralNetwork
from PIL import Image, ImageEnhance# musiałem to dodać Lisu


class CharFrame(Frame) :

        def __init__(self, x,y):
            self.matrix = Image.new("1", (x,y), 255)
	"""Class like class frame, but size is 20x20 and recognition is added """
	def recognize (self) :
		"""method uses neural layer to recognize character"""
		pass
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
	#you can use this section to test your module
	pass
	
