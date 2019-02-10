import random


def euclidean_distance(point, centroid):
    distance = 0
    for i in range(len(point)):
        distance += (centroid[i] - point[i])**2

    return distance**0.5


def get_initial_membership(data, c):
    data_size = len(data)
    membership_matrix = []
    for i in range(data_size):
        temp = []
        for j in range(c):
            temp.append(random.randint(1, data_size))
            temp = [t/sum(temp) for t in temp]
        membership_matrix.append(temp)

    return membership_matrix


def membership(data, centroids, i, j, c, m):
    s = 0
    distance = euclidean_distance(data[i], centroids[j])
    for k in range(c):
        s += (distance/euclidean_distance(data[i], centroids[k]))**(2/m - 1)
    return 1/s


def get_membership_matrix(data, centroids, c, m):
    data_size = len(data)
    membership_matrix = []
    for i in range(data_size):
        temp = []
        for j in range(c):
            temp.append(membership(data, centroids, i, j, c, m))
        membership_matrix.append(temp)
    return membership_matrix


def get_centroids(data, membership_matrix, c, m):
    n = len(data)
    centroids = []
    for j in range(c):
        temp = []
        for k in range(len(data[0])):
            s1 = 0
            s2 = 0
            for i in range(n):
                s1 += (membership_matrix[i][j]**m)*data[i][k]
                s2 += membership_matrix[i][j]**m
            temp.append(s1/s2)
        centroids.append(temp)

    return centroids


def calculate_error(data, centroids, membership_matrix, c, m):
    n = len(data)
    error = 0
    for i in range(n):
        for j in range(c):
            error += (membership_matrix[i][j]**m)*(euclidean_distance(data[i], centroids[j])**2)
    return error


def difference(A, B, c):
    result = []
    for i  in range(len(A)):
        temp = []
        for j in range(c):
            temp.append(abs(A[i][j] - B[i][j]))
        result.append(temp)
    return result


def fuzzy_c_means(data, c):
    m = 3
    new_membership_matrix = get_initial_membership(data, c)
    new_f_centers = get_centroids(data, new_membership_matrix, c, m)
    print(new_f_centers)
    J = calculate_error(data, new_f_centers, new_membership_matrix, c, m)
    old_J = float("inf")
    membership_matrix = None
    f_centers = None
    while J < old_J:
        membership_matrix = new_membership_matrix
        f_centers = new_f_centers
        old_J = J
        new_membership_matrix = get_membership_matrix(data, f_centers, c, m)
        new_f_centers = get_centroids(data, new_membership_matrix, c, m)
        J = calculate_error(data, new_f_centers, new_membership_matrix, c, m)
        diff = difference(new_membership_matrix, membership_matrix, c)
        if max(diff[i][j] for j in range(c) for i in range(len(data))) < 0.001:
            break

    cluster_labels = []
    for i in range(len(data)):
        cluster_labels.append(max(list(enumerate(membership_matrix[i])), key=lambda x: x[1])[0])

    return cluster_labels, f_centers

l = [[1660,1232,721,23,52,2885,537,7440,3300,450,2200,70,78,18.1,12,7041,60],
     [2186,1924,512,16,29,2683,1227,12280,6450,750,1500,29,30,12.2,16,10527,56],
     [1428,1097,336,22,50,1036,99,11250,3750,400,1165,53,66,12.9,30,8735,54],
     [417,349,137,60,89,510,63,12960,5450,450,875,92,97,7.7,37,19016,59],
     [193,146,55,16,44,249,869,7560,4120,800,1500,76,72,11.9,2,10922,15],
     [587,479,158,38,62,678,41,13500,3335,500,675,67,73,9.4,11,9727,55],
     [353,340,103,17,45,416,230,13290,5720,500,1500,90,93,11.5,26,8861,63],
     [1899,1720,489,37,68,1594,32,13868,4826,450,850,89,100,13.7,37,11487,73],
     [1038,839,227,30,63,973,306,15595,4400,300,500,79,84,11.3,23,11644,80],
     [582,498,172,21,44,799,78,10468,3380,660,1800,40,41,11.5,15,8991,52],
     [1732,1425,472,37,75,1830,110,16548,5406,500,600,82,88,11.3,31,10932,73],
     [2652,1900,484,44,77,1707,44,17080,4440,400,600,73,91,9.9,41,11711,76],
     [1179,780,290,38,64,1130,638,9690,4785,600,1000,60,84,13.3,21,7940,74],
     [1267,1080,385,44,73,1306,28,12572,4552,400,400,79,87,15.3,32,9305,68],
     [494,313,157,23,46,1317,1235,8352,3640,650,2449,36,69,11.1,26,8127,55],
     [1420,1093,220,9,22,1018,287,8700,4780,450,1400,78,84,14.7,19,7355,69]]
import pandas as pd
from collections import defaultdict
df=pd.read_csv('data.csv')
l=df.values.tolist()

labels, c = fuzzy_c_means(l, 3)
cluster_dict= defaultdict(list)

for i in range(len(labels)):
    cluster_dict[labels[i]].append(l[i])
for k,v in cluster_dict.items():
    print("cluster",k)
    print(*v,sep='\n')

