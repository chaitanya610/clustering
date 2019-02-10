import random


def euclidean_distance(point, centroid):
    distance = 0
    for i in range(len(point)):
        distance += (centroid[i] - point[i])**2

    return distance


def get_initial_centroids(data, n_clusters, data_size):
    centroids = []
    index = []
    i = 0
    while i < n_clusters:
        r = random.randint(0, data_size)
        if r not in index:
            centroids.append(data.iloc[r].tolist())
            index.append(r)
            i += 1

    return centroids


def add(total, row):
    for i in range(len(row)):
        total[i] += row[i]


def calculate_centroids(data, cols, clusters, n):
    total = dict()
    for i in range(n):
        total[i] = [0 for _ in range(cols)]
    count = [0]*n
    for row in data.iterrows():
        index, values = row
        add(total[clusters[index]], values.tolist())
        count[clusters[index]] += 1

    return [[total[i][j]/count[i] for j in range(cols)] for i in range(n)]


def get_nearest_cluster(point, centroids):
    min_distance = float("inf")
    closest_cluster = -1
    i = 0
    for centroid in centroids:
        distance = euclidean_distance(point, centroid)
        if distance < min_distance:
            min_distance = distance
            closest_cluster = i
        i += 1

    return closest_cluster


def get_clusters(data, rows, centroids):
    clusters = [-1 for _ in range(rows)]
    for row in data.iterrows():
        index, values = row
        cluster_no = get_nearest_cluster(values.tolist(), centroids)
        clusters[index] = cluster_no

    return clusters


def KMeans(data, n_clusters):
    data_size = data.shape[0]
    feature_size = data.shape[1]
    centroids = get_initial_centroids(data, n_clusters, data_size)
    change = True
    iterations = 0
    clusters = []
    while change and iterations < 1000:
        old_centroids = centroids.copy()
        clusters = get_clusters(data, data_size, centroids)
        centroids = calculate_centroids(data, feature_size, clusters, n_clusters)
        if old_centroids == centroids:
            change = False
        iterations += 1
    return clusters, centroids


def squared_error(data, cluster_labels, centroids):
    error = 0
    for row in data.iterrows():
        index, values = row
        error += euclidean_distance(values.tolist(), centroids[cluster_labels[index]])**0.5

    return error
