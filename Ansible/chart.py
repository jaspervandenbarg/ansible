# https://matplotlib.org/stable/tutorials/pyplot.html

import numpy as np
import matplotlib.pyplot as pplt

# Number of Instances
instances = [1, 2, 4, 8]

# Req/Sec for each number of instances
# These values were retrieved from the benchmarking results
# Typed over by hand
request_per_second = [870, 1030, 880, 900]

# Create plot
pplt.figure(figsize=(10, 5))
pplt.title('Req/Sec for different number of instances')

# Define x-axis
x_axis = np.linspace(0, len(instances)-1, len(instances))
pplt.bar(x_axis, request_per_second, color='red')
pplt.xlabel('Instances')
pplt.xticks(x_axis, instances)

# Define y-axis
pplt.grid(axis='y')
pplt.ylabel('Req/Sec')
pplt.ylim(600, 1200)

# Set data
for i in range(len(instances)):
    pplt.text(x_axis[i], request_per_second[i] + 5, str(request_per_second[i]), ha='center')

# Show results
pplt.show()