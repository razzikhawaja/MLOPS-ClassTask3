import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model to a file using joblib
joblib.dump(model, 'model.pkl')

print("Model saved as model.pkl")
