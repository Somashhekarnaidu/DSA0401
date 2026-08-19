import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("patients.csv")

print("Patient Dataset:")
print(df)

X = df[["Fever", "Cough", "Fatigue", "BodyPain", "Headache"]]
y = df["Condition"]

k = int(input("\nEnter value of K: "))

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X, y)

print("\nEnter New Patient Symptoms")

fever = int(input("Fever (0/1): "))
cough = int(input("Cough (0/1): "))
fatigue = int(input("Fatigue (0/1): "))
bodypain = int(input("Body Pain (0/1): "))
headache = int(input("Headache (0/1): "))

new_patient = pd.DataFrame(
    [[fever, cough, fatigue, bodypain, headache]],
    columns=["Fever", "Cough", "Fatigue", "BodyPain", "Headache"]
)

prediction = model.predict(new_patient)[0]

print("\nPrediction:")

if prediction == 1:
    print("Patient has the medical condition")
else:
    print("Patient does not have the medical condition")
