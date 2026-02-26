# 🔋 Battery State of Health (SOH) Prediction

A Machine Learning-based web application for predicting the State of Health (SOH) of Lithium-ion batteries using NASA battery degradation data.

Deployed using Streamlit and hosted on Streamlit Cloud.

---

## 📌 Project Overview

Battery State of Health (SOH) is a key indicator of battery performance and remaining life. Accurate SOH estimation is critical for:

- Electric Vehicles (EVs)
- Battery Management Systems (BMS)
- Energy Storage Systems
- Predictive Maintenance

This project uses Machine Learning to estimate SOH based on battery cycle and capacity features.

---

## 📊 Dataset

Source: NASA Prognostics Center of Excellence (PCoE)  
Dataset: Li-ion Battery Aging Dataset  

The dataset contains:
- Charge and discharge cycles
- Capacity degradation data
- Voltage and temperature measurements
- End-of-life information

SOH is calculated as:

SOH = Current Capacity / Rated Capacity

---

## 🧠 Model Used

### Random Forest Regressor

Features:
- Cycle Number
- Rolling Mean Capacity
- Rolling Standard Deviation

Why Random Forest?
- Handles nonlinear degradation patterns
- Robust to noise
- Performs well on time-based degradation data

---

## 🌐 Web Application

Built using:

- Streamlit
- Scikit-learn
- NumPy
- Pandas

Features:
- User input for battery cycle parameters
- Real-time SOH prediction
- SOH degradation trend visualization

---

## 🚀 Live Demo

👉 [View Live App](https://your-streamlit-link.streamlit.app)

*(Replace with your deployed Streamlit link)*

---

## 📁 Project Structure
battery-soh-dashboard/
│
├── app.py
├── rf_model.pkl
├── requirements.txt
├── .gitignore
└── README.md

---

## ⚙️ How to Run Locally

1. Clone the repository:
git clone https://github.com/khushii0504/battery-soh-dashboard.git

cd battery-soh-dashboard

2. Create virtual environment:
python3 -m venv venv
source venv/bin/activate


3. Install dependencies:
pip install -r requirements.txt

4. Run the app:

---

## 📈 Future Improvements

- Add LSTM-based deep learning model
- Remaining Useful Life (RUL) prediction
- Multi-battery training
- Upload .mat file directly in app
- Model comparison dashboard

---

## 👩‍💻 Author

Khushi Sharma  
Machine Learning & Energy Systems Enthusiast  

---

## 📜 License

This project is for educational and research purposes.
