from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample student data
X = [
    [1, 40, 10],
    [2, 50, 15],
    [3, 60, 20],
    [4, 65, 25],
    [5, 75, 30],
    [6, 80, 35],
    [7, 90, 40],
    [8, 95, 45],
    [2, 45, 12],
    [6, 85, 38]
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 0, 1]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained and saved successfully")