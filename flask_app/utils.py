import pickle
import os

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), '../models/model.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def model_predict(email_text):
    model = load_model()
    prediction = model.predict([email_text])[0]
    return prediction
