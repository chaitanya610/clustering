import pandas as pd
from openpyxl import load_workbook
from kruskalsMST import MST
from coassociation import create_graph, flood_fill
import networkx as nx
import pickle
import matplotlib.pyplot as plt

wb = load_workbook('matrix10.xlsx')
ws = wb.active
matrix = []
for row in ws:
    t = []
    for cell in row:
        t.append(cell.value)
    matrix.append(t)

nodes = len(matrix)
edges = []
for i in range(nodes):
    for j in range(i + 1, nodes):
        if matrix[i][i + 1 - j]:
            edges.append([i, j, matrix[i][i + 1 - j]])

k = 10
mst, edges_removed = MST(nodes, edges)
if edges_removed < k:
    mst = mst[:edges_removed - k + 1]
print(nodes)
'''with open('mst10.p', 'rb') as fp:
    mst = pickle.load(fp)'''
G=nx.Graph()
nodes_list = list(range(nodes))
G.add_nodes_from(nodes_list)
G.add_edges_from(mst)
nx.draw(G)
plt.savefig("simple_path10.png") # save as png
plt.show()
'''g = create_graph(mst)
labels = flood_fill(nodes, g)
print(labels)'''



