# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fj1NL195QFvRuzUp-d81pZpY-muCkXcR
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from google.colab import files
file1=files.upload()

df=pd.read_csv('/content/hcvdat0.csv')

df.head()

df.shape

df=df.drop(['Unnamed: 0'],axis=1)

df.head()

df.shape

y=np.array(df['Category'])

df=df.drop(['Category'],axis=1)

df=df.replace(['m','f'],[0,1])

cols=df.columns
print(cols)

x=df[:]

x

df.isnull().sum()

from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy='mean')
x=si.fit_transform(x)

pd.DataFrame(x).isnull().sum()

y.shape

g=sns.countplot(y)
plt.xticks(rotation='vertical')
plt.xlabel(['0=Blood Donor','1=suspect Blood Donor','2=Hepatitis','3=Fibrosis','4=Cirrhosis'])
plt.show()

from imblearn.over_sampling import SMOTE
smote=SMOTE()

x_smote,y_smote=smote.fit_resample(x,y)

g=sns.countplot(y_smote)
plt.xticks(rotation='vertical')
plt.xlabel(['0=Blood Donor','1=suspect Blood Donor','2=Hepatitis','3=Fibrosis','4=Cirrhosis'])
plt.show()

from sklearn.impute import SimpleImputer
si=SimpleImputer(strategy='mean')
df=si.fit_transform(df)
df=pd.DataFrame(df,columns=cols)

corr_mat=np.corrcoef(df[cols].values.T)
plt.figure(figsize=(12,12))
hm=sns.heatmap(corr_mat, annot=True)
plt.show()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_smote,y_smote, test_size=0.2)

from sklearn.model_selection import train_test_split
x_val, x_test1, y_val, y_test1 = train_test_split(x_test,y_test, test_size=0.5)

from imblearn.over_sampling import SMOTE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.metrics import accuracy_score

from sklearn.metrics import confusion_matrix ,precision_score,accuracy_score,recall_score,f1_score

result=[]
l=[]

p1=Pipeline([('s1',StandardScaler()),('l1',PCA()),('svm',SVC())])
p1.fit(x_train,y_train)
pred_train_p1=p1.predict(x_train)
pred_test_p1=p1.predict(x_test)
pred_val_p1=p1.predict(x_val)
pred_test1_p1=p1.predict(x_test1)
print("Accuracy of SVM on training: ",accuracy_score(pred_train_p1,y_train))
print("Accuracy of SVM on testing: ",accuracy_score(pred_test_p1,y_test))
l.append("SVM")
l.append(accuracy_score(pred_test_p1,y_test))
l.append(accuracy_score(pred_val_p1,y_val))
l.append(accuracy_score(pred_test1_p1,y_test1))
l.append(precision_score(pred_test_p1,y_test,average="weighted"))
l.append(recall_score(pred_test_p1,y_test,average="weighted"))
l.append(f1_score(pred_test_p1,y_test,average="weighted"))
result.append(l)

p2=Pipeline([('s2',StandardScaler()),('l2',PCA()),('lr',LogisticRegression())])
p2.fit(x_train,y_train)
pred_train_p2=p2.predict(x_train)
pred_test_p2=p2.predict(x_test)
pred_val_p2=p2.predict(x_val)
pred_test1_p2=p2.predict(x_test1)
print("Accuracy of LogisticRegression on training: ",accuracy_score(pred_train_p2,y_train))
print("Accuracy of LogisticRegression on testing: ",accuracy_score(pred_test_p2,y_test))
l=[]
l.append("LR")
l.append(accuracy_score(pred_test_p2,y_test))
l.append(accuracy_score(pred_val_p2,y_val))
l.append(accuracy_score(pred_test1_p2,y_test1))
l.append(precision_score(pred_test_p2,y_test,average="weighted"))
l.append(recall_score(pred_test_p2,y_test,average="weighted"))
l.append(f1_score(pred_test_p2,y_test,average="weighted"))
result.append(l)

