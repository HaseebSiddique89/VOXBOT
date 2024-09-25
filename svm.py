import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load the labeled dataset
data = pd.read_csv(r'C:\\Users\\MUHAMMAD HASEEB\\Documents\\CHATBOT - Copy\\Easy-Chatbot-master\\names_dataset.csv')

# Step 2: Preprocess the data
data['name'] = data['name'].str.lower()  # Convert names to lowercase
data['gender'] = data['gender'].map({'M': 0, 'F': 1})  # Map gender labels to 0 and 1

# Step 3: Feature extraction
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 3))
features = vectorizer.fit_transform(data['name'])

# Step 4: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(features, data['gender'], test_size=0.1, random_state=42)

# Step 5: Train the model
model_svm = SVC()
model_svm.fit(X_train.toarray(), y_train)

# Step 6: Evaluate the model
predictions_svm = model_svm.predict(X_test.toarray())
accuracy_svm = accuracy_score(y_test, predictions_svm)
print(f"SVM Accuracy: {accuracy_svm}")

# Step 7: Predict gender for new names
def svc(name):
    name = [name.lower()]
    feature = vectorizer.transform(name)
    new_prediction = model_svm.predict(feature.toarray())
    return new_prediction[0]


# name = input('enter: ')
# a = svc(name)
# print('output', a)