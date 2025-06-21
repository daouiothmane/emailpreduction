import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import os

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Load the dataset
df = pd.read_csv("dataset/mail_spam_dataset_1.csv", encoding="ISO-8859-1")

# Prepare the data
X = df['v2']  # Text column
y = (df['v1'] == 'spam').astype(int)  # Convert ham/spam to 0/1

# Create and train the model (same as in the notebook)
clf_NaiveBaised = Pipeline([
    ('vectorizer', CountVectorizer(stop_words='english', encoding="utf-8", decode_error='replace', strip_accents='ascii')),
    ('classifier', MultinomialNB())
])

# Train the model
clf_NaiveBaised.fit(X, y)

# Save the model
with open('models/model.pkl', 'wb') as file:
    pickle.dump(clf_NaiveBaised, file)

print("Model saved successfully as 'models/model.pkl'") 