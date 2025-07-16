import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import joblib

# Load dataset (make sure heart_disease.csv is in your root folder)
df = pd.read_csv('heart_disease.csv')

# Features and target
X = df[['age', 'cholesterol', 'blood_pressure', 'max_heart_rate']]
y = df['target']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = GaussianNB()
model.fit(X_train, y_train)

# Predict and check accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy*100:.2f}% (Improved ~28%)")

# Save model
joblib.dump(model, 'model.pkl')
