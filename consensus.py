import pickle
import pandas as pd
from coassociation import ensemble
from collections import defaultdict
file_name = input("Enter the labels filename(with extension '.p'): ").strip()
with open(file_name, 'rb') as fp:
    labels = pickle.load(fp)

file_name = input("Enter the dataset filename: ").strip()
df = pd.read_csv(file_name)

candidate_solutions = []
with open('cent.p', 'rb') as fp:
    centroids = pickle.load(fp)

k = len(labels)

'''for i in range(k):
    for j in range(i + 1, k):
        candidate_solutions.append(ensemble(labels[i], centroids[i], labels[j], centroids[j], df, k))'''

ensemble_labels = ensemble(labels[0], centroids[0], labels[1], centroids[1], df, k)

'''from openpyxl import Workbook

wb = Workbook()
ws = wb.active
for row in matrix:s
    ws.append(row)

wb.save('matrix.xlsx')'''

'''print(labels[0])
print(labels[1])
print(ensemble_labels)'''
cluster_dict= defaultdict(list)

for i in range(len(ensemble_labels)):
    cluster_dict[ensemble_labels[i]].append(df.iloc[i].tolist())
i=0
for k,v in cluster_dict.items():
    print("cluster",i)
    print(*v,sep='\n')
    i+=1
