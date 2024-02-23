import pandas as pd
import numpy
import csv
import matplotlib.pyplot as plt

'''
rows = []

with open('share_export.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

print(header)
print(rows)
'''

# Read the CSV file into a DataFrame
df = pd.read_csv('share_export.csv', delimiter=';')

# Access the 'Price' column
price_column = df['Price']

# Print or use the columns as needed
print("\nPrice column:")
print(price_column)

# Convert the 'Price' column to numeric (in case it's not already)
price_column = pd.to_numeric(price_column, errors='coerce')

# Create a line plot
plt.plot(price_column)

# Set plot title and labels
plt.title('Price Column Visualization Hexagon')
plt.xlabel('Index')
plt.ylabel('Price')

# Show the plot
plt.show()