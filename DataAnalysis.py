# Basic statistics of numerical columns
print("Basic statistics of numerical columns:\n", df.describe())

# Grouping by a categorical column and computing the mean of a numerical column
# For example, if 'species' is a categorical column and 'petal_length' is numerical
grouped = df.groupby('species')['petal_length'].mean()
print("\nAverage petal length per species:\n", grouped)

# You can explore more groupings and compute other statistics like sum, median, etc.
