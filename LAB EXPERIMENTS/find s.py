import pandas as pd

# Load the dataset
data = pd.read_csv("luxury_cars.csv")

# Separate attributes and target
concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

# Find the first positive example
for i in range(len(target)):
    if target[i].lower() == "yes":
        S = concepts[i].copy()
        break

print("Initial Specific Hypothesis:")
print(S)

# Find-S Algorithm
for i in range(len(concepts)):
    if target[i].lower() == "yes":
        for j in range(len(S)):
            if concepts[i][j] != S[j]:
                S[j] = "?"

        print("\nAfter Positive Example", i + 1)
        print(S)

print("\n==========================")
print("Final Specific Hypothesis:")
print(S)

print("Name   : Dhinakaran S")
print("Reg No : 192412353")