import pandas as pd

df = pd.read_excel(
    r"C:\Users\Lanyi\Desktop\Project\Python_Program\Data_analysis\Documents\23工程管理本科1班.xls",
    engine="xlrd"
)

print(df.head())
print("\nData Types:\n", df.dtypes)

numeric_df = df.select_dtypes(include=['number'])

score_rate = numeric_df.mean() / numeric_df.max()

score_rate_df = score_rate.reset_index()
score_rate_df.columns = ["Column", "Score Rate"]

output_path = r"C:\Users\Lanyi\Desktop\Project\Python_Program\Data_analysis\Documents\score_rate.xlsx"
score_rate_df.to_excel(output_path, sheet_name="Score Rate", index=False)

print("\nScore Rate (mean/max):\n", score_rate.round(2))
print(f"\nScore rate has been saved to: {output_path}")
