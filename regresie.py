from math import sqrt


def evalErrorL1(realOutputs, computedOutputs):
    noSamples = len(realOutputs)
    noTargets = len(realOutputs[0])
    valSum = 0

    # compute the error
    for i in range(0, noSamples):
        for j in range(0, noTargets):
            # compute abs(real - computed) for each target and then add it to the totalSum
            valSum += abs(realOutputs[i][j] - computedOutputs[i][j])

    errorPrediction = (1 / noSamples) * valSum
    return errorPrediction


def evalErrorL2(realOutputs, computedOutputs):
    noSamples = len(realOutputs)
    noTargets = len(realOutputs[0])

    valSum = 0
    for i in range(0, noSamples):
        optSum = 0
        for j in range(0, noTargets):
            optSum += abs(realOutputs[i][j] - computedOutputs[i][j])
        valSum += optSum ** 2
    errorPrediction = sqrt((1 / noSamples) * valSum)
    return errorPrediction


def main():
    # realOutputs = [[5, 3.1], [6, 5.5], [4.8, 5], [4.4, 2.3]]
    # computedOutputs = [[7, 3.3], [5.7, 4.5], [4.9, 4.7], [4.2, 2.5]]
    # realOutputs = [[7.7, 8.9, 8.5, 7.5], [6.3, 7.6, 7.9, 8.8], [6.1, 8, 7.9, 8], [8, 7.9, 7.7, 8.3],
    # [6.9, 8, 7, 7]]
    # computedOutputs = [[7, 8.4, 8.2, 7], [6.9, 7.3, 7, 7.2], [5.5, 8.7, 8.3, 8.5], [8.5, 7.3, 7.3,
    # 8], [7.2, 7.8, 6.7, 6.6]]
    realOutputs = [[5, 3.1, 5.5, 7.8], [6, 5.5, 9, 10], [4.8, 5, 4.7, 8.3], [4.4, 2.3, 6.6, 7.6], [7.1, 5.4, 7.9, 9],
                   [4, 2.3, 5.6, 7.8], [6.1, 8, 7.9, 8], [8, 7.9, 7.7, 8.3], [6.9, 8, 7, 7]]
    computedOutputs = [[5.2, 3.1, 5.4, 7.9], [6.3, 5.5, 9, 10.2], [4.9, 5.3, 5, 8.2], [4.4, 2.3, 6.7, 7.9],
                       [6.8, 5, 8, 9.1],
                       [4, 2.4, 5.8, 7.8], [5.7, 6.7, 8, 8.1], [8.3, 7.5, 7.5, 8.1], [6.3, 8.2, 7.7, 7.6]]
    # realOutputs = [[1, 2, 2.3, 2, 4, 5], [3, 2, 3.2, 4, 5], [1, 1.1, 2.3, 2, 1.6], [3.4, 5.6, 2.5, 2, 4]]
    # computedOutputs = [[1, 2, 2.3, 2, 4, 5], [5, 4, 3.2, 4, 5], [1, 6, 2.3, 2, 1.6], [6.2, 5.6, 2.5, 2, 4]]

    print("Error (L1) : " + str(evalErrorL1(realOutputs, computedOutputs)))
    print("Error (L2) : " + str(evalErrorL2(realOutputs, computedOutputs)))



main()
