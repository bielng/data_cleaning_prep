# main.py
# import kagglehub
# import os

# # Download the dataset (this returns the local folder path)
# handle = "ratnarohith/uncleaned-bike-sales-data"
# path = kagglehub.dataset_download(handle)

# print("Dataset downloaded to:", path)

# # List files inside to see what’s there (very useful first time)
# print("Files in dataset:", os.listdir(path))

# # The actual CSV file name in this dataset is "bike_sales_data_uncleaned.csv"
# csv_file = "bike_sales_data_uncleaned.csv"   # correct filename
# csv_path = os.path.join(path, csv_file)

# # Load it with pandas
# import pandas as pd
# df = pd.read_csv(csv_path)

# print("Shape:", df.shape)
# print("\nFirst 5 records:")
# print(df.head())

# # Optional: quick info
# print("\nColumns:", df.columns.tolist())


df = pd.read_csv(r'')
df.head()
df.tail()
display(df.describe())