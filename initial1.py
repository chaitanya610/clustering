from kmeans import get_initial_centroids
import pandas as pd
file_name = input("Enter the filename: ").strip()
n = int(input("Enter the number of clusters: ").strip())
df = pd.read_csv(file_name)
df.drop('Unnamed: 0', axis=1, inplace=True)
ic=get_initial_centroids(df,n,df.shape[0])
print (*ic,sep='\n')