# -*- coding: utf-8 -*-
"""Mainflow_task3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bnkComkO51-9m6IAvVDPsQs5PsCNl6TS
"""

pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Sample data for the DataFrame
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Sales': [250, 300, 400, 350, 450],
    'Expenses': [200, 220, 300, 280, 330]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Create the bar chart
plt.figure(figsize=(10, 5))
plt.bar(df['Month'], df['Sales'], color='blue', label='Sales')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Monthly Sales')
plt.legend()
plt.grid(True)
plt.show()

# Create the line chart
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Sales'], marker='o', color='blue', label='Sales')
plt.plot(df['Month'], df['Expenses'], marker='s', color='red', label='Expenses')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Monthly Sales and Expenses')
plt.legend()
plt.grid(True)
plt.show()