import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'x': [x for x in range(100)],
    'y': [y for y in range(100,0,-1)]
}
data1 = {
    'x': [3,6,3,7,3.6,27,45,79,356],
    'y': [78,68.67,96,.9,6.896,45,564,7,745]
}
#  Manual reverse
# for key in data:
#     v = []
#     for value in data[key]:
#         v.insert(0, value)
#     data2[key] = v

# consice reverse
data2 = {key: data[key][::-1] for key in data}

# Create a line plot
sns.lineplot(x='x', y='y', data=data1)
sns.lineplot(x='x', y='y', data=data)
plt.title('Sample Line Plot')
plt.show()

