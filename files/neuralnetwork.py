# -*- coding: utf8 -*-
"""Neural layers implementation for Python, uses logistic function as an activation function"""
class NeuralNetwork :	
	"""Neural network with learning based on backpropagation algorithm"""
	class NeuralLayer :
		""" """
		class Neuron :
			""" """
			def __init__(self) :
				self.w = [] # List of factors
				pass
			def setFactor (self, number, value) :
				pass
			def getOutput (self, inputVector) :
				pass
			def learn (self, delta, inputVector) :
				pass
			def activationFunction (self, x) :
				pass

		def __init__(self) :
			pass
		def getOutput (self, inputVector) :
			pass
		def countDeltas (self) :
			pass
		def learn (self, deltas, inputVector) :
			pass
	class NeuralOutputLayer(NeuralLayer) :
		def countOutputDeltas (self, inputVector, outputVector) :
			pass
	#end of integrated classes
	def saveFactors (self, filename) :
		pass
	def loadFactors (self, filename) :
		pass
	def getOutput (self, inputVector) :
		pass
	def learn (self, inputVector, outputVector) :
		pass
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
	#you can use this section to test your module
	pass

