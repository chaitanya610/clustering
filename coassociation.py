from kmeans import euclidean_distance, squared_error
from kruskalsMST import MST
from collections import defaultdict
import pickle

def fill(i, graph, visited, k ,labels):
    if not visited[i]:
        visited[i] = True
        labels[i] = k
        for j in graph[i]:
            fill(j, graph, visited, k, labels)


def flood_fill(nodes, graph):
    labels = [-1]*nodes
    visited = [False]*nodes
    k = 0
    for i in range(nodes):
        if not visited[i]:
            fill(i, graph, visited, k, labels)
        k += 1

    return labels


def create_graph(mst):
    graph = defaultdict(list)
    for edge in mst:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

    return graph


def weight(i, j, df):
    return euclidean_distance(df.iloc[i].tolist(), df.iloc[j].tolist())


def get_matrix(partition1, centroids1, partition2, centroids2, df):
    n = df.shape[0]
    matrix = []
    for i in range(n):
        matrix.append([0 for j in range(i + 1, n)])

    v_index1 = squared_error(df, partition1, centroids1)
    v_index2 = squared_error(df, partition2, centroids2)
    for i in range(n):
        for j in range(i + 1, n):
            wt = weight(i, j, df)
            matrix[i][i + 1 - j] = ((int(partition1[i] != partition1[j]))*(wt*v_index1) + (int(partition2[i] != partition2[j]))*(wt*v_index2))/2

    return matrix


def ensemble(partition1, centroids1, partition2, centroids2, df, k):
    matrix = get_matrix(partition1, centroids1, partition2, centroids2, df)
    from openpyxl import Workbook

    wb = Workbook()
    ws = wb.active
    for row in matrix:
        ws.append(row)

    wb.save('matrix10.xlsx')
    nodes = df.shape[0]
    edges = []
    for i in range(nodes):
        for j in range(i + 1, nodes):
            if matrix[i][i + 1 - j]:
                edges.append([i, j, matrix[i][i + 1 - j]])

    mst, edges_removed = MST(nodes, edges)
    if edges_removed < k:
        mst = mst[:edges_removed - k]

    g = create_graph(mst)
    labels = flood_fill(nodes, g)
    return labels








