import csv
from collections import Counter

# Euclidean Method
def Euclidean(x1, x2):
    L2 = 0
    for i in range(len(x1)):
        L2 += (x1[i] - x2[i]) ** 2
    return L2 ** 0.5

# Manhattan Method
def Manhattan(x1, x2):
    L1 = 0
    for i in range(len(x1)):
        L1 += abs(x1[i] - x2[i])
    return L1

# Find the mode of Label
def most_label(results):
    most = Counter(results)
    return (most.most_common(1))[0][0]

# KNN
def KNN(X1, Y1, X2, Y2, k, L):
    # Results of labels
    results = []

    for i in range(len(X2)):
        E_dist = []
        label1 = []
        for j in range(len(X1)):

            # Calculate the distance between two points
            if L == 'L2':
                E_dist.append([Euclidean(X1[j], X2[i]), Y1[j]])
            elif L == 'L1':
                E_dist.append([Manhattan(X1[j], X2[i]), Y1[j]])

        # Sort the distance to find the nearest point
        E_dist.sort(key=lambda x: x[0])

        # Find the points in range of K
        for t in range(0, k):
            label1.append(E_dist[t][1])

            # Find the mode of labels
        label = most_label(label1)

        # Save the labels to compare
        results.append(label)

    # Count the number of correct labels
    count = 0
    for i in range(len(Y2)):
        if results[i] == Y2[i]:
            count = count + 1

    if L == 'L2':
        print('L2) Euclidean Method, K is', k, '\tThe Accuracy is', count, "% \tThe number of test cases is", len(Y2))
    elif L == 'L1':
        print('L1) Manhattan Method, K is', k, '\tThe Accuracy is', count, "% \tThe number of test cases is", len(Y2))

def main():
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []

    with open("train.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            X1.append(row[1:])
            Y1.append(int(row[0]))

    with open("test.csv") as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            X2.append(row[1:])
            Y2.append(int(row[0]))

    # Manhattan Method
    for i in range(1, 10, 2):
        KNN(X1, Y1, X2, Y2, i, 'L1')

    print()

    # Euclidean Method
    for i in range(1, 10, 2):
        KNN(X1, Y1, X2, Y2, i, 'L2')

main()