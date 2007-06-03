import sys

sys.path.append(sys.path[0]+"/files")
from control import *
control=Control()
f=control.inputFile('l1.jpg')
lineList=control.blockSegmentation(f,[])
charList=[]
for line in lineList:
    charList.append(control.characterSegmentation(line,[]))
neur=NeuralNetwork(400,50,4,[(1,1),(2,2),(3,3)])
i=0
for x in charList:
    if i==0: char=[1.0,0.0,0.0,0.0]
    if i==1: char=[0.0,1.0,0.0,0.0]
    if i==2: char=[0.0,0.0,1.0,0.0]
    if i==3: char=[0.0,0.0,0.0,1.0]
    for y in x:
        kafel=[]
        for z in y:
            for i1 in range(19):
                for i2 in range(19):
                    kafel.append(z.getPixel(i1,i2))
        neur.learn(array(kafel),array(char))
    i+=1