p3=Pipeline([('s3',StandardScaler()),('l3',PCA()),('dtr',DecisionTreeClassifier())])
p3.fit(x_train,y_train)
pred_train_p3=p3.predict(x_train)
pred_test_p3=p3.predict(x_test)
pred_val_p3=p3.predict(x_val)
pred_test1_p3=p3.predict(x_test1)
print("Accuracy of DecisionTreeRegressor on training: ",accuracy_score(pred_train_p3,y_train))
print("Accuracy of DecisionTreeRegressor on testing: ",accuracy_score(pred_test_p3,y_test))
l=[]
l.append("DT")
l.append(accuracy_score(pred_test_p3,y_test))
l.append(accuracy_score(pred_val_p3,y_val))
l.append(accuracy_score(pred_test1_p3,y_test1))
l.append(precision_score(pred_test_p3,y_test,average="weighted"))
l.append(recall_score(pred_test_p3,y_test,average="weighted"))
l.append(f1_score(pred_test_p3,y_test,average="weighted"))
result.append(l)

p4=Pipeline([('s4',StandardScaler()),('l4',LDA(n_components=4)),('gnb',GaussianNB())])
p4.fit(x_train,y_train)
pred_train_p4=p4.predict(x_train)
pred_test_p4=p4.predict(x_test)
pred_val_p4=p4.predict(x_val)
pred_test1_p4=p4.predict(x_test1)
print("Accuracy of GaussianNB on training: ",accuracy_score(pred_train_p4,y_train))
print("Accuracy of GaussianNB on testing: ",accuracy_score(pred_test_p4,y_test))
l=[]
l.append("GNB")
l.append(accuracy_score(pred_test_p4,y_test))
l.append(accuracy_score(pred_val_p4,y_val))
l.append(accuracy_score(pred_test1_p4,y_test1))
l.append(precision_score(pred_test_p4,y_test,average="weighted"))
l.append(recall_score(pred_test_p4,y_test,average="weighted"))
l.append(f1_score(pred_test_p4,y_test,average="weighted"))
result.append(l)

p5=Pipeline([('s5',StandardScaler()),('l5',PCA()),('rft',RandomForestClassifier(n_estimators=100, random_state=0))])
p5.fit(x_train,y_train)
pred_train_p5=p5.predict(x_train)
pred_test_p5=p5.predict(x_test)
pred_test1_p5=p5.predict(x_test1)
pred_val_p5=p5.predict(x_val)
print("Accuracy of RandomForestRegressor on training: ",accuracy_score(pred_train_p5,y_train))
print("Accuracy of RandomForestRegressor on testing: ",accuracy_score(pred_test_p5,y_test))
l=[]
l.append("RF")
l.append(accuracy_score(pred_test_p5,y_test))
l.append(accuracy_score(pred_val_p5,y_val))
l.append(accuracy_score(pred_test1_p5,y_test1))
l.append(precision_score(pred_test_p5,y_test,average="weighted"))
l.append(recall_score(pred_test_p5,y_test,average="weighted"))
l.append(f1_score(pred_test_p5,y_test,average="weighted"))
result.append(l)

p6=Pipeline([('s6',StandardScaler()),('l6',PCA()),('knn',KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=4))])
p6.fit(x_train,y_train)
pred_train_p6=p6.predict(x_train)
pred_test_p6=p6.predict(x_test)
pred_test1_p6=p6.predict(x_test1)
pred_val_p6=p6.predict(x_val)
print("Accuracy of KNeighborsClassifier on training: ",accuracy_score(pred_train_p6,y_train))
print("Accuracy of KNeighborsClassifier on testing: ",accuracy_score(pred_test_p6,y_test))
l=[]
l.append("KNN")
l.append(accuracy_score(pred_test_p6,y_test))
l.append(accuracy_score(pred_val_p6,y_val))
l.append(accuracy_score(pred_test1_p6,y_test1))
l.append(precision_score(pred_test_p6,y_test,average="weighted"))
l.append(recall_score(pred_test_p6,y_test,average="weighted"))
l.append(f1_score(pred_test_p6,y_test,average="weighted"))
result.append(l)

result=np.array(result)
result=pd.DataFrame(result,columns=['Methods','Accuracy_test_without_holdout','validaton_accuracy','Accuracy_test_holdout','Precision','Recall','F1_score'],index=[1,2,3,4,5,6])
display(result)

validation=list(result['validaton_accuracy'])
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')
for i in range(6):
  validation[i]=float(validation[i])*100
  validation[i]=float("{0:.2f}".format(validation[i]))
print(validation)
plt.bar(['SVM','LR','DT','GNB','RF','KNN'],validation,color='green')
addlabels(['SVM','LR','DT','GNB','RF','KNN'],validation)
plt.show()

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

k=5

kf=KFold(n_splits=k, shuffle=True)

acc_score=[]

result=cross_val_score(p5,x,y, cv=kf)

print(np.average(result))