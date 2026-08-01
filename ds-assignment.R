
url <- "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Task: Load a CSV dataset
cat("Loading dataset...\n")
df <- read.csv(url)

# Task: Display first 5 rows
cat("\n--- First 5 rows ---\n")
print(head(df, 5))

# Task: Show column names
cat("\n--- Column names ---\n")
print(colnames(df))

# Task: Display number of rows and columns
cat("\n--- Number of rows and columns (Rows, Columns) ---\n")
print(dim(df))

# Task: Show summary statistics
cat("\n--- Summary statistics ---\n")
print(summary(df))


# ==========================================
# Assignment 2: Creating New Columns
# ==========================================

# Task: Create a new column 'Average Score'
# (Using 'Age' and 'Fare' as placeholder numeric columns to average)
df$Average_Score <- (df$Age + df$Fare) / 2

# Task: Apply a condition, if true then decide to do some action
# (Action: Create a 'Status' column. If Average_Score > 30, status is 'High', else 'Low')
df$Status <- ifelse(df$Average_Score > 30, "High", "Low")

cat("\n--- Data after Assignment 2 (First 5 rows) ---\n")
print(head(df[, c("Age", "Fare", "Average_Score", "Status")], 5))


# ==========================================
# Assignment 3: Sorting Data
# ==========================================

# Task: Sort data by a specific column (ascending)
# order() function defaults to ascending orde
df_sorted <- df[order(df$Average_Score), ]

cat("\n--- Data sorted by Average Score in ascending order (First 5 rows) ---\n")
print(head(df_sorted[, c("Average_Score", "Status")], 5))
