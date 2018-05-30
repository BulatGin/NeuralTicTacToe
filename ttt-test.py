import pandas as pd

data = pd.read_csv('dataset_50_tic-tac-toe.csv')
#  print(data.head())
X = data.iloc[1:, 0:9]
#  print(X.head())
y = data.iloc[1:, 9:10]
#  print(y.head())
print(y.Class.unique())
# print(pd.get_dummies(X.bm.unique()))
#  print(pd.concat([X, pd.get_dummies(X.bm.unique())], axis=1).head())
#  print(X.join(pd.get_dummies(X.bm.unique())))
#  print(pd.get_dummies(y.Class.unique()))
X = pd.get_dummies(X, columns=["tl", "tm", "tr", "ml", "mm", "mr", "bl", "bm", "br"])
print(X.head())

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

y = y.apply(le.fit_transform)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(27,), max_iter=10000)
mlp.fit(X_train, y_train.values.ravel())

predictions = mlp.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

# print(mlp.predict_proba([[0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0]]))
print(mlp.predict_proba([[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1]]))
c = mlp.classes_
print(c)

#  001 - X
#  010 - O
#  100 - blank
