from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your models (assuming they are saved as pickle files)
with open('models/diabetes_model.sav', 'rb') as f:
    diabetes_model = pickle.load(f)
with open('models/heart_disease_model.sav', 'rb') as f:
    heart_disease_model = pickle.load(f)
with open('models/parkinsons_model.sav', 'rb') as f:
    parkinson_model = pickle.load(f)

@app.route('/')
def home():
    return "Welcome to the Medical Prediction App!"

@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes_form():
    if request.method == 'POST':
        # Retrieve form data
        Pregnancies = int(request.form['Pregnancies'])
        Glucose = float(request.form['Glucose'])
        BloodPessure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])

        # Make prediction using the model
        prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPessure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])[0]

        return render_template('results.html', prediction=prediction)

    return render_template('diabetes_form.html')

@app.route('/predict_heart_disease', methods=['GET', 'POST'])
def predict_heart_disease():
    if request.method == 'POST':
        # Get form data
        data = [float(request.form[field]) for field in ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']]
        prediction = heart_disease_model.predict([np.array(data)])
        result = 'Positive' if prediction[0] == 1 else 'Negative'
        return render_template('heart_disease_form.html', prediction=result)
    return render_template('heart_disease_form.html')

@app.route('/predict_parkinson', methods=['GET', 'POST'])
def predict_parkinson():
    if request.method == 'POST':
        # Get form data
        fields = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']
        data = [float(request.form[field]) for field in fields]
        prediction = parkinson_model.predict([np.array(data)])
        result = 'Positive' if prediction[0] == 1 else 'Negative'
        return render_template('parkinson_form.html', prediction=result)
    return render_template('parkinson_form.html')

if __name__ == '__main__':
    app.run(debug=True)
