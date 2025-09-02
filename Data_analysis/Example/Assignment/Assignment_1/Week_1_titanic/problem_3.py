import pandas as pd

df = pd.read_csv("train.csv")
df.fillna(0, inplace=True)

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

print("Numerical Columns:")
print(numerical_columns)

print("\nCategorical Columns:")
print(categorical_columns)

df_encoded = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

print("\nFirst 5 rows after one-hot encoding:")
print(df_encoded.head())

df['Age'] = df['Age'].fillna(df['Age'].median())

df['Age'] = df.groupby('Pclass')['Age'].transform(lambda x: x.fillna(x.median()))


from sklearn.ensemble import RandomForestRegressor

age_df = df[['Age', 'Pclass', 'Sex', 'SibSp', 'Parch', 'Fare']]
age_df = pd.get_dummies(age_df)

known_age = age_df[age_df['Age'].notnull()]
unknown_age = age_df[age_df['Age'].isnull()]

X_train = known_age.drop('Age', axis=1)
y_train = known_age['Age']
X_pred = unknown_age.drop('Age', axis=1)

rfr = RandomForestRegressor(random_state=0, n_estimators=100)
rfr.fit(X_train, y_train)
df.loc[df['Age'].isnull(), 'Age'] = rfr.predict(X_pred)


df['Age_missing'] = df['Age'].isnull().astype(int)

