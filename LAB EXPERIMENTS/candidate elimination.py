import pandas as pd

# Load the dataset
data = pd.read_csv("luxury_cars.csv")

# Separate attributes and target
concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

# Initialize Specific Hypothesis with the first positive example
for i in range(len(target)):
    if target[i].lower() == "yes":
        S = concepts[i].copy()
        break

# Initialize General Hypothesis
G = [["?" for _ in range(len(S))] for _ in range(len(S))]

print("Initial Specific Hypothesis:")
print(S)

print("\nInitial General Hypothesis:")
for g in G:
    print(g)

# Candidate Elimination Algorithm
for i, h in enumerate(concepts):

    if target[i].lower() == "yes":
        # Positive Example
        for j in range(len(S)):
            if h[j] != S[j]:
                S[j] = "?"
                G[j][j] = "?"

    else:
        # Negative Example
        for j in range(len(S)):
            if h[j] != S[j]:
                G[j][j] = S[j]
            else:
                G[j][j] = "?"

    print(f"\nAfter Training Example {i+1}:")
    print("Specific Hypothesis:")
    print(S)

    print("General Hypothesis:")
    for g in G:
        print(g)

# Remove overly general hypotheses
final_G = [g for g in G if g != ["?" for _ in range(len(S))]]

print("\n==========================")
print("Final Specific Hypothesis:")
print(S)

print("\nFinal General Hypothesis:")
for g in final_G:
    print(g)

print("Name   : Dhinakaran S")
print("Reg No : 192412353")