# 📧 Mail Spam Detection Web Application

A machine learning-based web application that detects spam emails using Natural Language Processing (NLP) and Naive Bayes classification. The application is built with Flask and provides both a web interface and REST API for spam detection.

## 🎯 Project Overview

This project demonstrates the complete pipeline of a machine learning application:
- **Data Processing**: Text preprocessing and feature extraction
- **Model Training**: Naive Bayes classifier with CountVectorizer
- **Model Deployment**: Flask web application with REST API
- **User Interface**: Simple and intuitive web interface

## 🏗️ Project Structure

```
lab.2/
├── dataset/
│   ├── mail_spam_dataset_1.csv    # Training dataset
│   └── mail_spam_dataset_2.csv    # Additional dataset
├── models/
│   └── model.pkl                  # Trained model (saved)
├── flask_app/
│   ├── app.py                     # Flask application
│   ├── utils.py                   # Helper functions
│   └── templates/
│       └── index.html             # Web interface
├── mail_spam_example_tasks.ipynb  # Model training notebook
├── deploying_model_documentation.ipynb  # Deployment guide
├── save_model.py                  # Model saving script
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## 🚀 Features

### Core Functionality
- **Spam Detection**: Classifies emails as spam (1) or ham (0)
- **Real-time Processing**: Instant prediction results
- **Text Input**: Accepts email content through web interface
- **API Endpoint**: RESTful API for programmatic access

### Technical Features
- **Machine Learning Model**: Naive Bayes classifier with TF-IDF features
- **Text Preprocessing**: Stop words removal, encoding handling
- **Web Framework**: Flask-based web application
- **Responsive Design**: Clean and user-friendly interface

## 📋 Prerequisites

Before running this project, make sure you have:

- **Python 3.7+** installed
- **pip** package manager
- **Web browser** for accessing the application

## 🛠️ Installation & Setup

### 1. Clone or Download the Project
```bash
# Navigate to your project directory
cd lab.2
```

### 2. Install Dependencies
```bash
# Install required packages
pip install pandas scikit-learn flask
```

### 3. Train and Save the Model
```bash
# Run the model training script
python save_model.py
```

This will:
- Load the spam dataset
- Train a Naive Bayes classifier
- Save the model as `models/model.pkl`

## 🏃‍♂️ Running the Application

### 1. Start the Flask Server
```bash
# Navigate to the Flask app directory
cd flask_app

# Run the application
python app.py
```

### 2. Access the Web Interface
Open your web browser and go to:
```
http://127.0.0.1:5000/
```

### 3. Using the Application
1. **Enter Email Text**: Paste or type email content in the text area
2. **Click Predict**: Submit the form to get prediction
3. **View Results**: See if the email is classified as spam or ham
4. **Reset**: Use the reset link to clear the form

## 🔌 API Usage

The application also provides a REST API endpoint for programmatic access:

### Endpoint: `/api/predict`
- **Method**: POST
- **Content-Type**: application/json
- **Request Body**:
  ```json
  {
    "email": "Your email text here"
  }
  ```
- **Response**:
  ```json
  {
    "prediction": 1,
    "email": "Your email text here"
  }
  ```

### Example API Call
```python
import requests

url = "http://127.0.0.1:5000/api/predict"
data = {"email": "Free entry in 2 a wkly comp to win FA Cup final tkts"}
response = requests.post(url, json=data)
result = response.json()
print(f"Prediction: {'Spam' if result['prediction'] == 1 else 'Ham'}")
```

## 📊 Model Details

### Algorithm
- **Classifier**: Multinomial Naive Bayes
- **Feature Extraction**: CountVectorizer with TF-IDF
- **Text Preprocessing**: 
  - Stop words removal (English)
  - ASCII encoding
  - Error handling for special characters

### Training Data
- **Dataset**: SMS Spam Collection Dataset
- **Features**: Text content of messages
- **Labels**: Binary classification (0 = Ham, 1 = Spam)
- **Encoding**: ISO-8859-1

### Model Performance
The model is trained on a dataset containing:
- Ham (legitimate) messages
- Spam messages
- Preprocessed text features

## 🧪 Testing the Application

### Test Cases
1. **Spam Example**:
   ```
   "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121"
   ```
   Expected: Spam

2. **Ham Example**:
   ```
   "Hi, how are you? Let's meet for coffee tomorrow."
   ```
   Expected: Ham

### Manual Testing
1. Start the Flask application
2. Open the web interface
3. Enter test messages
4. Verify predictions match expectations

## 🔧 Configuration

### Flask Settings
- **Host**: 0.0.0.0 (accessible from any IP)
- **Port**: 5000
- **Debug Mode**: Enabled for development

### Model Settings
- **Model Path**: `models/model.pkl`
- **Vectorizer**: CountVectorizer with English stop words
- **Classifier**: MultinomialNB

## 📝 Dependencies

### Core Dependencies
- **Flask**: Web framework
- **pandas**: Data manipulation
- **scikit-learn**: Machine learning library
- **numpy**: Numerical computing
- **pickle**: Model serialization

### Optional Dependencies
- **requests**: For API testing
- **matplotlib**: For data visualization (in notebook)

## 🚨 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install missing dependencies
   ```bash
   pip install pandas scikit-learn flask
   ```

2. **Model Not Found**: Ensure model is saved
   ```bash
   python save_model.py
   ```

3. **Port Already in Use**: Change port in `app.py`
   ```python
   app.run(host="0.0.0.0", port=5001, debug=True)
   ```

4. **Encoding Errors**: Check dataset encoding
   - Dataset uses ISO-8859-1 encoding

## 🔮 Future Enhancements

### Potential Improvements
- **Model Performance**: Try different algorithms (SVM, Random Forest)
- **Feature Engineering**: Add more text features
- **User Interface**: Enhanced UI with Bootstrap/CSS
- **Database Integration**: Store predictions and user feedback
- **Real-time Learning**: Update model with new data
- **Email Integration**: Direct email processing
- **Multi-language Support**: Support for different languages

### Advanced Features
- **Confidence Scores**: Show prediction confidence
- **Batch Processing**: Process multiple emails at once
- **Model Versioning**: Track model improvements
- **Performance Metrics**: Display accuracy, precision, recall

## 📄 License

This project is created for educational purposes as part of a machine learning lab assignment.

## 👥 Contributing

This is a lab project, but suggestions and improvements are welcome!

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the Jupyter notebooks for detailed explanations
3. Ensure all dependencies are properly installed

---

**Happy Spam Detection! 🛡️📧** 