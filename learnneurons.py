import sys
from numpy.oldnumeric  import * ##I am using matrix implementation

sys.path.append(sys.path[0]+"/files")
from control import *
control=Control()
neur=NeuralNetwork(400,40,4,[(n,n) for n in range(0,3)])
neur.loadFactors('fourletters3.bin')

f=control.inputFile('l1.jpg')
lineList=control.blockSegmentation(f,['','','poor'])
charList=[]
char=[]
char.append([1.0,0.0,0.0,0.0])
char.append([0.0,1.0,0.0,0.0])
char.append([0.0,0.0,1.0,0.0])
char.append([0.0,0.0,0.0,1.0])
        
for line in lineList:
    charList.append(control.characterSegmentation(line,[]))

for n in range(1):
    i=0
    kafel=[[],[],[],[],[]]    
    for x in charList:
        for y in x:
            for z in y:
                helpList=[]
                for i1 in range(20):
                    for i2 in range(20):
                        helpList.append(int(z.getPixel(i1,i2)==255))
                kafel[i].append(helpList)
                print len(helpList)
                #print len(kafel)
                #print kafel
            
        i+=1
        print 'letter '+str(i)
    print str(n)


for n in range(10):
    print n
    print neur.getOutput(array(kafel[0][2]))
    print neur.getOutput(array(kafel[1][2]))
    print neur.getOutput(array(kafel[2][2]))
    print neur.getOutput(array(kafel[3][2]))
    print ' '
    for line in range(4):
        for letter in range(10):
            neur.learn(array(kafel[line][letter]),array(char[line]))    

print neur.getOutput(array(kafel[0][2]))
print neur.getOutput(array(kafel[1][2]))
print neur.getOutput(array(kafel[2][2]))
print neur.getOutput(array(kafel[3][2]))
neur.saveFactors('fourletters3.bin')
