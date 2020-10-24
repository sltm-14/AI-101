from sklearn.model_selection import train_test_split #to split our sets for trraining and test
from sklearn.metrics import accuracy_score # to calculate the accuracy of our predictions

#y = music_...
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2) # we take 20% of our set for testing, returns a tupple
# X = inputs for training and testing
# y = oututs for training and testing

model = decisionTreeClassifier()
model.fir(X_train, y_train)
predictions = model.redict(X_test)

score = accuracy_score(y_test, predictions) # Check the accuracy of our predictions, 1 = 100%
