import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler

print("=======================================================")
print("🔄 RUNNING SYNTHETIC TELEMETRY GENERATION ENGINE...")
print("=======================================================")

np.random.seed(42)
num_rows = 12000

ph = np.random.uniform(5.0, 10.0, num_rows)
temp = np.random.uniform(20.0, 35.0, num_rows)
turbidity_v = np.random.uniform(0.8, 1.4, num_rows)
dissolved_oxygen = np.random.uniform(1.0, 9.0, num_rows)
distance_cm = np.random.uniform(1.0, 25.0, num_rows)

threat_label = np.zeros(num_rows, dtype=int)

for i in range(num_rows):
    critical_ph = (ph[i] < 6.0 or ph[i] >= 8.5)
    critical_do = (dissolved_oxygen[i] < 3.0)
    critical_turb = (turbidity_v[i] > 1.25)
    critical_lvl = (distance_cm[i] <= 5.0)

    if critical_ph or critical_do or critical_turb or critical_lvl:
        threat_label[i] = 1
        if np.random.rand() < 0.02: 
            threat_label[i] = 0
    else:
        if np.random.rand() < 0.01:  
            threat_label[i] = 1

df = pd.DataFrame({
    'pH': np.round(ph, 2),
    'Temperature': np.round(temp, 1),
    'Turbidity_V': np.round(turbidity_v, 2),
    'Dissolved_Oxygen': np.round(dissolved_oxygen, 1),
    'Distance_CM': np.round(distance_cm, 1),
    'Threat_Label': threat_label
})

dataset_file = "water_quality_dataset.csv"
df.to_csv(dataset_file, index=False)
print(f"✅ Success! Matrix profiles saved to: {dataset_file}\n")


print("=======================================================")
print("🧠 INITIATING EMBEDDED MODEL OPTIMIZATION TRAINING...")
print("=======================================================")

data = pd.read_csv(dataset_file)
X = data[['pH', 'Temperature', 'Turbidity_V', 'Dissolved_Oxygen', 'Distance_CM']].values
y = data['Threat_Label'].values

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X_scaled, y)

weights = model.coef_[0]
bias = model.intercept_[0]

print("\n🚀 EDGE-AI MATRIX WEIGHT PARAMETERS GENERATED SUCCESSFULLY!")
print("-------------------------------------------------------")
print("Copy and replace these variables into your Pico W main.py script:\n")
print(f"AI_W1 = {list(np.round(weights, 4))}")
print(f"AI_B1 = {round(bias, 4)}")
print("=======================================================\n")
