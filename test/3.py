"""
3.py is used to test plotting bar graph
"""
import matplotlib.pyplot as plt
import numpy as np


label = ["Jan-2016", "Feb-2016", "March-2016"]
sales = [100,120,88]


index = np.arange(len(label))
plt.bar(index, sales)
plt.xlabel('Genre', fontsize=5)
plt.ylabel('No of Movies', fontsize=5)
plt.xticks(index, label, fontsize=5, rotation=30)
plt.title('Market Share for Each Genre 1995-2017')
plt.show()
