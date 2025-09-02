import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_dataset.csv")
X = df["YearsExperience"].values.reshape(-1, 1)
Y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

plt.figure(figsize=(10, 8))
plt.scatter(X_train, y_train, c='blue', label='Training Data')
plt.scatter(X_test, y_test, c='red', label='Testing Data')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Original Salary Data Distribution')
plt.legend()
plt.grid(True)
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
plt.title("Linear Regression Model for Salary Prediction (Original Data)")
plt.legend()
plt.grid(True)
plt.show()

new_data = pd.DataFrame({'YearsExperience': [19], 'Salary': [27e5]})
df_with_outlier = pd.concat([df, new_data], ignore_index=True)

X_outlier = df_with_outlier["YearsExperience"].values.reshape(-1, 1)
Y_outlier = df_with_outlier['Salary'].values

X_train_out, X_test_out, y_train_out, y_test_out = train_test_split(
    X_outlier, Y_outlier, test_size=0.2, random_state=1
)

model_linear = LinearRegression()
model_linear.fit(X_train_out, y_train_out)

y_train_pred_linear = model_linear.predict(X_train_out)
y_test_pred_linear = model_linear.predict(X_test_out)

train_mse_linear = mean_squared_error(y_train_out, y_train_pred_linear)
test_mse_linear = mean_squared_error(y_test_out, y_test_pred_linear)

print(f"\nLinear Regression with Outlier - Training MSE: {train_mse_linear:.2f}")
print(f"Linear Regression with Outlier - Test MSE: {test_mse_linear:.2f}")

alphas = [1, 10, 100, 1000, 10000]
ridge_models = {}

for alpha in alphas:
    model_ridge = Ridge(alpha=alpha, random_state=1)
    model_ridge.fit(X_train_out, y_train_out)
    
    y_train_pred_ridge = model_ridge.predict(X_train_out)
    y_test_pred_ridge = model_ridge.predict(X_test_out)
    
    train_mse_ridge = mean_squared_error(y_train_out, y_train_pred_ridge)
    test_mse_ridge = mean_squared_error(y_test_out, y_test_pred_ridge)
    
    ridge_models[alpha] = {
        'model': model_ridge,
        'train_mse': train_mse_ridge,
        'test_mse': test_mse_ridge,
        'coefficient': model_ridge.coef_[0]
    }
    
    print(f"Ridge Regression (α={alpha}) - Training MSE: {train_mse_ridge:.2f}, Test MSE: {test_mse_ridge:.2f}")

plt.figure(figsize=(12, 8))

plt.scatter(X_train, y_train, c='blue', alpha=0.6, s=50, label='Original Training Data')
plt.scatter(X_test, y_test, c='green', alpha=0.6, s=50, label='Original Test Data')

plt.scatter([19], [27e5], c='red', s=200, marker='*', label='Outlier (Mark Zuckerberg)')

plt.plot(x_range, model_linear.predict(x_range), 'r-', linewidth=2, 
         label=f'Linear Regression (Coeff={model_linear.coef_[0]:.2f}, MSE={train_mse_linear:.0f})')

colors = ['purple', 'brown', 'olive', 'teal', 'navy']
for i, alpha in enumerate(alphas):
    plt.plot(x_range, ridge_models[alpha]['model'].predict(x_range), 
             colors[i], linestyle='--', linewidth=1.5,
             label=f'Ridge (α={alpha}, Coeff={ridge_models[alpha]["coefficient"]:.2f}, MSE={ridge_models[alpha]["train_mse"]:.0f})')

plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Linear Regression vs Ridge Regression with Outlier')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.show()