import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("iris.xlsx")

print(df.head(10))
print("\nRow 0:")
print(df.iloc[0])
print("\nColumn 0:")
print(df.iloc[:, 0])
print("\nCell at row 0, column 0:")
print(df.iloc[0, 0])

row_number = int(input("\nEnter the row (range 0 - 149) of the data: "))
column_number = int(input("Enter the column (range 0 - 4) of the data: "))
print("\nThe data at row", row_number, "and column", column_number, "is:")
print(df.iloc[row_number, column_number])

modified_data = df.copy()

#replacing 3.3 with 999, and counting the amount of times it occurs
count = 0
for row in range(len(modified_data)):
    for column in range(len(modified_data.columns)):
        if modified_data.iloc[row, column] == 3.3:
            count += 1
            print(count, "A value 3.3 is found at row", row, "and column", column)
            modified_data.iloc[row, column] = 999
            print("The value 3.3 is changed to 999")
print("\nTotal", count, "of 3.3 found in the dataset")

#save data into a new file
modified_data.to_excel("modified_iris.xlsx", index=False)
print("\nModified dataset saved as modified_iris.xlsx")

#getting all the math values for each species
species_groups = df.groupby("Species")
for species, group in species_groups:
    print("\nSpecies:", species)
    print("\nMean:")
    print(group.iloc[:, 0:4].mean())
    print("\nMedian:")
    print(group.iloc[:, 0:4].median())
    print("\nStandard Deviation:")
    print(group.iloc[:, 0:4].std())
    print("\nVariance:")
    print(group.iloc[:, 0:4].var())
    print("\nCorelation:")
    print(group.iloc[:, 0:4].corr())

# finding the 5 smallst/largest values
for column in df.columns[0:4]:
    print("\nColumn:", column)
    smallest = df.nsmallest(5, column)
    print("\n5 Minimum Values:")
    for index, row in smallest.iterrows():
        print(row[column], "-", row["Species"])
    largest = df.nlargest(5, column)
    print("\n5 Maximum Values:")
    for index, row in largest.iterrows():
        print(row[column], "-", row["Species"])

#all the 6 graph combinations using the first 4 columns
attributes = df.columns[0:4]
markers = ["o", "s", "^"]
for i in range(len(attributes)):
    for j in range(i + 1, len(attributes)):
        plt.figure()
        for marker, species in zip(markers, df["Species"].unique()):
            species_data = df[df["Species"] == species]
            plt.scatter(
                species_data[attributes[i]],
                species_data[attributes[j]],
                marker=marker,
                label=species
            )
        plt.xlabel(attributes[i])
        plt.ylabel(attributes[j])  
        plt.title(attributes[i] + " vs " + attributes[j])
        plt.legend()
        plt.show()


