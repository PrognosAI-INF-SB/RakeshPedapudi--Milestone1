# PrognosAI: AI-Driven Predictive Maintenance

## 🔹 Project Objective
An AI-based predictive maintenance system using time-series sensor data to estimate the Remaining Useful Life (RUL) of industrial machinery.  
We will prototype using the NASA CMAPSS dataset and train deep learning models (LSTM/GRU).

## 🔹 Tech Stack
- Python
- Pandas, NumPy (data processing)
- TensorFlow/Keras (deep learning models)
- Scikit-learn (metrics & preprocessing)
- Matplotlib/Seaborn (visualization)
- Streamlit (dashboard)
- NASA CMAPSS Dataset (data source)

## 🔹 Workflow
1. Data ingestion (load & preprocess CMAPSS dataset)  
2. Feature engineering (rolling windows, RUL calculation)  
3. Model training (LSTM/GRU)  
4. Model evaluation (RMSE, predicted vs actual RUL)  
5. Risk thresholding (maintenance alerts)  
6. Visualization (dashboard)  

## 🔹 Repo Structure
- `data_fetch.py` → Load & preprocess data  
- `train_model.py` → Train LSTM/GRU model  
- `requirements.txt` → Dependencies  

---
👨‍💻 *Infosys Springboard Cohort 6.0 Internship Project*
