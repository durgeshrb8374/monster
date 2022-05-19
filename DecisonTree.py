import numpy as np
import pandas as pd

print("\n\n")
#reading dataset
dataset = pd.read_csv("DT.csv")
x = dataset.iloc[:,:-1]
y = dataset.iloc[:,5].values
#perform label encoding
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
x= x.apply(LabelEncoder().fit_transform)
print(x)
from sklearn.tree import DecisionTreeClassifier
regressor = DecisionTreeClassifier()
regressor.fit(x.iloc[:,1:5].values,y)
#predict value for the given expression
x_in =np.array([1,1,0,0])
Y_pred = regressor.predict([x_in])
print("\n---------------------------------------------")
print ("\n\nPrediction of given Test Data is {}".format(Y_pred[0]))
print("\n---------------------------------------------")
#from sklearn.externals.six import StringIO
from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(regressor, out_file = dot_data, filled =
True,rounded = True,special_characters = True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png("tree.png")