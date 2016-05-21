import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import csv

def loadData(fileName):
    with open(fileName, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)

        return dataset

def main():
        # dataset = loadData("data.txt")  # Transposed for easier unpacking
        # print len(dataset[0])
        # results = [int(i) for i in dataset[1]]

        dataset = loadData('test.csv')
        print len(dataset[1])
        print dataset[1]

        nrows, ncols = 28, 28

        drawPixels(dataset[2],nrows,ncols)


def drawPixels(pixelsList,nRows,nCols):
    # grid = np.asarray(dataset[2]).reshape((nrows, ncols))
    # print len(pixelsList)
    grid = np.asarray(pixelsList).reshape((nRows, nCols))
    grid = grid.astype(int)
    # print grid
    plt.imshow(grid, origin='lower');
    plt.show()

# main()
