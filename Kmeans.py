# Practical 4: K-means
from statistics import mode
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Data Set
X = [ [0.1,0.6],[0.15,0.71],[0.08,0.9],[0.16,0.85],
 [0.2,0.3],[0.25,0.5],[0.24,0.1],[0.3,0.2]
 ]
#Initalize Centre Points
centers = np.array( [ [0.1,0.6] , [0.3,0.2] ] )
print("\n\nInitial Centriods -> {} and {}".format(centers[0],centers[1]))
#Generating the Model
from sklearn.cluster import KMeans
model = KMeans(n_clusters=2,init= centers, n_init=1)
model.fit(X)
print("Labels -> {} ".format(model.labels_))
print("\n -------------------------------------------------------------------------------------------------------------")
print("\n\t\t -- Answer of Given Questions --")
# Which cluster does P6 belongs to?
print("\n\tP6 Belongs to Cluster : {}".format(model.labels_[5]))
# What is the population of cluster around m2?
print("\n\tPopulation around Cluster 'm2 = [0.15,0.71]' : {}".format(np.count_nonzero(model.labels_== 1)))
# What is updated value of m1 and m2(New Centriods)?
print("\n\tUpdates Values of m1 and m2 'New Centriods' : {} and {}".format(model.cluster_centers_[0],model.cluster_centers_[1]))
print("\n ---------")