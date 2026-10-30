import pandas as pd

# Load the CSV
filename = input("Enter CSV file name: ")
df = pd.read_csv(filename)

# 1. Records and columns
print("\n--- 1. RECORDS AND COLUMNS ---")
print("Number of records:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Column names:", list(df.columns))

# 2. Missing values
print("\n--- 2. MISSING VALUES ---")
print(df.isnull().sum())

# 3. Duplicate records
print("\n--- 3. DUPLICATE RECORDS ---")
print("Number of duplicate rows:", df.duplicated().sum())
print(df[df.duplicated(keep=False)])

# 4. Data types
print("\n--- 4. DATA TYPES ---")
print(df.dtypes)

# 5. Basic statistics
print("\n--- 5. BASIC STATISTICS ---")
print(df.describe())

# 6. Invalid values
print("\n--- 6. INVALID VALUES ---")
number_columns = df.select_dtypes(include="number").columns

for col in number_columns:
    negative = df[df[col] < 0]
    if len(negative) > 0:
        print(f"Column '{col}' has {len(negative)} negative value(s):")
        print(negative[col].tolist())

# Age should be between 0 and 120
if "age" in df.columns:
    bad_age = df[(df["age"] < 0) | (df["age"] > 120)]
    print("Invalid ages:", bad_age["age"].tolist())

# 7. Useful summaries
print("\n--- 7. USEFUL SUMMARIES ---")

# Count of each value in text columns
text_columns = df.select_dtypes(exclude="number").columns
for col in text_columns:
    if df[col].nunique() <= 10:
        print(f"\nValue counts for '{col}':")
        print(df[col].value_counts())

# Min, max, mean of number columns
print("\nMin / Max / Mean of number columns:")
for col in number_columns:
    print(col, "->", df[col].min(), "/", df[col].max(), "/", round(df[col].mean(), 2))

print("\nDone!")