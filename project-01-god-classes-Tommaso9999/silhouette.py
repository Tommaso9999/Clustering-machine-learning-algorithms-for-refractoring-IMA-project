import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from ast import literal_eval
from sklearn.cluster import KMeans, AgglomerativeClustering
import os


featureVectorsCsvFiles=[r"feature_vectors_csv_files/CoreDocumentImpl.csv", r"feature_vectors_csv_files/DTDGrammar.csv", r"feature_vectors_csv_files/XIncludeHandler.csv", r"feature_vectors_csv_files/XSDHandler.csv"]


folder_name = 'k_means_best_k_clusters'
if not os.path.exists(folder_name):
   os.mkdir(folder_name)

folder_name_h = 'hierarchical_best_k_clusters'
if not os.path.exists(folder_name_h):
   os.mkdir(folder_name_h)



#Takes the files in Folder "k_means_csv_files" that have been produced with Kmeans Algorithm with k=2 (run k_means.py before)
#Computes and prints silhouette score for these clustering files. 

for element in featureVectorsCsvFiles:
 
  df = pd.read_csv(element)

  clusters=pd.read_csv("k_means_csv_files\Kmeans_results_with_k=2_"+os.path.basename(element)).iloc[: , 1:].values
  clusters2= np.ravel(clusters)

  X = df.drop(df.columns[[0, 1]], axis=1).reset_index(drop=True).values

  score = silhouette_score(X, clusters2)

 
  print("The silhouette score of "+os.path.basename(element)+   " k means clustering with k=2 is:", score)


#Applies Kmeans algorithm from k=2 ... k=60 printing the results. This code section only takes the feature vectors csv, therefore we need
#to compute the silhouette score every iteration for different k values. Results are printed and, lastly, the best k is printed for every 
#god class (the k that produces the highest silhouette score, therefore the best clustering according to this metric) then this clustering 
# solution is saved in k_means_best_k_clusters folder.

for elem in featureVectorsCsvFiles:
  df = pd.read_csv(elem)

  X = df.drop(df.columns[[0, 1]], axis=1).reset_index(drop=True).values

  silhouette_scores = []
  print("iterations for Kmeans of : "+os.path.basename(elem))

  for k in range(2, 61):
    
    kmeans = KMeans(n_clusters=k).fit(X)
    
    score = silhouette_score(X, np.ravel(kmeans.labels_))

    silhouette_scores.append(score)

    print(f"k means with k={k}, silhouette score={score}")

  best_k = silhouette_scores.index(max(silhouette_scores)) + 2
  print(f"Best k value for Kmeans clustering applied on " +os.path.basename(elem)+":"+ str(best_k))
  print("\n")

  clustering = KMeans(n_clusters=best_k).fit(X)

  df['cluster_id'] = clustering.labels_

  clusters = df.groupby('cluster_id')['method_name'].apply(list)
  clusters.to_csv(os.path.join(folder_name, "K_means_results_for_evaluation_phase_of_"+os.path.basename(elem)))






 
#Takes the files in the folder "Agglomerative_clustering_csv_files" obtained by running the "hierarcical.py" script. 
#each file stores agglomerative clustering results with k=2, those are then printed.

for element in featureVectorsCsvFiles:
 
  df = pd.read_csv(element)

  clusters=pd.read_csv("Agglomerative_clustering_csv_files\Agglomerative_clustering_results_with_k=2_"+os.path.basename(element)).iloc[: , 1:].values
  clusters2= np.ravel(clusters)



  X = df.drop(df.columns[[0, 1]], axis=1).reset_index(drop=True).values

  score = silhouette_score(X, clusters2)

 
  print("The silhouette score of "+os.path.basename(element)+   "with Agglomerative clustering with k=2 is:", score)

#Applies Agglomerative clustering algorithm from k=2 ... k=60 printing the results. This code section only takes the feature 
#vectors csv,therefore we need to compute the silhouette score every iteration for different k values. 
#Results are printed and, lastly, the best k is printed for every 
#god class (the k that produces the highest silhouette score, therefore the best clustering according to the metric used), then the
# best clusterings are saved in hierarchical_best_k_clusters folder.


for elem in featureVectorsCsvFiles:
 df = pd.read_csv(elem)

 X = df.drop(df.columns[[0, 1]], axis=1).reset_index(drop=True).values

 silhouette_scores = []
 print("iterations for agglomerative of: "+os.path.basename(elem))

 for k in range(2, 61):
    
   kmeans = AgglomerativeClustering(n_clusters=k).fit(X)
   
   score = silhouette_score(X, kmeans.labels_)

   silhouette_scores.append(score)

   print(f"Agglomerative with k={k}, silhouette score={score}")

   best_k = silhouette_scores.index(max(silhouette_scores)) + 2

 print(f"Best k value for Agglomerative clustering applied on" +os.path.basename(elem)+":"+ str({best_k}))
 print("\n")
 clustering = KMeans(n_clusters=best_k).fit(X)

 df['cluster_id'] = clustering.labels_


 clusters = df.groupby('cluster_id')['method_name'].apply(list)
 clusters.to_csv(os.path.join(folder_name_h, "Hierarchical_results_for_evaluation_phase_of_"+os.path.basename(elem)))

 

