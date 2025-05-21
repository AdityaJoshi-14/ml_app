# ~/joshidata/ml_app/src/model_utils.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load and preprocess the dataset once when the app starts
data = pd.read_csv('data/heights.csv')
X = data[['height']].values
y = data['tall'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

def predict_tallness(height: float) -> str:
    scaled = scaler.transform([[height]])
    prediction = lr_model.predict(scaled)[0]
    return "Tall" if prediction == 1 else "Not Tall"

