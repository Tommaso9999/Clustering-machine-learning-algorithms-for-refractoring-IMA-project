import pandas as pd 
from sklearn.cluster import AgglomerativeClustering
import os
from sklearn.metrics import silhouette_score


FeatureVectorsCSVS=[r"feature_vectors_csv_files/CoreDocumentImpl.csv", r"feature_vectors_csv_files/DTDGrammar.csv", r"feature_vectors_csv_files/XIncludeHandler.csv", r"feature_vectors_csv_files/XSDHandler.csv"]

#This method applies Agglomerative clustering. It takes as an input the csv file containing feature vectors and the desired k value. 

def apply_clustering(csv, k):
   
    df = pd.read_csv(csv)


    features = df.drop(['method_name'], axis=1).reset_index(drop=True).values

    clustering = AgglomerativeClustering(n_clusters=k)
    
 
    cluster_labels = clustering.fit_predict(features)

   
    df['cluster_id'] = cluster_labels

    
    folder_name = 'Agglomerative_clustering_csv_files'
    if not os.path.exists(folder_name):
     os.mkdir(folder_name)

    file_name = "Agglomerative_clustering_results_with_k="+str(k)+"_" +os.path.basename(csv)
    file_path = os.path.join(folder_name, file_name)
    pd.DataFrame(cluster_labels).to_csv(file_path)


   
    clusters = df.groupby('cluster_id')['method_name'].apply(list)
    

    clusters.to_csv(os.path.join(folder_name, "Agglomerative_Clustering_results_for_evaluation_phase_of_"+os.path.basename(csv)))

    print(csv +" Clusters with Agglomerative clustering with k="+str(k)+'\n')
    
    for cluster_id, methods in clusters.iteritems():
      print(f"Cluster {cluster_id}: {methods}")
      print('\n')
    
#apply clustering for every god class and k=2
for csv in FeatureVectorsCSVS:
    apply_clustering(csv, 2)