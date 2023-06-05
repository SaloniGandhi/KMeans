# K-means
import sklearn.cluster
from matplotlib.pyplot import plot as plt

Ks, objectives = range(1,11), []

for k in Ks:
    model = cluster.Kmeans(n_clusters=k)
    model.fit(x)
    objectives.append(-model.score(x))


plt.plot(Ks,objectives,'.-',markersize=15)
plt.scatter([4], [objectives[3]],s=200,c='r')
plt.xlabel("Number of clusters K")
plt.ylabel("Objective function value")

# ``` 
# Algorithm
# For a given dataset, k is specified to be the number of distinct groups the points belong to. These k centroids are first randomly initialized, then iterations are performed to optimize the locations of these k centroids as follows:

# The distance from each point to each centroid is calculated.
# Points are assigned to their nearest centroid.
# Centroids are shifted to be the average value of the points belonging to it. If the centroids did not move, the algorithm is finished, else repeat.```
