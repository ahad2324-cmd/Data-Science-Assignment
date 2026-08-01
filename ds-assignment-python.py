import pandas as pd


# Task: Find a CSV file from the internet
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Task: Load a CSV dataset
print("Loading dataset...")
df = pd.read_csv(url)

# Task: Display first 5 rows
print("\n--- First 5 rows ---")
print(df.head(5))

# Task: Show column names
print("\n--- Column names ---")
print(df.columns.tolist())

# Task: Display number of rows and columns
print("\n--- Number of rows and columns (Rows, Columns) ---")
print(df.shape)

# Task: Show summary statistics
print("\n--- Summary statistics ---")
print(df.describe())


# Task: Create a new column 'Average Score'
# (Using 'Age' and 'Fare' as placeholder numeric columns to average)
df['Average Score'] = (df['Age'] + df['Fare']) / 2

# Task: Apply a condition, if true then decide to do some action
# (Action: Create a 'Status' column. If Average Score > 30, status is 'High', else 'Low')
df['Status'] = df['Average Score'].apply(lambda x: 'High' if x > 30 else 'Low')

print("\n--- Data after Assignment 2 (First 5 rows) ---")
print(df[['Age', 'Fare', 'Average Score', 'Status']].head())


df_sorted = df.sort_values(by='Average Score', ascending=True)

print("\n--- Data sorted by Average Score in ascending order (First 5 rows) ---")
print(df_sorted[['Average Score', 'Status']].head())