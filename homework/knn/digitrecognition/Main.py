import math
import csv
import operator
import plotpixel as plt

'''---------------Helper Methods---------------'''

# load training data

def loadData(fileName):
    with open(fileName, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)

        return dataset

def printDataset(dataset):
    for x in range(len(dataset) - 1):
        echo( dataset[x] )


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        if(x==0):
            continue
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        # distances.append((trainingSet[x], dist,trainingSet[x][0]))
        distances.append((dist,trainingSet[x]))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x])
    return neighbors


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        # print "x is %d instance1[x], instance2[x] :::", x ,instance1[x], instance2[x];
        distance += pow((int(instance1[x+1] ) - int(instance2[x])), 2)
    return math.sqrt(distance)

def echo(message):
        # print message
        return

'''---------------Helper Methods---------------'''

def main():

    trainingData = loadData('data/train.csv')

    testData =   loadData('data/test.csv')

    instance = testData[10]

    plt.drawPixels(instance,nRows=28,nCols=28)

    neighbors = getNeighbors(trainingData,instance,10)

    echo( neighbors )

    # printDataset(testData)
    echo (neighbors[0][1])

    for i in range(len(neighbors)):
        # plt.drawPixels(neighbors[i][1][1:],nRows=28,nCols=28)
        echo( "hello" )

main()
