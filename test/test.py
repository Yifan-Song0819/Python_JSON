"""
this files is used to test matplotlib
"""
import matplotlib.pyplot as plt


plot_list = [1,2,3,4]
mean = sum(plot_list) / len(plot_list)
# print(mean)
print(max(plot_list))
print(min(plot_list))
plt.plot(plot_list)
plt.ylabel('some numbers')
plt.xlabel(mean)
# plt.show()
