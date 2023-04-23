import csv
import pandas as pd 
import ast
from itertools import combinations



GodClasses = ['CoreDocumentImpl.csv', 'DTDGrammar.csv', 'XIncludeHandler.csv', 'XSDHandler.csv']



def str_to_set(s):
    return set(ast.literal_eval(s))

#code section to compute precision and recall for k means best k clustering results. I used the intra pairs formula as we are using 
#precision and recall to asses the quality of a clustering solution. 

for Gclass in GodClasses:

 dfground = pd.DataFrame

 with open('ground_truth_csv_files/'+Gclass, 'r') as csvfile:
    dfground = pd.read_csv(csvfile)
    dfground = dfground.set_index('Keywords')

    dfground['Methods'] = dfground['Methods'].apply(str_to_set)


 dfD = pd.DataFrame
 with open('k_means_best_k_clusters/K_means_results_for_evaluation_phase_of_'+Gclass, 'r') as csvfile:
    dfD = pd.read_csv(csvfile)
    dfD = dfD.set_index('cluster_id')
    dfD['method_name'] = dfD['method_name'].apply(str_to_set)


 dfground =dfground.rename(columns={"Keywords": "id", "Methods": "method_set"})
 dfground.index.name = "id"
 dfD =dfD.rename(columns={"cluster_id": "id", "method_name": "method_set"})
 dfD.index.name = "id"

 G = {}
 for i, s in enumerate(dfground['method_set']):
    G["string{0}".format(i)] = combinations(s, 2)


 intrapairsG = set()
 for value in G.values():
  
    intrapairsG.update(set(value))

 D = {}
 for i, s in enumerate(dfD['method_set']):
    D["string{0}".format(i)] = combinations(s, 2)

 intrapairsD = set()
 for value in D.values():
  
    intrapairsD.update(set(value))



 Intersection_Intrapairs_D_G = intrapairsD.intersection(intrapairsG)


 precision = len(Intersection_Intrapairs_D_G)/len(intrapairsD)
 recall = len(Intersection_Intrapairs_D_G)/len(intrapairsG)




#compute F score using both precision and recall and prin the results

 F = (2*precision*recall)/(precision+recall)

 print("Algorithm: K means"+"\n")
 print("Precision of "+Gclass +": " + str(precision) +"\n", "Recall of "+ Gclass+": " + str(recall) +"\n", 
       
       "F value of" + Gclass +": " +str(F) +"\n")
 
#The next lines of code do the same but for Agglomerative clustering best k results

for Gclass in GodClasses:

 dfground = pd.DataFrame

 with open('ground_truth_csv_files/'+Gclass, 'r') as csvfile:
    dfground = pd.read_csv(csvfile)
    dfground = dfground.set_index('Keywords')

    dfground['Methods'] = dfground['Methods'].apply(str_to_set)


 dfD = pd.DataFrame
 with open('Hierarchical_best_k_clusters/Hierarchical_results_for_evaluation_phase_of_'+Gclass, 'r') as csvfile:
    dfD = pd.read_csv(csvfile)
    dfD = dfD.set_index('cluster_id')
    dfD['method_name'] = dfD['method_name'].apply(str_to_set)


 dfground =dfground.rename(columns={"Keywords": "id", "Methods": "method_set"})
 dfground.index.name = "id"
 dfD =dfD.rename(columns={"cluster_id": "id", "method_name": "method_set"})
 dfD.index.name = "id"

 G = {}
 for i, s in enumerate(dfground['method_set']):
    G["string{0}".format(i)] = combinations(s, 2)


 intrapairsG = set()
 for value in G.values():
  
    intrapairsG.update(set(value))

 D = {}
 for i, s in enumerate(dfD['method_set']):
    D["string{0}".format(i)] = combinations(s, 2)

 intrapairsD = set()
 for value in D.values():
    
    intrapairsD.update(set(value))



 Intersection_Intrapairs_D_G = intrapairsD.intersection(intrapairsG)


 precision = len(Intersection_Intrapairs_D_G)/len(intrapairsD)
 recall = len(Intersection_Intrapairs_D_G)/len(intrapairsG)






 F = (2*precision*recall)/(precision+recall)



 print("Algorithm: Agglomerative"+"\n")

 print("Precision of "+Gclass +": " + str(precision) +"\n", "Recall of "+ Gclass+": " + str(recall) +"\n", 
       
       "F value of" + Gclass +": " +str(F) +"\n")
 

