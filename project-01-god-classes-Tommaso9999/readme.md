### Information Modelling & Analysis: Project 1

Student: *Tommaso Verzegnassi*

### Project instructions:
Please follow the instructions provided in the project slides.
For your convenience, the source code to be analyzed (xerces2)
 has already been added to this repository (*/resources/xerces2-j-src*).

**Attention**: Please consider the submission instructions available on iCorsi.

**Report**: You may want to use the template distributed on iCorsi.



**Instructions**: 

#Final Commit: in the list below you can find the scripts in the order that should be ran with a short description of the operations performed, if you have any trouble to run or understand some sections of the code feel free to contact me on verzet@usi.ch!: 

1. Find_god_classes.py: this file, according to the rule of the mean number of methods + 6sigma, finds the god classes that are needed for 
our analysis. The classes are then printed with the number of methods contained. Then, for all subsequent phases, i just declared a list with 
the God Classes names. 

2. Extract_feature_vecotrs.py: this script creates 4 csv files, one for each God Class, that store the feature vectors. Each Method in the God Class is a row and the columns are represented by methods and fields accessed by the method that defines the row (first column of the csv files called"method name"). Only accessed methods and fields that belong to the God Class are added in the feature vector csv file.  

3. Hirarcical.py & k_means.py: These scripts apply the clustering algorithms seen in class for a k value equal to 2 on feature vector csv files previously produced. The clustering results are then saved in csv files in the folders "k_means_csv_files" and Agglomerative_csv_files". 

4. Silhouette.py: this script computes the silhouette metric for all the clustering solutions provided by the two previous scripts. The most important thing done by the silhouette script is the following: it applies k means and agglomerative clustering 58 times, from k=2 up to k=60 (essentially doing 58 times what Hierarcical.py and k_means.py do). Then, for each clustering solution produced by the different k values, the silhouette metric is computed. The higher the silhouette score value the better the clustering is as it means that there is low distance intra cluster and high distance inter cluster. The clustering solutions with the best silhouette scores are saved as csv files in the two following folders: "hierarchical_best_k_clusters" and "k_means_best_k_clusters". These will be needed for the final script precision_recall.py 

5. precision_recall.py: this script takes the csv files with the best k for each clustering algorithm and evaluates, with precision and recall intrapairs formulas, how good the clustering is. With precision and recall we can calculate the F score computed as (2*precision*recall)/precision + recall. The values of this index are, by convention, considered good around 0.5 and above and bad if below this threshold. Some of the clusterings had very high quality (up to 0.8 F score), others had lower quality of about 0.2/0.3 F score. This means that, according to our groud truth clustering technique, some of the clustering solution produced are very effective and developers of Xerces2 libary could apply them for refracotring. Others are not so good and could either need different k values (above 60) or different clustering algorithms. 

