# Tryout 2: Second attempt to solve the handwritten digits
# We break the whole training set in x:y ration and treat y as the
# testing dataset for calculating the accuracy of the algorithm

import math
import csv
import operator

from __builtin__ import len

import plotpixel as plt
import random

'''---------------Helper Methods---------------'''

# load training data

# def loadData(fileName):
#     with open(fileName, 'rb') as csvfile:
#         lines = csv.reader(csvfile)
#         dataset = list(lines)
#
#         return dataset

def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            # First line in this dataset is the label not the data
            if (x==0):
                continue
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

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
    distances.sort(key=operator.itemgetter(0))
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
        print message
        return

'''---------------Helper Methods---------------'''

def main():
    # prepare data
    trainingData = []
    testData = []
    split = 0.67

    loadDataset('data/train.csv', split, trainingData, testData)
    # loadDataset('actualdata/train.csv', split, trainingData, testData)

    matches = 0

    for x in range(len(testData)):
        instance = testData[x]
        neighbors = getNeighbors(trainingData,instance,3)
        guess = int(getGuessedDigit(neighbors))
        actual = int(instance[0])

        echo('(%d) Guessed Value %d ' %(x , guess))
        echo('(%d) Actual Value %d ' %(x , actual))

        if(guess == actual):
            matches +=1
        else:
            echo('Displaying character which is not matching')
            # plt.drawPixels(instance[1:], nRows=28, nCols=28)

    echo ('Total matches %d out of %d' %(matches,len(testData)))

    echo ('Accuracy is %f  ' %((matches)/float(len(testData))*100)+'%')


# def getGuessedDigit(items):
#     # Iterate over the neighbors
#     # for i in range(len(items)):
#     #     echo(items[i][0])
#     return items[0][1][0]

# def getGuessedDigit(items):
#     # Iterate over the neighbors
#     arrayElements = []
#     frequencies = [0,0,0,0,0,0,0,0,0,0]
#     # for i in range(len(items)):
#     #     arrayElements[i] = items[0][1][i]
#
#     # arrayElements = items[0][1]
#
#     echo(arrayElements)
#
#     for i in range(len(items)):
#         arrayElements.append(items[i][1][0])
#
#
#     for i in range(len(arrayElements)):
#         digit = int(arrayElements[i])
#         echo(digit)
#         frequencies[digit]= frequencies[digit]+1
#
#     max = 0
#     idx = 0
#     for i in range(len(frequencies)):
#
#         if(max<frequencies[i]):
#             max = frequencies[i]
#             idx = i
#     return frequencies[idx]

# Returns the first closet neighbor
def getGuessedDigit(items):
    # Iterate over the neighbors
    arrayElements = []

    for i in range(len(items)):
        arrayElements.append(items[i][1][0])

    return arrayElements[0]

main()
