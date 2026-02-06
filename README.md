## 📌 Project Overview

Liver disease is a serious health concern, and early diagnosis plays a crucial role in effective treatment. This project presents a **machine learning–based binary classification system** that predicts whether a person is likely to have liver disease based on clinical and biochemical parameters.

The system is trained using the **Indian Liver Patient Dataset (ILPD)** and deployed as an **interactive web application using Streamlit**, allowing users to input patient data and receive real-time predictions.

---

## 🎯 Objectives

* To analyze and preprocess liver patient data
* To build and evaluate multiple machine learning models
* To perform binary classification (Disease / No Disease)
* To deploy the trained model as a web-based application
* To provide an easy-to-use interface for prediction

---

## 📊 Dataset Description

* **Dataset Name:** Indian Liver Patient Dataset (ILPD)
* **Total Records:** 583
* **Features:** 10 medical attributes
* **Target Variable:**

  * `1` → Liver Disease
  * `0` → No Liver Disease

### Input Features:

* Age
* Gender
* Total Bilirubin
* Direct Bilirubin
* Alkaline Phosphotase
* Alamine Aminotransferase (ALT)
* Aspartate Aminotransferase (AST)
* Total Proteins
* Albumin
* Albumin and Globulin Ratio

---

## ⚙️ Methodology

1. **Data Preprocessing**

   * Handling missing values
   * Encoding categorical variables
   * Feature scaling using StandardScaler

2. **Model Training**

   * Logistic Regression
   * Support Vector Machine (SVM)
   * Random Forest Classifier

3. **Model Evaluation**

   * Accuracy
   * Precision
   * Recall
   * F1-score
   * Confusion Matrix

4. **Model Deployment**

   * Best-performing model saved using serialization
   * Deployed via Streamlit Cloud

---

##  Model Performance (Sample)

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | ~73%     |
| SVM                 | ~71%     |
| Random Forest       | ~72%     |

Logistic Regression was selected due to its balanced performance and high recall.

---

## 🖥️ Web Application (Streamlit)

The deployed application allows users to:

* Enter patient medical details
* Click **Predict**
* Instantly view whether liver disease is detected

### Prediction Output:

* ⚠️ Liver Disease Detected
* ✅ No Liver Disease Detected

---

## 📁 Project Structure

```
binary_classification_ml/
│
├── app.py                     # Streamlit web app
├── indian_liver_patient.csv   # Dataset
├── liver_model.pkl            # Trained ML model
├── scaler.pkl                 # Feature scaler
├── src.ipynb                  # Model training notebook
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/RISHAV2205/Binary_classification_ML
cd IEDC
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The application is deployed using **Streamlit Cloud**, enabling public access through a web browser without any local setup.
LINK: https://binaryclassificationml.streamlit.app/
---

## 🏁 Conclusion

This project demonstrates the practical application of machine learning in the healthcare domain. By integrating data preprocessing, model training, evaluation, and deployment, the system provides a complete end-to-end solution for liver disease prediction.

---

## 🔮 Future Enhancements

* Integration of deep learning models
* Use of larger and more diverse datasets
* Explainable AI (XAI) for medical interpretation
* Integration with hospital or clinical systems

---

## 👨‍💻 Author

**Rishav Poddar**
Student | 
---

