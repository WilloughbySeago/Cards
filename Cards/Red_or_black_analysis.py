"""
This is a program to analyse the results from Red_or_black
"""
import csv
import numpy as np
import matplotlib.pyplot as plt

result_array = []
with open('results.csv', mode='r') as results:
    results_reader = csv.reader(results)
    next(results_reader)
    for row in results_reader:
        result_array.append(row[0])

result_array = np.array(result_array, dtype=int)
# print(result_array)
average = int(round(np.mean(result_array)))
print(f'Mean = {average}')
std_dev = np.std(result_array)
print(f'Standard deviation = {std_dev}')

min_result = np.amin(result_array)
max_result = np.amax(result_array)
range_result = max_result - min_result
print(min_result, max_result, range_result)
resolution = 100
padding = 20
min_bin = int(np.ceil(min_result/resolution)*resolution) - padding
max_bin = int(np.ceil(max_result/resolution)*resolution) + padding
print(min_bin, max_bin)
bins = [i for i in range(min_bin, max_bin, resolution)]
print(bins)
plt.hist(result_array, bins=bins)
plt.title(f'A histogram of the results of red vs. black with the strategy of picking the opposite of the first card'
          + f'class width = {resolution}')
plt.xlabel('Correct guesses out of 10^6')
plt.ylabel('Frequency')
plt.show()
