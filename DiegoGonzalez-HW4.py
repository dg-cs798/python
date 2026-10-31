import numpy as np
import time
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris_data = iris.data
iris_labels = iris.target

print("The length(rows) of dataset:", len(iris_data))

k_values = [1, 3, 5, 7, 9]
test_sizes = [10, 20, 30, 40]
#using one random order of the dataset
np.random.seed(int(time.time()))
indices = np.random.permutation(len(iris_data))
results = []

#running all 20 test cases
for test_size in test_sizes:
    learnset_data = iris_data[indices[:-test_size]]
    learnset_labels = iris_labels[indices[:-test_size]]
    testset_data = iris_data[indices[-test_size:]]
    testset_labels = iris_labels[indices[-test_size:]]

    for k in k_values:
        print("\nKNN TEST")
        print("Number of test samples:", test_size)
        print("k =", k)

        #trains the knn classifier
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(learnset_data, learnset_labels)
        predictions = knn.predict(testset_data)

        print("\nTarget values:")
        print(testset_labels)
        print("Predictions from the classifier:")
        print(predictions)

        #counting how many predictions were correct
        correct = 0
        for i in range(len(testset_labels)):
            if testset_labels[i] == predictions[i]:
                correct += 1
        percent_correct = (correct / test_size) * 100
        print("Correctly classified:", correct, "out of", test_size)
        print("Percent correct: %.2f%%" % percent_correct)
        results.append({
            "k": k,
            "test size": test_size,
            "percent correct": percent_correct
        })

#all of the test case results
print("\nALL KNN TEST RESULTS")
print("k\tTest Samples\tPercent Correct")
for result in results:
    print(
        result["k"],
        "\t",
        result["test size"],
        "\t\t",
        "%.2f%%" % result["percent correct"]
    )


#finding the best test case
best_percent = max(result["percent correct"] for result in results)
print("\nBest test case percentage: %.2f%%" % best_percent)
print("Best case(s):")
for result in results:
    if result["percent correct"] == best_percent:
        print(
            "k =",
            result["k"],
            ", test samples =",
            result["test size"]
        )


#average result for each k value
print("\nAVERAGE RESULT FOR EACH K")
best_average = 0
best_k = 0
for k in k_values:
    total = 0
    for result in results:
        if result["k"] == k:
            total += result["percent correct"]

    average = total / len(test_sizes)
    print("k =", k, "average percent correct: %.2f%%" % average)
    if average > best_average:
        best_average = average
        best_k = k

print("\nBest k value overall:", best_k)
print("Average percent correct: %.2f%%" % best_average)

#3d plot settings:
#using 2 k values and 2 test sample sizes for the representative plots
plot_k_values = [1, 5]
plot_test_sizes = [10, 30]
plot_columns = [
    (0, 1, 2),
    (0, 1, 3),
    (0, 2, 3),
    (1, 2, 3)
]
attribute_names = [
    "Sepal length",
    "Sepal width",
    "Petal length",
    "Petal width"
]
colors = ["r", "g", "y"]
test_colors = ["c", "m", "b"]
training_markers = ["o", "o", "o"]
test_markers = ["x", "x", "x"]
class_names = [
    "Iris-setosa",
    "Iris-versicolor",
    "Iris-virginica"
]
#creating the representative 3d plots
for test_size in plot_test_sizes:
    learnset_data = iris_data[indices[:-test_size]]
    learnset_labels = iris_labels[indices[:-test_size]]
    testset_data = iris_data[indices[-test_size:]]
    testset_labels = iris_labels[indices[-test_size:]]

    for k in plot_k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(learnset_data, learnset_labels)
        predictions = knn.predict(testset_data)

        for columns in plot_columns:
            first = columns[0]
            second = columns[1]
            third = columns[2]
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")

            #plotting the training data
            for iris_class in range(3):
                training_points = learnset_data[
                    learnset_labels == iris_class
                ]

                ax.scatter(
                    training_points[:, first],
                    training_points[:, second],
                    training_points[:, third],
                    c=colors[iris_class],
                    marker=training_markers[iris_class],
                    label="train " + class_names[iris_class]
                )

            #plotting the test data using the predicted classes
            for iris_class in range(3):
                test_points = testset_data[
                    predictions == iris_class
                ]
                ax.scatter(
                    test_points[:, first],
                    test_points[:, second],
                    test_points[:, third],
                    c=test_colors[iris_class],
                    marker=test_markers[iris_class],
                    label="test " + class_names[iris_class]
                )
            ax.set_xlabel(attribute_names[first])
            ax.set_ylabel(attribute_names[second])
            ax.set_zlabel(attribute_names[third])
            ax.set_title(
                "KNN Classification - k = "
                + str(k)
                + ", test samples = "
                + str(test_size)
                + ", columns"
                + str(first)
                + str(second)
                + str(third)
            )
            plt.legend(loc="upper left")
            plt.show()
