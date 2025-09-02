import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("23工程管理本科1班.xls", engine="xlrd")

questions = df.iloc[:, 2:]

full_mark = 1  
rates = questions.mean(axis=0) / full_mark * 100

plt.figure(figsize=(10, 6))
plt.plot(rates.index, rates.values, marker="o")
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.title("每道题得分率")
plt.xlabel("题号")
plt.ylabel("得分率 (%)")
plt.grid(True)
plt.show()
