import pandas as pd

df = pd.read_excel(r"C:\Users\Lanyi\Desktop\Project\Python_Program\Data_analysis\Documents\23工程管理本科1班.xls")

print(df.head())

print("\nData Types:\n", df.dtypes)

numeric_df = df.select_dtypes(include=['number'])

score_rate = numeric_df.mean() / numeric_df.max()

print("\nScore Rate (mean/max):\n", score_rate)

output_path = r"C:\Users\Lanyi\Desktop\Project\Python_Program\Data_analysis\Documents\score_rate.xlsx"
score_rate.to_excel(output_path, sheet_name="Score Rate")

print(f"\nScore rate has been saved to: {output_path}")
