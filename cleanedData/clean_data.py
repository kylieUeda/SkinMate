import pandas as pd

# read csv file
df = pd.read_csv("dataset/product_info.csv")

# Get the info
print(df.info())