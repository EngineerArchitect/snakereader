import sys
from numpy.oldnumeric  import * ##I am using matrix implementation

sys.path.append(sys.path[0]+"/files")
from control import *
control=Control()
neur=NeuralNetwork(400,40,4,[(n,n) for n in range(0,3)])
neur.loadFactors('fourletters.bin')
f=control.inputFile('l1.jpg')
lineList=control.blockSegmentation(f,['','','poor'])
charList=[]
for line in lineList:
    charList.append(control.characterSegmentation(line,[]))

for n in range(20):
    i=0
    kafel=[[],[],[],[],[]]
    char=[]
    for x in charList:
        char.append([1.0,0.0,0.0,0.0])
        char.append([0.0,1.0,0.0,0.0])
        char.append([0.0,0.0,1.0,0.0])
        char.append([0.0,0.0,0.0,1.0])
        for y in x:
            for z in y:
                kafel[i]=[]
                for i1 in range(20):
                    for i2 in range(20):
                        kafel[i].append(int(z.getPixel(i1,i2)==255))
                #print len(kafel)
                #print kafel
                for j in range(i+1):
                    neur.learn(array(kafel[j]),array(char[j]))    
            
        i+=1
        print 'letter '+str(i)
    print str(n)
print neur.getOutput(array(kafel[0]))
print neur.getOutput(array(kafel[1]))
print neur.getOutput(array(kafel[2]))
print neur.getOutput(array(kafel[3]))
neur.saveFactors('fourletters2.bin')
