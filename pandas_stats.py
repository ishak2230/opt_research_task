import pandas as pd


# Load the dataset
filename = "fb_ads_president_scored_anon.csv"
df = pd.read_csv(filename)


# Display basic dataset information
print("Dataset Structure")
print("-" * 50)
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nData Types")
print(df.dtypes)

print("\nDataset Info")
df.info()


# Summary statistics
print("\nNumeric Summary Statistics")
print(df.describe())

print("\nCategorical Summary Statistics")
print(df.describe(include=["object"]))


# Missing values
print("\nMissing Values")
missing = pd.DataFrame({
    "Missing Count": df.isnull().sum(),
    "Missing Percentage": (df.isnull().sum() / len(df)) * 100
})

print(missing)


# Categorical column analysis
print("\nCategorical Column Analysis")

categorical_columns = df.select_dtypes(include=["object"]).columns

for column in categorical_columns:

    print("\n" + "=" * 60)
    print(f"Column: {column}")

    print(f"Unique Values: {df[column].nunique()}")

    print("Top 5 Values:")

    print(df[column].value_counts().head(5))
