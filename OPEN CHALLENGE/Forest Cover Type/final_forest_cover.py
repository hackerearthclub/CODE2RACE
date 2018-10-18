#Importing Modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#Reading Training & Testing Data
train = pd.read_csv("D://ML bvp//Data//Forest Cover Type//train.csv")
test = pd.read_csv("D://ML bvp//Data//Forest Cover Type//test.csv")
train_y=train["Cover_Type"]
train_X = train.drop(['Id','Cover_Type','Soil_Type7','Soil_Type15'],axis=1)
test_X = test.drop(['Id','Soil_Type7','Soil_Type15'],axis=1)


#Cover type distributution 
plt.hist(train_y,bins=14)
plt.title("Cover type distribution in training data")
plt.xlabel("cover type")
plt.ylabel("frequency")
print(train_y.value_counts())
print(len(train_y))
plt.show()


#Data Visualization
for i,j in zip(range(1,11),test_X.columns):
	plt.figure()
	sns.distplot(train[j])
plt.show()


#Splitting Data into Train & Test
import sklearn.model_selection
x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(train_X,train_y,test_size=0.2)


#RANDOM FOREST
import sklearn.ensemble
rf = sklearn.ensemble.RandomForestClassifier()
rf=rf.fit(x_train,y_train)
print("Random Forest Accuracy-->",rf.score(x_test,y_test),'\n')


#Top 10 important features
importance=rf.feature_importances_
indices = np.argsort(importance)[::-1]
indices=indices[:10]
plt.figure() 
plt.title("Cover Type:Top 10 Feature importances") 
plt.bar(range(10), importance[indices],align="center") 
plt.xticks(range(10),train.columns[indices], fontsize=14,rotation=90) 
plt.xlim([-1, 10]) 
plt.show()


#DECISION TREE
import sklearn.tree
clf_gini=sklearn.tree.DecisionTreeClassifier(criterion='gini',random_state=0,max_depth=5,min_samples_leaf=7)
clf=clf_gini.fit(x_train,y_train)
print("Decision Tree Accuracy-->",clf.score(x_test,y_test),'\n')


#NAIVE BAYES
from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb=nb.fit(x_train,y_train)
print("Naive Bayes Accuracy-->",nb.score(x_test,y_test),'\n')


#SVM:SVC
import sklearn.svm
sv=sklearn.svm.SVC()
sv=sv.fit(x_train,y_train)
print("SVM Accuracy-->",sv.score(x_test,y_test),'\n')


#DNN Classifier
import tensorflow as tf
feature_columns=[]

for key in train_X.keys():
	feature_columns.append(tf.contrib.layers.feature_column.real_valued_column(key))

estimator=tf.estimator.DNNClassifier(feature_columns=feature_columns,hidden_units=[10,10],n_classes=7)
def my_input_fn():
	df=pd.read_csv("D://ML bvp//Data//Forest Cover Type//train.csv")
	y=pd.Categorical(df["Cover_Type"]).codes
	y=np.array(y,dtype=np.int32)
	df=df.drop(["Id","Cover_Type"],axis=1)
	x=df
	x_train,x_test,y_train,y_test=sklearn.model_selection.train_test_split(x,y,test_size=0.2)
	return x_train,x_test,y_train,y_test

train_x,test_x,train_y,test_y=my_input_fn()	

def my_train_input_fn():
	return dict(train_x),train_y

def my_test_input_fn():
	return dict(test_x),test_y
estimator.train(input_fn=my_train_input_fn,steps=200)
print("DNN Classifier Accuracy-->",estimator.evaluate(input_fn=my_test_input_fn,steps=200))


# Retrain with entire training set and predict test set.
rf.fit(train_X,train_y)
ans=rf.predict(test_X)


#Write to CSV
submission =pd.DataFrame({"Id":test["Id"],"Cover_Type":ans})
submission.to_csv('Final Submission.csv',index=False)