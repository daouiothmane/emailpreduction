from flask import Flask, request, render_template, jsonify
from utils import model_predict

app = Flask(__name__)

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

# For local development
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
