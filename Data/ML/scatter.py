from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict
predictions = model.predict(X)

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, predictions, color='red')
plt.title('Linear Regression Example')
plt.show()
