from kmeans import KMeans
import pandas as pd
import pickle

file_name = input("Enter the filename: ").strip()
n = int(input("Enter the number of clusters: ").strip())
df = pd.read_csv(file_name)
df.drop('Unnamed: 0', axis=1, inplace=True)
cluster_labels = []
centroids = []
for i in range(n):
    temp_labels, temp_centroids = KMeans(df.drop('Private', axis=1), n)
    cluster_labels.append(temp_labels)
    print("IS:", i)
    print(temp_labels)
    centroids.append(temp_centroids)

file_name = input("Enter the filename to store labels(with extension '.p'): ").strip()
with open(file_name, 'wb') as fp:
    pickle.dump(cluster_labels, fp)

centroid_file = 'cent.p'

with open(centroid_file, 'wb') as fp:
    pickle.dump(centroids, fp)















'''clusters = dict()
for i in range(n):
    clusters[i] = []
for row in df.iterrows():
    index, values = row
    clusters[cluster_labels[index]].append(values.tolist())
for i in range(n):
    print("\nCluster ", i + 1)
    print(*clusters[i], sep = "\n")
    print(centroids[i])
print("\nSquared Error: ", squared_error(df.drop('Private', axis = 1), cluster_labels, centroids))'''
