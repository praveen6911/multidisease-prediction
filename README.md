
---

# Multidisease Prediction Project

## Overview

This project involves predicting the presence of multiple diseases, including heart disease, Parkinson's disease, and diabetes, using machine learning algorithms. A Flask web application is also developed to allow users to input their health data and receive predictions.

## Dataset

Datasets used for this project include health records containing various features relevant to each disease. Each dataset is preprocessed to ensure data quality and to handle missing values.

### Datasets Used
- **Heart Disease Dataset**: Contains features such as age, sex, chest pain type, resting blood pressure, cholesterol level, etc.
- **Parkinson's Disease Dataset**: Contains features extracted from voice recordings, such as jitter, shimmer, and other measures.
- **Diabetes Dataset**: Contains features such as age, BMI, blood pressure, glucose levels, etc.

## Methodology

### Data Preprocessing

1. **Handling Missing Values**: Imputation techniques to fill missing values.
2. **Feature Scaling**: Standardizing or normalizing features.
3. **Encoding Categorical Variables**: Converting categorical variables to numerical values.

### Machine Learning Models

- **Heart Disease Prediction**: Logistic Regression
- **Parkinson's Disease Prediction**: Support Vector Machine (SVM)
- **Diabetes Prediction**: Logistic Regression

### Evaluation Metrics

- **Accuracy**: The proportion of correctly classified instances.
- **Precision**: The proportion of positive predictions that are actually positive.
- **Recall**: The proportion of actual positives that are correctly predicted.
- **F1 Score**: The harmonic mean of precision and recall.

## Flask Web Application

A Flask web application is developed to provide an interface for users to input their health data and receive disease predictions.

### Features

- User-friendly interface for data input.
- Predictions for heart disease, Parkinson's disease, and diabetes.
- Display of prediction probabilities and relevant health advice.

## Installation

To run the project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/multidisease-prediction.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd multidisease-prediction
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**:

   ```bash
   python app.py
   ```

5. **Access the app**:

   Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Data Preprocessing**:

   ```python
   from preprocess import preprocess_data
   preprocess_data('path/to/dataset.csv')
   ```

2. **Model Training**:

   ```python
   from train import train_model
   train_model('path/to/preprocessed_data.csv', 'heart_disease')
   train_model('path/to/preprocessed_data.csv', 'parkinsons_disease')
   train_model('path/to/preprocessed_data.csv', 'diabetes')
   ```

3. **Model Evaluation**:

   ```python
   from evaluate import evaluate_model
   evaluate_model('path/to/test_data.csv', 'heart_disease')
   evaluate_model('path/to/test_data.csv', 'parkinsons_disease')
   evaluate_model('path/to/test_data.csv', 'diabetes')
   ```

4. **Running the Flask App**:

   ```python
   python app.py
   ```

## Contributing

Contributions are welcome! Please open an issue to discuss what you would like to change or add.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
- [Parkinson's Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Parkinsons)
- [Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

