#importing the necesary libraires
import pandas as pd
import mlflow
import re
import numpy as np
import sklearn





from sklearn.linear_model import SGDClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay














def Train_SGD_Classifier(X_train, y_train):
    
    mlflow.sklearn.autolog()
    

    model = SGDClassifier(n_jobs=-1,loss='log_loss' ,max_iter=1000)

    model.fit(X_train, y_train.to_numpy())

    

    return  model


def Test_SGD_Classifier(model , X_test , y_test):

    y_pred = model.predict(X_test)

    cm = ConfusionMatrixDisplay.from_estimator(model, X_test, y_test
                                               ,cmap='Blues', values_format='d'
                                               ,display_labels=['Accepted', 'Declined'])
    
    mlflow.log_metric("accuracy_score", accuracy_score(y_test, y_pred))
    mlflow.log_metric("roc_auc_score" , roc_auc_score(y_test, y_pred))
    mlflow.log_figure(cm.figure_, 'test_confusion_matrix.png')


    
    
   



