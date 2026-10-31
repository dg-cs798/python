import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

df = pd.read_excel("iris1.xlsx")
x = np.array(df.iloc[:, 0:4])
attributes = list(df.columns[0:4])
print("The length(rows) of dataset:", len(df))

#all the different pairs of the 4 attributes
attribute_pairs = [
    (0, 1),
    (0, 2),
    (0, 3),
    (1, 2),
    (1, 3),
    (2, 3)
]

silhouette_results = []

#k-means with k 2-6
for k in range(2, 7):
    print("\nK-MEANS with", k, "CLUSTERS")
    kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
    kmeans.fit(x)
    print(kmeans)
    print("\nThe cluster centroids:")
    print(kmeans.cluster_centers_)
    print("\nThe sample clusters")
    print(kmeans.labels_)

    score = silhouette_score(x, kmeans.labels_)

    print("\nThe silhouette score: %.4f" % score)
    silhouette_results.append({
        "k value": k,
        "Silhouette coefficient": score
    })

    #creating a graph for each pair of atributes
    for pair in attribute_pairs:
        first_column = pair[0]
        second_column = pair[1]

        plt.figure()

        plt.scatter(
            x[:, first_column],
            x[:, second_column],
            c=kmeans.labels_
        )

        #cluster centroids
        plt.scatter(
            kmeans.cluster_centers_[:, first_column],
            kmeans.cluster_centers_[:, second_column],
            marker="x",
            s=100,
            label="Centroids"
        )
        plt.xlabel(attributes[first_column])
        plt.ylabel(attributes[second_column])
        plt.title(
            "K-means clustering with k ="
            + str(k)
            + " - "
            + attributes[first_column]
            + " vs "
            + attributes[second_column]
        )
        plt.legend()
        plt.show()


silhouette_table = pd.DataFrame(silhouette_results)

print("\nSilhouette Coefficient Results:")
print(silhouette_table)
best_run = silhouette_table.loc[
    silhouette_table["Silhouette coefficient"].idxmax()
]
print("\nBest k value from silhouette coefficient", int(best_run["k value"]))
print(
    "Best silhouette coefficient: %.4f"
    % best_run["Silhouette coefficient"]
)


#elbow method
k_values = range(1, 11)
mean_distortions = []

for k in k_values:

    kmeans = KMeans(n_clusters=k, random_state=0, n_init=10)
    kmeans.fit(x)

    distances = cdist(
        x,
        kmeans.cluster_centers_,
        "euclidean"
    )

    mean_distortion = (
        sum(np.min(distances, axis=1)) / x.shape[0]
    )

    mean_distortions.append(mean_distortion)

#plotting
plt.figure()
plt.plot(k_values, mean_distortions, "bx-")
plt.xlabel("k")
plt.ylabel("Average distortion")
plt.title("Selecting k with the Elbow Method for iris dataset")
plt.xticks(range(1, 11))
plt.show()
