# Chronic-Kidney-Disease-Prediction

This web application was developed using the **Flask** web framework. The predictive models were trained on comprehensive datasets, enabling high accuracy in predicting chronic kidney disease.

## Steps to Run This Application on Your System

1. **Clone or download the repository**:

```bash
git clone https://github.com/Karthi-blip/CKD-B.TECH.git
```

2. Change directory

```bash
cd CKD-B.TECH
```

3 .Create a virtual environment:

```bash
python3 -m venv ckd-env
```

4. Activate the virtual environment:

# On macOS/Linux:

```bash
source ckd-env/bin/activate
```

# On Windows:

```bash
ckd-env\Scripts\activate
```

5. Install necessary packages:

```bash
pip install pandas numpy
```

6. Install all dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

7. Run the Flask application:

```bash
python3 app.py
```

8. Open your browser and navigate to:

```bash
http://127.0.0.1:5000/
```
Dataset

**The dataset used is from Kaggle**:

Kidney Disease Dataset

Models and Accuracy of Prediction
Disease	Type of Model	Accuracy
Kidney Disease	Machine Learning Model	98.33%

## CKD Prediction Project Screenshots

### Home Page
![Home Page](assets/home_page.png)

The **Home Page** is the main interface of the CKD Prediction web application.  
- Users can enter patient details such as age, blood pressure, sugar levels, and other medical parameters.  
- The form collects all necessary inputs required by the predictive model.  
- After filling the form, users can click the **Predict** button to get CKD prediction results.

### Result Page
![Result Page](assets/result_page.png)

The **Result Page** displays the outcome of the CKD prediction.  
- It shows whether the patient is predicted to have chronic kidney disease (`CKD`) or not (`Not CKD`).  
- The page also highlights key input parameters for reference.  
- Users can navigate back to the Home Page to perform another prediction.