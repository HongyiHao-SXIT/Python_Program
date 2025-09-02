import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_dataset.csv") 
X = df["YearsExperience"].values
X = X.reshape(-1,1) 
Y = df['Salary']

from sklearn.model_selection import train_test_split 
 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)


plt.figure(figsize=(10, 8))
plt.scatter(X_train, y_train, c='blue', label='Training')
plt.scatter(X_test, y_test, c='red', label='Testing')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()


model = LinearRegression()


model.fit(X_train, y_train)

print(f"Model Intercept: {model.intercept_}")
print(f"Model Coefficient: {model.coef_[0]}")


y_train_pred = model.predict(X_train)
train_mse = mean_squared_error(y_train, y_train_pred)
print(f"Training Set MSE: {train_mse:.2f}")


y_test_pred = model.predict(X_test)
test_mse = mean_squared_error(y_test, y_test_pred)
print(f"Test Set MSE: {test_mse:.2f}")

plt.figure(figsize=(10, 8))


plt.scatter(X_train, y_train, c='blue', label='Training Data')


x_range = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)
plt.plot(x_range, model.predict(x_range), 'r-', label='Regression Line')

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression Model for Salary Prediction")
plt.legend()
plt.grid(True)
plt.show()