# app.py

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle
import os

# Create flask app
app = Flask(__name__)

# Load the kidney disease model
kidney_model = pickle.load(open("kidney.pkl", "rb"))

# --- You will need to load your other models here ---
# Example:
# heart_model = pickle.load(open("heart.pkl", "rb"))
# diabetes_model = pickle.load(open("diabetes.pkl", "rb"))


# --- Main Routes ---
@app.route("/")
def home():
    return render_template("home.html")

# --- Kidney Disease Prediction ---
@app.route("/kidney")
def kidneyPage():
    return render_template("kidney.html")

@app.route("/predict_kidney", methods=["POST"])
def predict_kidney():
    try:
        if request.method == 'POST':
            input_features = [float(x) for x in request.form.values()]
            features_value = [np.array(input_features)]
            
            feature_names = ['age', 'bp', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 
                             'bgr', 'bu', 'sc', 'pot', 'wc', 'htn', 'dm', 'cad', 'pe', 'ane']
            
            df = pd.DataFrame(features_value, columns=feature_names)
            output = kidney_model.predict(df)
            
            if output[0] == 1:
                prediction_text = "The person is likely to have Chronic Kidney Disease."
            else:
                prediction_text = "The person is not likely to have Chronic Kidney Disease."
                
            return render_template('predict.html', prediction=prediction_text, disease="Kidney Disease")

    except Exception as e:
        message = f"Error during prediction: {e}. Please check your inputs and try again."
        return render_template('kidney.html', message=message)

# --- Heart Disease Prediction ---
@app.route("/heart")
def heartPage():
    return render_template("heart.html")

@app.route("/predict_heart", methods=["POST"])
def predict_heart():
    # TODO: Add your heart disease model and prediction logic here
    # Example: data = [float(x) for x in request.form.values()]
    # prediction = heart_model.predict([data])
    return render_template('predict.html', prediction="Heart prediction logic is not implemented yet.", disease="Heart Disease")

# --- Diabetes Prediction ---
@app.route("/diabetes")
def diabetesPage():
    return render_template("diabetes.html")

@app.route("/predict_diabetes", methods=["POST"])
def predict_diabetes():
    # TODO: Add your diabetes model and prediction logic here
    return render_template('predict.html', prediction="Diabetes prediction logic is not implemented yet.", disease="Diabetes")

# --- Liver Disease Prediction ---
@app.route("/liver")
def liverPage():
    return render_template("liver.html")

@app.route("/predict_liver", methods=["POST"])
def predict_liver():
    # TODO: Add your liver disease model and prediction logic here
    return render_template('predict.html', prediction="Liver prediction logic is not implemented yet.", disease="Liver Disease")

# --- Breast Cancer Prediction ---
@app.route("/cancer")
def cancerPage():
    return render_template("breast_cancer.html")
    
@app.route("/predict_cancer", methods=["POST"])
def predict_cancer():
    # TODO: Add your breast cancer model and prediction logic here
    return render_template('predict.html', prediction="Breast Cancer prediction logic is not implemented yet.", disease="Breast Cancer")

# --- Malaria Prediction ---
@app.route('/malaria')
def malariaPage():
    return render_template('malaria.html')

@app.route('/malariapredict', methods=['POST'])
def malariapredictPage():
    # TODO: Add your malaria (image-based) model and prediction logic here
    if 'image' not in request.files:
        return render_template('malaria.html', message='No image file selected')
    
    # file = request.files['image']
    # Process the image and predict
    # pred = malaria_model.predict(processed_image)
    pred = 0 # Placeholder value
    return render_template('malaria_predict.html', pred=pred)

# --- Pneumonia Prediction ---
@app.route('/pneumonia')
def pneumoniaPage():
    return render_template('pneumonia.html')

@app.route('/pneumoniapredict', methods=['POST'])
def pneumoniapredictPage():
    # TODO: Add your pneumonia (image-based) model and prediction logic here
    if 'image' not in request.files:
        return render_template('pneumonia.html', message='No image file selected')

    # file = request.files['image']
    # Process the image and predict
    # pred = pneumonia_model.predict(processed_image)
    pred = "Normal" # Placeholder value
    return render_template('pneumonia_predict.html', pred=pred)


# --- Other Routes (No changes needed here) ---
@app.route('/egfr')
def egfrPage():
    return render_template('egfr.html')

@app.route('/egfr/calculate', methods=['POST'])
def calculate_egfr():
    """
    Basic CKD-EPI (2009) formula without race coefficient.
    """
    try:
        creatinine = float(request.form.get('creatinine', '').strip())
        age = float(request.form.get('age', '').strip())
        sex = request.form.get('sex', 'Male')

        if creatinine <= 0 or age <= 0:
            raise ValueError("Values must be positive")

        if sex.lower() == 'female':
            k = 0.7
            alpha = -0.329
            sex_multiplier = 1.018
        else:
            k = 0.9
            alpha = -0.411
            sex_multiplier = 1.0

        scr_k = creatinine / k
        egfr = 141 * min(scr_k, 1) ** alpha * max(scr_k, 1) ** (-1.209) * (0.993 ** age) * sex_multiplier
        egfr = round(egfr, 2)

        return render_template('egfr.html', egfr_value=egfr)
    except Exception as e:
        return render_template('egfr.html', egfr_error=f"Unable to calculate eGFR: {e}")

if __name__ == "__main__":
    app.run(debug=True)