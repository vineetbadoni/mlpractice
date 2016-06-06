def main():
    filename = 'data/pima-indians-diabetes.csv'
    dataset = Util.loadCsv(filename)

    dataset = [[1], [2], [3], [4], [5]]
    splitRatio = 0.6
    train, test = Util.splitDataset(dataset, splitRatio)
    print('Split {0} rows into train with {1} and test with {2}').format(len(dataset), train, test)

    dataset = [[1, 20, 1], [2, 21, 0], [3, 22, 1]]
    separated = Util.separateByClass(dataset)
    print('Separated instances: {0}').format(separated)

    numbers = [1, 2, 3, 4, 5]
    print('Summary of {0}: mean={1}, stdev={2}').format(numbers, Util.mean(numbers), Util.stdev(numbers))

    dataset = [[1, 20, 0], [2, 21, 1], [3, 22, 0]]
    summary = Util.summarize(dataset)
    print('Attribute summaries: {0}').format(summary)

    dataset = [[1, 20, 1], [2, 21, 0], [3, 22, 1], [4, 22, 0]]
    summary = Util.summarizeByClass(dataset)
    print('Summary by class value: {0}').format(summary)

    x = 71.5
    mean = 73
    stdev = 6.2
    probability = Util.calculateProbability(x, mean, stdev)
    print('Probability of belonging to this class: {0}').format(probability)

    summaries = {0: [(1, 0.5)], 1: [(20, 5.0)]}
    inputVector = [1.1, '?']
    probabilities = Util.calculateClassProbabilities(summaries, inputVector)
    print('Probabilities for each class: {0}').format(probabilities)

    summaries = {'A': [(1, 0.5)], 'B': [(20, 5.0)]}
    inputVector = [1.1, '?']
    result = Util.predict(summaries, inputVector)
    print('Prediction: {0}').format(result)

    summaries = {'A': [(1, 0.5)], 'B': [(20, 5.0)]}
    testSet = [[1.1, '?'], [19.1, '?']]
    predictions = Util.getPredictions(summaries, testSet)
    print('Predictions: {0}').format(predictions)

    testSet = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
    predictions = ['a', 'a', 'a']
    accuracy = Util.getAccuracy(testSet, predictions)
    print('Accuracy: {0}').format(accuracy)


main()
