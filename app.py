import os
import pickle
import pandas as pd
from flask import Flask, request, render_template, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

app = Flask(__name__)

# Train and save model if it doesn't exist
def train_and_save_model():
    if not os.path.exists('model.pkl'):
        # Load the dataset
        df = pd.read_csv("dataset/mail_spam_dataset_1.csv", encoding="ISO-8859-1")
        
        # Prepare the data
        X = df['v2']  # Text column
        y = (df['v1'] == 'spam').astype(int)  # Convert ham/spam to 0/1
        
        # Create and train the model
        model = Pipeline([
            ('vectorizer', CountVectorizer(stop_words='english', encoding="utf-8", decode_error='replace', strip_accents='ascii')),
            ('classifier', MultinomialNB())
        ])
        
        # Train the model
        model.fit(X, y)
        
        # Save the model
        with open('model.pkl', 'wb') as file:
            pickle.dump(model, file)
        
        print("Model trained and saved successfully!")

def load_model():
    if not os.path.exists('model.pkl'):
        train_and_save_model()
    
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def model_predict(email_text):
    model = load_model()
    prediction = model.predict([email_text])[0]
    return prediction

@app.route("/")
def home():
    return render_template("index.html", prediction=None, email=None)

@app.route('/predict', methods=['POST'])
def predict():
    email = request.form.get('email')
    if not email:
        return render_template("index.html", prediction=None, email=email, error="Please enter an email message.")
    prediction = model_predict(email)
    return render_template("index.html", prediction=prediction, email=email)

@app.route('/api/predict', methods=['POST'])
def predict_api():
    try:
        data = request.get_json(force=True)
        email = data.get('email')
        if not email:
            return jsonify({'error': 'No email provided'}), 400
        prediction = model_predict(email)
        return jsonify({'prediction': int(prediction), 'email': email})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True) 