import pandas as pd
df = pd.read_csv("train.csv")
survival_rate_by_sex = df.groupby("Sex")["Survived"].mean()
print("Average survival rate by sex:")
print(survival_rate_by_sex)
