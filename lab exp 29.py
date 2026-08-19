# Decision Tree Classification - Iris Dataset

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load Iris dataset
iris = load_iris()

# Separate input features and target
X = iris.data
y = iris.target

# Create Decision Tree classifier
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X, y)

# Get input from user
print("Enter the measurements of the new flower:")

sepal_length = float(input("Sepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

# Store the input values
new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]

# Predict the species
prediction = model.predict(new_flower)

# Display the predicted species
print("\nPredicted Iris Species:",
      iris.target_names[prediction[0]])
