import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = iris.data[:, :2]  # Use only the first two features for 2D visualization
# Initialize parameters
K = 4  # number of clusters
max_iters = 100
tol = 1e-4  # tolerance for centroid movement

# Step 1: Randomly initialize centroids
np.random.seed(42)
random_idx = np.random.permutation(data.shape[0])[:K]
centroids = data[random_idx]

def euclidean_distance(a, b):
    return np.linalg.norm(a - b)

# Function to assign points to the nearest centroid
def assign_clusters(data, centroids):
    clusters = []
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster = np.argmin(distances)
        clusters.append(cluster)
    return np.array(clusters)

# Function to update centroids
def update_centroids(data, clusters, K):
    new_centroids = []
    for k in range(K):
        cluster_points = data[clusters == k]
        if len(cluster_points) > 0:
            new_centroid = cluster_points.mean(axis=0)
        else:
            new_centroid = data[np.random.choice(data.shape[0])]
        new_centroids.append(new_centroid)
    return np.array(new_centroids)

# K-Means loop
for i in range(max_iters):
    clusters = assign_clusters(data, centroids)
    new_centroids = update_centroids(data, clusters, K)

    # Check convergence
    if np.all(np.abs(new_centroids - centroids) < tol):
        break
    centroids = new_centroids

# Plotting final clusters
plt.figure(figsize=(8, 6))
colors = ['red', 'green', 'blue', 'pink']
for k in range(K):
    cluster_points = data[clusters == k]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=colors[k], label=f'Cluster {k}')

plt.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='X', s=200, label='Centroids')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('K-Means Clustering from Scratch')
plt.legend()
plt.grid(True)
plt.show()
