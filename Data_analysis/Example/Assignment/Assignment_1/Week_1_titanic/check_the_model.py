import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import accuracy_score

df = pd.read_csv("train.csv")

df['Age'] = df['Age'].fillna(0)

df.fillna(0, inplace=True)

categorical_cols = df.select_dtypes(include='object').columns.tolist()
df_encoded = pd.get_dummies(df, columns=categorical_cols)

X = df_encoded.drop("Survived", axis=1)
y = df_encoded["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

ros = RandomOverSampler(random_state=42)
X_train_resampled, y_train_resampled = ros.fit_resample(X_train, y_train)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_resampled, y_train_resampled)
y_pred = knn.predict(X_test)

test_accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy (Age filled with 0): {test_accuracy:.4f}")
