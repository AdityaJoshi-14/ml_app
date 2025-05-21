# ~/joshidata/ml_app/src/predict_tallness.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load the dataset
data = pd.read_csv('data/heights.csv')

# Separate features and labels
X = data[['height']].values
y = data['tall'].values

# Scale the height values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the logistic regression model
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# Evaluate the model
y_pred = lr_model.predict(X_test)
accuracy = sum(y_pred == y_test) / len(y_test)
print(f"Accuracy on test set: {accuracy:.2f}")

# Get user input for prediction
try:
    user_input = float(input("Enter height in inches to predict if the person is tall: "))
    user_input_scaled = scaler.transform([[user_input]])
    predicted_tall = lr_model.predict(user_input_scaled)[0]
    print(f"Predicted label for height {user_input} inches: {'Tall' if predicted_tall else 'Not Tall'}")
except ValueError:
    print("Invalid input. Please enter a numeric value for height.")

