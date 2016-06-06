#class,long,sweet,Yellow
#(0(Banana),1(Orange),2(Other))

import random
import csv

#---------------------Utilities -------------------------
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = int(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

def calculateProbabilities(trainingSet=[]):
        total = len(trainingSet)
        print (total)
        totalClass0 = 0
        totalClass1 = 0
        totalClass2 = 0

        bananaFeaturesCount=[0,0,0]
        orangeFeaturesCount=[0,0,0]
        otherFeaturesCount =[0,0,0]

        for i in range(total):
            element = trainingSet[i][0]
            if(element==0):
                # Banana Class
                totalClass0+=1
                incrementFeature(trainingSet[i],bananaFeaturesCount)
            elif(element==1):
                #  Class Orange
                totalClass1+=1
                incrementFeature(trainingSet[i], orangeFeaturesCount)
            elif(element==2):
                # Class Other
                totalClass2+=1
                incrementFeature(trainingSet[i], otherFeaturesCount)

        print ("Probability Banana ",float(totalClass0)/total)
        print ("Probability Orange ", float(totalClass1)/total)
        print ("Probability Other ", float(totalClass2)/total)

#         Calculate bayesian probabilities given features
        probLongGivenBanana = float(bananaFeaturesCount[0])/totalClass0
        probSweetGivenBanana = float(bananaFeaturesCount[1])/totalClass0
        probYellowGivenBanana = float(bananaFeaturesCount[2])/totalClass0

        probBanana = float(totalClass0)/total


        probBananaGivenLongSweetYellow = (probLongGivenBanana*probSweetGivenBanana*probYellowGivenBanana)*(probBanana)

        print ('Probability of Banana given Long,Sweet,Yellow %f' %(probBananaGivenLongSweetYellow))

        #         Calculate bayesian probabilities given features
        probLongGivenOrange = float(orangeFeaturesCount[0]) / totalClass1
        probSweetGivenOrange = float(orangeFeaturesCount[1]) / totalClass1
        probYellowGivenOrange = float(orangeFeaturesCount[2]) / totalClass1

        probOrange = float(totalClass1) / total

        probOrangeGivenLongSweetYellow = (probLongGivenOrange * probSweetGivenOrange * probYellowGivenOrange) * (probOrange)

        print ('Probability of Orange given Long,Sweet,Yellow %f' % (probOrangeGivenLongSweetYellow))

        #         Calculate bayesian probabilities given features
        probLongGivenOther = float(otherFeaturesCount[0]) / totalClass2
        probSweetGivenOther = float(otherFeaturesCount[1]) / totalClass2
        probYellowGivenOther = float(otherFeaturesCount[2]) / totalClass2

        probOther = float(totalClass2) / total

        probOtherGivenLongSweetYellow = (probLongGivenOther * probSweetGivenOther * probYellowGivenOther) * (probOther)

        print ('Probability of Other given Long,Sweet,Yellow %f' % (probOtherGivenLongSweetYellow))


def incrementFeature(tuple,featureCount):
    for i in range(len(tuple)):
        if (i==0):
            continue
        element = tuple[i]
        if (element==1):
            featureCount[i-1]+=1
    return

#---------------------Utilities -------------------------

def main():
    # Dataset structure
    # class,long,sweet,Yellow
    # (0(Banana),1(Orange),2(Other))
    # Example 0,1,1,1 means Banana,long,sweet and Yellow
    # Example 2,0,1,0 means Other,not long,Sweet,not Yellow
    # Resources http://blog.aylien.com/post/120703930533/naive-bayes-for-dummies-a-simple-explanation
    # http://stackoverflow.com/questions/10059594/a-simple-explanation-of-naive-bayes-classification

    trainingSet = []
    testSet = []
    split = .6

    loadDataset('training.data',split,trainingSet,testSet)

    print ('Training data ',trainingSet)
    print ('Testing Data ',testSet)

    calculateProbabilities(trainingSet)

    return

main()
