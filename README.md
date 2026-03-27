# Automotive Intrusion Detection System (IDS)

## Project Overview
This project implements a real-time Intrusion Detection System (IDS) for automotive networks based on the Controller Area Network (CAN) protocol. It detects cyber-attacks such as Denial of Service (DoS), Replay, and Fuzzing attacks and visualizes them using an interactive dashboard.

---

## Objectives
- Simulate real-time CAN bus communication  
- Detect malicious messages using IDS techniques  
- Classify attack types (DoS, Replay, Fuzzing)  
- Provide live monitoring through an industry-style dashboard  

---

## Key Features
- Real-time CAN message simulation  
- Attack detection system  
- Live dashboard with:
  - Total messages & attack count  
  - Live attack graph  
  - Attack type display  
  - Attack distribution (pie chart)  
  - Recent attack history table  
- Event-based attack detection (burst handling)  
- Performance metrics (Accuracy, Precision, Recall)

---

## Dataset

Dataset is NOT included due to GitHub file size limitations.

Download from:  
https://figshare.com/articles/dataset/Automotive_Controller_Area_Network_CAN_Bus_Intrusion_Dataset/12696950

### After downloading:
Extract and place inside:

IDS/data/

---

## Installation & Setup

### 1. Clone Repository

git clone https://github.com/pr1t03/IDS.git  
cd IDS

---

### 2. Install Dependencies

pip install pandas scikit-learn flask requests

---

### 3. Add Dataset
- Download dataset  
- Place inside `/data` folder  

---

## How to Run

### Step 1: Preprocess Data

python preprocess.py

---

### Step 2: Start Dashboard Server

python dashboard/app.py

---

### Step 3: Run IDS System (in new terminal)

python main.py

---

### Step 4: Open Dashboard

http://localhost:5001

---

## How It Works

1. CAN log dataset is preprocessed  
2. Messages are streamed in real-time  
3. IDS analyzes each message  
4. Attacks are detected and classified  
5. Dashboard displays live results  

---

## Attack Types Detected

- DoS (Denial of Service) – High-frequency message flooding  
- Replay Attack – Repeated valid messages  
- Fuzzing Attack – Random data injection  

---

## Evaluation Metrics

- Accuracy  
- Precision  
- Recall  

---

## Real-World Relevance

Modern vehicles use CAN protocol, which lacks built-in security.  
This project simulates how automotive IDS systems detect and prevent cyber-attacks in real vehicles.

---

## Notes

- Dataset is large and must be downloaded separately  
- Ensure correct folder structure before running  
- Default dashboard runs on port 5001  

---

## Author

Developed as part of a Computer Science & Engineering project on 'Cybersecurity in Automotive Vehicle'.

---

## License

This project is for educational purposes only.
