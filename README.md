# Mail Spam Detector

A machine learning web application that detects spam emails using a Naive Bayes classifier.

## Features

- Web interface for email spam detection
- REST API endpoint for programmatic access
- Real-time prediction using trained ML model

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask app:
   ```bash
   cd flask_app
   python app.py
   ```

3. Open http://127.0.0.1:5000 in your browser

## Deployment on Vercel

This project is configured for deployment on Vercel. The following files are required:

- `vercel.json` - Vercel configuration
- `flask_app/wsgi.py` - WSGI entry point
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification

## API Usage

### Web Interface
- Visit the homepage to use the web form
- Paste email text and click "Predict"

### REST API
```bash
curl -X POST https://your-vercel-app.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{"email": "Your email text here"}'
```

## Project Structure

```
├── flask_app/
│   ├── app.py          # Flask application
│   ├── utils.py        # Model loading and prediction
│   ├── wsgi.py         # WSGI entry point
│   └── templates/
│       └── index.html  # Web interface
├── models/
│   └── model.pkl       # Trained ML model
├── dataset/            # Training data
├── vercel.json         # Vercel configuration
├── requirements.txt    # Python dependencies
└── runtime.txt         # Python version
``` 