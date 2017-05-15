import cv2
import numpy as np
import os
from sklearn.decomposition import PCA
from sklearn.lda import LDA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn import linear_model

#########################################################################################################
npzfile = np.load('potholes_features.npz')
features = npzfile['arr_0']
labels = npzfile['arr_1']
print(features.shape)

### PCA to reduce the dimensions of data
#pca = PCA(n_components=5000)
#pca.fit(features)
#print(pca.explained_variance_ratio_)
#reduced_features = pca.transform(features);
#print(reduced_features.shape)

### LDA to project data into most discriminative (n-1) directions where n is the number of classes
#lda = LDA()
#lda.fit(reduced_features, labels)
#new_features = lda.transform(reduced_features)
#print(new_features.shape)

### Classification

# partition the data into training and testing splits, using 75%
# of the data for training and the remaining 25% for testing
(trainFeat, testFeat, trainLabels, testLabels) = train_test_split(features, labels, test_size=0.25, random_state=42)

### SVM Classifier
### One against one approach
# clf = svm.SVC(decision_function_shape='ovo')
# clf.fit(trainFeat, trainLabels)
# acc = model.score(testFeat, testLabels)
# print("[INFO] SVM's accuracy with one against one approach: {:.2f}%".format(acc * 100))

# ### One against rest approach
# clf = svm.SVC(decision_function_shape='ovr')
# clf.fit(trainFeat, trainLabels)
# acc = model.score(testFeat, testLabels)
# print("[INFO] SVM's accuracy with one against rest approach: {:.2f}%".format(acc * 100))

# ### Logistic Regression Classifier
# lr = linear_model.LogisticRegression(C=1e5)
# lr.fit(trainFeat, trainLabels)
# acc = lr.score(testFeat, testLabels)
# print("[INFO] Multinomail Logistic Regression's Accuracy: {:.2f}%".format(acc * 100))


# ### KNN Classifier
# # train and evaluate a k-NN classifer on the histogram
# # representations
# print("[INFO] evaluating Average Flow Histogram's accuracy...")
# model = KNeighborsClassifier(n_neighbors=1000,n_jobs=10)
# model.fit(trainFeat, trainLabels)
# acc = model.score(testFeat, testLabels)
# print("[INFO] KNN's accuracy: {:.2f}%".format(acc * 100))

### Incremental Classifiers
clf = linear_model.SGDClassifier()
clf.fit(trainFeat, trainLabels)
acc = model.score(testFeat, testLabels)
print("[INFO] SGD Classifier's accuracy with one against rest approach: {:.2f}%".format(acc * 100))