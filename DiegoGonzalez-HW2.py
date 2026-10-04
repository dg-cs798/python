import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

#linear regression section
print("LINEAR REGRESSION")
linear_scores = []
linear_runs = []
while True:

    #getting the sheet that will be tested
    sheet_number = int(input("\nEnter the sheet number (1 - 4): "))
    sheet_name = "Sheet" + str(sheet_number)
    df = pd.read_excel("iris.xlsx", sheet_name=sheet_name)
    print("\nLength(rows) of dataset:", len(df))
    print("\nColumns that can be used for training:")
    print("0 - Sepal length")
    print("1 - Sepal width")
    print("2 - Petal length")
    print("Target column:")
    print("3 - Petal width")
    #getting which columns will be used to predict petal width
    column_input = input(
        "Enter the training columns separated by commas (example 0,1,2): "
    )
    column_numbers = []
    for column in column_input.split(","):
        column_numbers.append(int(column))

    test_size = float(input("Enter the test size (example .25): "))
    x = np.array(df.iloc[:, column_numbers])
    y = np.array(df.iloc[:, 3])

    print("\nCorrelation values:")
    print(df.iloc[:, 0:4].corr())

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size
    )

    #training the linear regression model
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    y_predictions = lr.predict(x_test)

    print("\nSheet used:", sheet_name)
    print("Training columns:", column_input)
    print("Test size:", test_size)

    print("\ny_test\t\ty_prediction")

    for i in range(len(y_predictions)):
        print(
            i,
            "\t",
            round(y_test[i], 2),
            "\t\t",
            round(y_predictions[i], 2)
        )

    score = lr.score(x_test, y_test)

    print("\nR-squared: %.4f" % score)

    linear_scores.append(score)

    #saving the information from each run
    linear_runs.append({
        "Sheet": sheet_number,
        "Training Columns": column_input,
        "Test Size": test_size,
        "R-squared": score
    })

    another_run = input("\nDo another linear regression run? (y/n): ")

    if another_run.lower() == "n":
        break

linear_table = pd.DataFrame(linear_runs)
print("\nLinear Regression Runs:")
print(linear_table)

#finds the math values for the r-squared results
print("\nLinear Regression R-squared Results:")
print("Maximum:", max(linear_scores))
print("Minimum:", min(linear_scores))
print("Mean:", np.mean(linear_scores))
print("Variance:", np.var(linear_scores))
print("\n\nLOGISTIC REGRESSION")

df = pd.read_excel("iris.xlsx", sheet_name="Sheet1")
logistic_scores = []
logistic_runs = []
print("\nLength(rows) of dataset:", len(df))
while True:
    print("\nColumns that can be used for training:")
    print("0 - Sepal length")
    print("1 - Sepal width")
    print("2 - Petal length")
    print("3 - Petal width")
    print("Target column:")
    print("4 - Species")
    #getting which columns will be used to predict the species
    column_input = input(
        "Enter the training columns separated by commas (example 0,1,2,3): "
    )
    column_numbers = []

    for column in column_input.split(","):
        column_numbers.append(int(column))
    #getting the test size
    test_size = float(input("Enter the test size (example .25): "))

    x = np.array(df.iloc[:, column_numbers])
    y = np.array(df["Species"])
    #splitting the data into training and testing data
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size
    )

    lr = LogisticRegression(max_iter=200)
    lr.fit(x_train, y_train)
    y_predictions = lr.predict(x_test)
    print("\nTraining columns:", column_input)
    print("Test size:", test_size)
    print("\ny_test\t\t\ty_prediction")

    for i in range(len(y_predictions)):
        print(
            i,
            "\t",
            y_test[i],
            "\t",
            y_predictions[i]
        )
    score = lr.score(x_test, y_test)
    print("\nR-squared: %.4f" % score)
    logistic_scores.append(score)
    logistic_runs.append({
        "Training Columns": column_input,
        "Test Size": test_size,
        "R-squared": score
    })

    another_run = input("\nDo another logistic regression run? (y/n): ")

    if another_run.lower() == "n":
        break

logistic_table = pd.DataFrame(logistic_runs)

print("\nLogistic Regression Runs:")
print(logistic_table)

#finding all the math vals for the logistic regression results
print("\nLogistic Regression R-squared Results:")
print("Maximum:", max(logistic_scores))
print("Minimum:", min(logistic_scores))
print("Mean:", np.mean(logistic_scores))
print("Variance:", np.var(logistic_scores))