# 🚀 Mail Spam Detector

A machine learning-based web application that detects spam emails using Natural Language Processing and Naive Bayes classification.

## 🎯 Features

- **Real-time Spam Detection**: Instantly classify emails as spam or legitimate
- **Web Interface**: User-friendly HTML interface for easy interaction
- **REST API**: JSON API endpoint for programmatic access
- **Machine Learning Model**: Trained on a comprehensive spam dataset
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn, Naive Bayes Classifier
- **Text Processing**: CountVectorizer with English stop words
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Hugging Face Spaces

## 📊 Model Performance

The model is trained on a dataset containing:
- **Ham (Legitimate)**: Normal, legitimate emails
- **Spam**: Promotional, suspicious, or unwanted emails

The classifier uses:
- **CountVectorizer**: Converts text to numerical features
- **Multinomial Naive Bayes**: Probabilistic classifier for text classification
- **English Stop Words**: Removes common words to improve accuracy

## 🚀 Usage

### Web Interface
1. Visit the application URL
2. Paste your email message in the text area
3. Click "Predict" to get the classification
4. View the result (Spam or Not Spam)

### API Usage
Send a POST request to `/api/predict` with JSON data:

```json
{
    "email": "Your email message here"
}
```

Response:
```json
{
    "prediction": 1,
    "email": "Your email message here"
}
```

- `prediction: 1` = Spam
- `prediction: 0` = Ham (Not Spam)

## 📁 Project Structure

```
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Web interface
├── dataset/
│   └── mail_spam_dataset_1.csv  # Training data
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🔧 Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mail-spam-detector
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Web Interface: http://localhost:7860
   - API Endpoint: http://localhost:7860/api/predict

## 📈 Model Training

The model is automatically trained when the application starts for the first time. The training process:

1. Loads the spam dataset
2. Preprocesses the text data
3. Trains a Naive Bayes classifier
4. Saves the model for future use

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Dataset: SMS Spam Collection Dataset
- Scikit-learn team for the excellent ML library
- Flask team for the web framework
- Hugging Face for the deployment platform

---

**Made with ❤️ for the ML community** 