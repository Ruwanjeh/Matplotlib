import pandas as pd

# Load the dataset (for example, the Iris dataset or any CSV file)
try:
    df = pd.read_csv('path_to_your_dataset.csv')  # Replace with your dataset path
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("File not found. Please check the path.")

# Display the first few rows of the dataset
print(df.head())

# Explore the structure of the dataset
print("Data types of columns:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())

# Clean the dataset by filling missing values (if any)
# For example, filling numeric columns with the median or dropping rows
df.fillna(df.median(), inplace=True)  # Fill missing values with median for numeric columns
# Alternatively, you can drop rows with missing values:
# df.dropna(inplace=True)

print("\nCleaned dataset preview:\n", df.head())
