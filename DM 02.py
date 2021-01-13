#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as acc
from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS
df = pd.read_csv("Absenteeism_at_work.csv",sep=';')
X_train, X_test, y_train, y_test = train_test_split(
    df.values[:,:-1],
    df.values[:,-1:],
    test_size=0.25,
    random_state=42)

y_train = y_train.ravel()
y_test = y_test.ravel()
print('Training dataset shape:', X_train.shape, y_train.shape)
print('Testing dataset shape:', X_test.shape, y_test.shape)

clf = RandomForestClassifier(n_estimators=100, n_jobs=-1)
knn = KNeighborsClassifier(n_neighbors=3)
print("1.Forward Selection")
print("2.Backward Selection")
print("3.Combined Selection")
choice = int(input("Enter the choice"))

# Build step forward feature selection
if(choice == 1):
  sfs1 = sfs(clf,
           k_features=4,
           forward=True,
           floating=False,
           verbose=2,
           scoring='accuracy',
           cv=5)
 # Perform SFFS
  sfs1 = sfs1.fit(X_train, y_train)

  feat_cols = list(sfs1.k_feature_idx_)
  print("****************")
  print("The selected feature list:")
  print(feat_cols)
elif(choice == 2):
  sfs1 = sfs(clf,
           k_features=4,
           forward=False,
           floating=False,
           verbose=2,
           scoring='accuracy',
           cv=5)
  # Perform SFFS
  sfs1 = sfs1.fit(X_train, y_train)

  feat_cols = list(sfs1.k_feature_idx_)
  print("****************")
  print("The selected feature list:")
  print(feat_cols)
elif(choice == 3):
  efs1 = EFS(knn,
             min_features=4, 
             max_features=5,
             scoring='accuracy',
             print_progress=True,
             cv = 5)
  efs1 = efs1.fit(X_train, y_train)
  feat_cols = list(efs1.best_idx_)
  print("****************")
  print("The selected feature list:")
  print(feat_cols)
else:
  print("Wrong Input")


# In[ ]:




