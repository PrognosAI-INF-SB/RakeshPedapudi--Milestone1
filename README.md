

# PrognosAI: AI-Driven Predictive Maintenance

![Project Banner](https://img.shields.io/badge/Status-Active-green) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

---



## 📌 Project Overview

**PrognosAI** is an advanced AI-based predictive maintenance system designed to revolutionize industrial machinery management. Using **time-series sensor data**, this project estimates the **Remaining Useful Life (RUL)** of critical machinery to reduce downtime, improve efficiency, and cut maintenance costs.

This system leverages cutting-edge deep learning models (LSTM & GRU) trained on real-world datasets, enabling data-driven, proactive maintenance scheduling for industries worldwide.

---

## 🎯 Project Objective

* **Predict Remaining Useful Life (RUL):** Use sensor data to predict when a machine might fail.
* **Enable Predictive Maintenance:** Shift from reactive maintenance to data-driven proactive maintenance.
* **Optimize Industrial Efficiency:** Reduce unplanned downtime, increase machine lifespan, and save costs.
* **Build a Scalable AI System:** Make a reusable architecture for predictive maintenance applicable across industries.

---

## 💡 Key Features

* **Data Ingestion:** Load and preprocess NASA CMAPSS time-series dataset.
* **Feature Engineering:** Apply rolling windows, normalization, and RUL calculation.
* **Model Training:** Train advanced LSTM and GRU models to predict RUL.
* **Model Evaluation:** Evaluate predictions using RMSE and visualization.
* **Maintenance Alerts:** Risk thresholding to flag potential failures early.
* **Visualization:** Interactive dashboards using Streamlit for real-time insights.

---

## 🛠 Tech Stack

| Technology          | Purpose                        |
| ------------------- | ------------------------------ |
| Python              | Core programming language      |
| Pandas, NumPy       | Data processing & manipulation |
| TensorFlow/Keras    | Deep learning models           |
| Scikit-learn        | Preprocessing & evaluation     |
| Matplotlib, Seaborn | Visualization                  |
| Streamlit           | Interactive dashboard          |
| NASA CMAPSS Dataset | Predictive maintenance dataset |

---

## 🗂 Repository Structure

```
PrognosAI/
│
├── data_fetch.py        # Data ingestion & preprocessing
├── train_model.py       # Model training (LSTM/GRU)
├── requirements.txt     # Dependencies
├── README.md            # Project description
```

---

## 📊 Workflow

1. **Data Ingestion:** Load raw sensor time-series data.
2. **Preprocessing:** Clean data, handle missing values, normalize features.
3. **Feature Engineering:** Create rolling windows and compute Remaining Useful Life (RUL).
4. **Model Training:** Train LSTM & GRU networks to learn patterns in time-series data.
5. **Model Evaluation:** Compare predicted RUL with actual values.
6. **Dashboard Visualization:** Build a real-time interface to visualize predictions and alerts.

---

## 🚀 How to Run the Project

### **Prerequisites**

* Python >= 3.8
* Git

### **Clone the Repository**

```bash
git clone https://github.com/PrognosAI-INF-SB/RakeshPedapudi.git
cd RakeshPedapudi
```

### **Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Run the Scripts**

```bash
python data_fetch.py
python train_model.py
```

---

## 📈 Future Enhancements

* Integrate more deep learning architectures for better prediction accuracy.
* Build a web-based dashboard with Streamlit for interactive usage.
* Deploy the system as a cloud-based predictive maintenance platform.
* Incorporate real-time IoT data streaming for live predictions.

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your work (`git commit -m "Description"`).
5. Push to the branch (`git push origin feature-name`).
6. Create a pull request.

---

## 📜 License

This project is licensed under the **MIT License** — see the LICENSE file for details.

---

## 📚 References

* NASA CMAPSS Dataset: [Link](https://data.nasa.gov/dataset/C-MAPSS-Aircraft-Engine-Simulation-Data/vrks-gjie)
* TensorFlow Documentation: [Link](https://www.tensorflow.org/)
* Streamlit Documentation: [Link](https://docs.streamlit.io/)

---

## 👨‍💻 About Me

I’m **Rakesh Pedapudi**, a passionate AI & Data Science enthusiast. This project is part of my journey to merge deep learning with real-world industrial applications, making maintenance smarter and more predictive.

---

