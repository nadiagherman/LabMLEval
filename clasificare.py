def get_precision_and_recall(realOutputs, computedOutputs, pos, neg):
    # computes the True Positive, False Positive, False Negative, True Negative values
    # pos = positive class, neg = a list with the rest of the classes(labels), all considered negative

    TP = sum([1 if (realOutputs[i] == pos and computedOutputs[i] == pos) else 0 for i in range(len(realOutputs))])
    FP = sum([1 if (realOutputs[i] in neg and computedOutputs[i] == pos) else 0 for i in range(len(realOutputs))])
    FN = sum([1 if (realOutputs[i] == pos and computedOutputs[i] in neg) else 0 for i in range(len(realOutputs))])
    # TN = sum([1 if (realOutputs[i] in neg and computedOutputs[i] in neg) else 0 for i in range(len(realOutputs))])

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)

    return precision, recall


def evalClassification(realOutputs, computedOutputs, labels):
    precisions = {}
    recalls = {}

    # accuracy = nr of outputs computed correctly / nr of outputs
    accuracy = sum([1 if (realOutputs[i] == computedOutputs[i]) else 0 for i in range(len(realOutputs))]) / len(
        realOutputs)

    for label in labels:
        # we compute the precision and recall for each class(label)
        # take each label and consider it positive
        # all other labels are considered negative
        # store precision and recall values for each label in two dictionaries

        copy_labels = labels.copy()
        copy_labels.remove(label)
        precision, recall = get_precision_and_recall(realOutputs, computedOutputs, label, copy_labels)
        precisions[label] = precision
        recalls[label] = recall

    return accuracy, precisions, recalls


def main():
    # realOutputs = ['banana', 'apple', 'apple', 'peach', 'grapes', 'apple', 'grapes', 'banana', 'banana']
    # computedOutputs = ['apple', 'banana', 'apple', 'peach', 'apple', 'apple', 'grapes', 'banana', 'peach']
    # realOutputs = ['apple', 'banana', 'peach', 'peach', 'banana', 'banana', 'peach', 'banana', 'peach', 'peach',
    #               'banana', 'apple']
    # computedOutputs = ['apple', 'peach', 'peach', 'apple', 'banana', 'banana', 'peach', 'banana', 'banana', 'peach',
    #                   'apple', 'apple']
    # realOutputs = ['red', 'red', 'blue', 'blue', 'yellow', 'red', 'yellow', 'yellow', 'blue', 'red', 'blue',
    #              'yellow', 'red', 'red', 'yellow', 'blue']
    # computedOutputs = ['red', 'blue', 'blue', 'blue', 'red', 'red', 'yellow', 'yellow', 'blue', 'yellow', 'blue',
    #                 'red', 'blue', 'red', 'yellow', 'red']
    # realOutputs = ['green', 'red', 'red', 'green', 'blue', 'blue', 'yellow', 'red', 'yellow', 'yellow', 'green',
    #               'blue', 'red', 'blue', 'yellow', 'red', 'green', 'red', 'yellow', 'blue']
    # computedOutputs = ['green', 'red', 'blue', 'yellow', 'blue', 'blue', 'green', 'red', 'yellow', 'yellow',
    #                   'green', 'blue', 'yellow', 'blue', 'green', 'blue', 'red', 'red', 'yellow', 'red']
    # realOutputs = ['red', 'red', 'blue', 'blue', 'green', 'blue', 'green', 'blue', 'blue', 'blue', 'blue',
    #               'blue', 'blue', 'blue']
    # computedOutputs = ['red', 'red', 'green', 'blue', 'red', 'blue', 'green', 'blue', 'blue', 'red', 'blue',
    #                   'blue', 'green', 'blue']

    realOutputs = ['banana', 'apple', 'apple', 'peach', 'apple', 'peach', 'banana', 'banana', 'peach']
    computedOutputsProb = [[0.3, 0.5, 0.2], [0.6, 0.1, 0.3], [0.3, 0.5, 0.2], [0.2, 0.2, 0.6], [0.5, 0.1, 0.4],
                           [0.1, 0.3, 0.6], [0.7, 0.1, 0.2], [0.2, 0.4, 0.4], [0.1, 0.2, 0.7]]

    labels = ['apple', 'banana', 'peach']

    computedOutputs = []
    for output in computedOutputsProb:
        probMaxPos = output.index(max(output))
        label = labels[probMaxPos]
        computedOutputs.append(label)

    print("labels are : " + str(labels))
    acc, prec, rec = evalClassification(realOutputs, computedOutputs, ['apple', 'banana', 'peach'])
    print("acc: " + str(acc) + '\n' + "precisions: " + str(prec) + '\n' + "recalls: " + str(rec) + '\n')


main()
