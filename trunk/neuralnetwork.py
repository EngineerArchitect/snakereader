# -*- coding: utf8 -*-
"""Neural layers implementation for Python, uses logistic function as an activation function"""
from Numeric import *
import random
import math
class NeuralNetwork :	
	"""Neural network with learning based on backpropagation algorithm"""
	def __init__(self,K,M,N,alfamatrix='rnd',betamatrix='rnd',beta=1,eta=0.6):
		if alfamatrix=='rnd': alfamatrix=array([self.__rand(M) for i in range(K)])
		if betamatrix=='rnd':	betamatrix=array([self.__rand(N) for i in range(M)])
		self.beta,self.alfamatrix,self.betamatrix,self.K,self.M, self.N,self.eta=beta,array(alfamatrix),array(betamatrix),K,M,N,eta
	def __rand(self,n): return [random.random() for i in range(n)]
	def activationFunction (self, x) : 
		return 1/(1+math.exp(-self.beta*x))
	def saveFactors (self, filename) :
		pass
	def loadFactors (self, filename) :
		pass
	def getOutput (self, inputVector) :
		self.Y=array([self.activationFunction(i) for i in matrixmultiply(inputVector,self.alfamatrix)])
		self.Z=array([self.activationFunction(i2) for i2 in matrixmultiply(self.Y, self.betamatrix)])
		return self.Z
	def learn (self, inputVector, outputVector) :
		delta=outputVector-self.getOutput(inputVector)
		epsilon=array([sum(array([self.betamatrix[m,n]*delta[n] for n in range(1,self.N)]))for m in range(0,self.M)])
		for n in range(self.N):
			for m in range(self.M):
				self.betamatrix[m,n]+=float(self.eta*delta[n]*self.Z[n]*(1-self.Z[n])*self.beta*self.Y[m])
		for m in range(self.M):
			for k in range(self.K):
				self.alfamatrix[k,m]+=float(self.eta*epsilon[m]*self.Y[m]*(1-self.Y[m])*self.beta*inputVector[k])
		
if __name__ == "__main__": #this runs, when code is running as an own program, not as a module
	#you can use this section to test your module
	x=NeuralNetwork(2,2,2,[[0.0,0.0],[1.0,1.0]],[[0.0,0.0],[1.0,1.0]])
	print x.getOutput(array([2.0,2.0]))
	for i in range(500): x.learn(array([2.0,2.0]),array([0.6,0.09]))
	print x.alfamatrix
	print x.getOutput(array([2.0,2.0]))
	
	
