import numpy as np
import matplotlib.pyplot as plt

#opening and writing data to list
f = open("random_data.txt","r")
temp = f.read()
data_str = temp.split('\n')
#reformating strig as float (not including empty final string)
data = []
for x in range(len(data_str)-1):
    data.append(float(data_str[x]))

n, bins, patches = plt.hist(data, 50, density=True, facecolor='b', alpha=0.75)

# plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Uniform random number')
plt.grid(True)

# show figure (program only ends once closed)
plt.show()