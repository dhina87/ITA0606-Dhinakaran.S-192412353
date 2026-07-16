import csv
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder

# Read CSV file
X = []
y = []

with open("buy_computer.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header

    for row in reader:
        X.append(row[:-1])   # Features
        y.append(row[-1])    # Target

# Encode categorical features
encoders = []

for i in range(len(X[0])):
    le = LabelEncoder()
    column = [row[i] for row in X]
    encoded = le.fit_transform(column)

    for j in range(len(X)):
        X[j][i] = encoded[j]

    encoders.append(le)

# Encode target
target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

# Train ID3 Decision Tree
model = DecisionTreeClassifier(criterion="entropy", random_state=42)
model.fit(X, y)

# Display Decision Tree
print("Decision Tree:\n")
print(export_text(model, feature_names=header[:-1]))

# New sample
new_sample = ["Youth", "Medium", "Yes", "Fair"]

# Encode new sample
for i in range(len(new_sample)):
    new_sample[i] = encoders[i].transform([new_sample[i]])[0]

# Predict
prediction = model.predict([new_sample])

print("\nPrediction:")
print("Buy Computer =", target_encoder.inverse_transform(prediction)[0])

print("\nName   : Dhinakaran S")
print("Reg No : 192412353")