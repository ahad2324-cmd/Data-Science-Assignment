import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

print("Loading dataset...")
df = pd.read_csv(url)

print("\n--- First 5 rows ---")
print(df.head(5))

print("\n--- Column names ---")
print(df.columns.tolist())

print("\n--- Number of rows and columns (Rows, Columns) ---")
print(df.shape)


print("\n--- Summary statistics ---")
print(df.describe())

df['Average Score'] = (df['Age'] + df['Fare']) / 2

df['Status'] = df['Average Score'].apply(lambda x: 'High' if x > 30 else 'Low')

print("\n--- Data after Assignment 2 (First 5 rows) ---")
print(df[['Age', 'Fare', 'Average Score', 'Status']].head())


df_sorted = df.sort_values(by='Average Score', ascending=True)

print("\n--- Data sorted by Average Score in ascending order (First 5 rows) ---")
print(df_sorted[['Average Score', 'Status']].head())
