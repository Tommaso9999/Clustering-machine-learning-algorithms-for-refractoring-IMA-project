import pandas as pd 
import os

FeatureVectorsCSVS=[r"feature_vectors_csv_files/CoreDocumentImpl.csv", r"feature_vectors_csv_files/DTDGrammar.csv", r"feature_vectors_csv_files/XIncludeHandler.csv", r"feature_vectors_csv_files/XSDHandler.csv"]



folder_name = 'ground_truth_csv_files'
if not os.path.exists(folder_name):
    os.mkdir(folder_name)



with open('keyword_list.txt', 'r') as f:
    keywords = [line.strip() for line in f]


keywords.append('none') #is needed for methods that do not contain any keyword

for element in FeatureVectorsCSVS:
  

    ground_truth_cluster = {}
    df = pd.read_csv(element)

    for method_name in df['method_name']:
        keyword_found = False
        
        for keyword in keywords:
            if keyword.lower() in method_name.lower():
                if keyword not in ground_truth_cluster:
                    ground_truth_cluster[keyword] = []
                
                ground_truth_cluster[keyword].append(method_name)
                keyword_found = True
        
        # If no keyword was found, add the method to the 'none' cluster
        if not keyword_found:
            if 'none' not in ground_truth_cluster:
                ground_truth_cluster['none'] = []
            ground_truth_cluster['none'].append(method_name)


  

    df2 = pd.DataFrame.from_dict(list(ground_truth_cluster.items()))
    df2 = df2.rename(columns={0: 'Keywords', 1: 'Methods'})
    df2 = df2.set_index('Keywords')
    df2.to_csv(os.path.join(folder_name, os.path.basename(element)))
    print(os.path.basename(element) + " Ground truth:")
    print(df2)
    print("\n")
