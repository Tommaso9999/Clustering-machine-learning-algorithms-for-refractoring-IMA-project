import pandas as pd 
from sklearn.cluster import KMeans
import os
from sklearn.metrics import silhouette_score


FeatureVectorsCSVS=[r"feature_vectors_csv_files/CoreDocumentImpl.csv", r"feature_vectors_csv_files/DTDGrammar.csv", r"feature_vectors_csv_files/XIncludeHandler.csv", r"feature_vectors_csv_files/XSDHandler.csv"]

#This method applies k means clustering. It takes as an input the csv containing feature vectors and the desired k value. Beware that k means 
# algorithm has a random factor involved (the initial centroid choice is random) therefore results could vary sligthly for each run of the code.  

def apply_clustering(csv, k):
   
    df = pd.read_csv(csv)

   
    features = df.drop(df.columns[[0, 1]], axis=1).reset_index(drop=True).values

    clustering = KMeans(n_clusters=k).fit(features)
    
   
    df['cluster_id'] = clustering.labels_

    
    folder_name = 'k_means_csv_files'
    if not os.path.exists(folder_name):
     os.mkdir(folder_name)

    file_name = "Kmeans_results_with_k="+str(k)+"_" + os.path.basename(csv)
    file_path = os.path.join(folder_name, file_name)
    pd.DataFrame(clustering.labels_).to_csv(file_path)


    
    clusters = df.groupby('cluster_id')['method_name'].apply(list)

    clusters.to_csv(os.path.join(folder_name, "K_means_results_for_evaluation_phase_of_"+os.path.basename(csv)))

    print(csv +" Clusters with Kmeans with k="+str(k)+'\n')
    
    
    for cluster_id, methods in enumerate(clusters):
      print(f"Cluster {cluster_id}: {methods}")
      print('\n')
    

#Apply clustering to every god class with k=2 
for csv in FeatureVectorsCSVS:
    apply_clustering(csv, 2)
  