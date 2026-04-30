# 🏠 House Price Prediction App

A Machine Learning web application that predicts house prices based on user inputs like location, income, population, and housing details.

---

## 📌 Project Overview

This project uses a trained Machine Learning model to estimate housing prices using real-world housing data.

The system includes:
- Data preprocessing pipeline
- Feature engineering
- Machine learning model training
- Deployment using Streamlit

It is designed as a **production-ready ML web app**.

---

## 🚀 Features

- 📊 Real-time house price prediction
- 🤖 ML model: HistGradientBoostingRegressor
- 🔄 Separate preprocessing pipeline (avoids data leakage)
- 🖥️ Interactive UI using Streamlit
- ⚡ Fast prediction response
- 🌍 Location-based prediction inputs

---

## 🧠 Tech Stack

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib & Seaborn (EDA)

---

## 📂 Project Structure


├── app.py # Streamlit web application
├── model.pkl # Trained ML model
├── preprocess.pkl # Preprocessing pipeline
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files


---

## 🧪 Machine Learning Workflow

### 1. Data Preprocessing
- Missing value handling using median/mode
- One-hot encoding for categorical features
- Feature scaling using StandardScaler

### 2. Model Training
- Multiple models tested:
  - Linear Regression
  - Ridge
  - Random Forest
  - HistGradientBoostingRegressor (Best)

### 3. Model Selection
- Selected based on lowest RMSE using Cross Validation

### 4. Final Model
- HistGradientBoostingRegressor
- Tuned using GridSearchCV

---

## ▶️ How to Run Locally

### 1. Clone the repository
git clone https://github.com/vkhushi9458-design/house-price-prediction.git
cd house-price-prediction
### 2. Install dependencies
pip install -r requirements.txt
### 3. Run the Streamlit app
streamlit run app.py

---

### 📸 App Preview
![alt text](<Screenshot 2026-04-30 183211.png>)

### 📈 Future Improvements
Add map visualization for location-based pricing 🌍
Improve model using XGBoost / LightGBM 🚀
Add feature importance graph 📊
Deploy with Docker 🐳

#### 👩‍💻 Author

Khushi Verma
B.Voc (Internet of Things) Student
Aspiring AI/ML & Python Developer 🚀