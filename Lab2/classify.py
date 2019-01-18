# Import libraries
import numpy as np
import argparse
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

## Define argument parser with the following args:
## filepath: a string containing the path to the file
## header: binary variable ([0,1]) indicating whether the csv file has a header
## classifier: a string from ["logreg","svm","rf"] - type of classifier
## -n,--normalize: flag indicating whether to normalize the features or not


## Load the csv file using numpy's genfromtxt
## with the following args
## delimiter=",",names=None,skip_header=args.header


## Extract features and labels. Assume that the last column contains the labels. 
## Also assume all columns are of numerical type
## Eg:
## X = dat[:,:-1]
## y = dat[:,-1]


## Split dataset into training and test sets in the ratio 4:1
## use random_state = 42, test_size = 0.2


## If normalization is requested, use either sklearn's StandardScaler
## or your own function


## Define classifier object depending on user output
## denote the classifier object by clf
## Use random_state = 1 for all classifiers. In addition,
## for logistic regression, use solver = 'lbfgs'
## for support vector classifer - use kernel ='rbf', C=1, and gamma = 1/(#cols)
## for random forests, use n_estimators=200,min_samples_leaf = 5


## Train classifier
## clf.fit(_,_)

## Compute and print training and test accuracy
## Use accuracy_score
## eg: print("Training accuracy of {}: {}".format(args.classifier,_))


## Save the object to disk using pickle
## Modify the out directory using os.path.join if you want a different directory
with open(classifier+"_"+ dataset +".pkl",'wb') as f:
	pickle.dump(clf,f)