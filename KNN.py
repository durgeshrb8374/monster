import numpy as np
import pandas as pd
#reading dataset
dataset = pd.read_csv("data.csv")
x = dataset.iloc[:,:-1]
y = dataset.iloc[:,2].values
#perform label encoding
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x.values,y)
#predict value for the given expression
X_in =np.array([6,2])
y_pred = classifier.predict([X_in])
print("\n\n ---------------------------------------------------------------------------\n")
print ("\tPrediction of the Given Values [6,2] is :{} ".format(y_pred[0]))
classifier =KNeighborsClassifier(n_neighbors=3,weights="distance")
classifier.fit(x.values,y)
y_pred = classifier.predict([X_in])
print ("\n\tDistance Weight KNN: ", y_pred)
print("\n-------------------------------------------------------------------------------")