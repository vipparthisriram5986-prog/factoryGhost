# 🏭 Factory Ghost
### Local AI Predictive Maintenance Assistant for Industrial Motors

Factory Ghost is a beginner-friendly industrial motor monitoring project that simulates motor sensor readings and uses a locally running AI model to explain possible warning conditions.

## ✨ Features

- Simulates motor temperature, vibration, and current.
- Detects simulated abnormal conditions using threshold rules.
- Displays readings and charts in a Streamlit dashboard.
- Uses local Gemma AI through Ollama to explain motor warnings.
- Stores simulated readings in a CSV file.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Ollama
- Gemma 2 (2B)

## 🚀 How to Run

1. Install Python and Ollama.
2. Download the Gemma model:

   `ollama run gemma2:2b`

3. Install the Python packages:

   `py -m pip install -r requirements.txt`

4. Generate simulated motor data:

   `py motor_simulator.py`

5. Start the dashboard:

   `py -m streamlit run dashboard.py`

6. Open `http://localhost:8501` in your browser.

## ⚠️ Important Note

This project uses **simulated sensor data** and example thresholds for educational purposes. It does not diagnose real industrial equipment or guarantee fault detection.

## 🌱 Open Innovation

Factory Ghost demonstrates how local AI can help explain industrial monitoring alerts without sending the readings to a cloud-based AI service. The simulator and dashboard are intended as a starting point for further experimentation.
