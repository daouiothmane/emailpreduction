import pickle
import os

def load_model():
    # Try multiple possible paths for the model
    possible_paths = [
        os.path.join(os.path.dirname(__file__), '../models/model.pkl'),
        os.path.join(os.getcwd(), 'models/model.pkl'),
        'models/model.pkl'
    ]
    
    for model_path in possible_paths:
        if os.path.exists(model_path):
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
            return model
    
    raise FileNotFoundError("Model file not found in any of the expected locations")

def model_predict(email_text):
    model = load_model()
    prediction = model.predict([email_text])[0]
    return prediction
