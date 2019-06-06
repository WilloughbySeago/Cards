"""
This is a program to analyse the results from Red_or_black
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom_test

result_array = []

with open('results.csv', mode='r') as results:
    results_reader = csv.reader(results)
    next(results_reader)  # Skip the header row
    for row in results_reader:
        correct = int(row[0])
        result_array.append(correct)

result_array = np.array(result_array)  # create array of number of times it guessed correctly out of a million guesses

average = int(round(np.mean(result_array)))
std_dev = np.std(result_array)

print(f'Mean = {average}')
print(f'Standard deviation = {std_dev}')

# statistical significance test
p = 0.05  # set significance level
prob = binom_test(average, 1000000, 0.5, 'greater')  # calculate prob given null hypothesis
if p < prob:
    print(f'{prob * 100}% is the probability that this would occur with the null hypothesis '
          + f'so we accept the null hypothesis')
else:
    print(f'{prob * 100}% is the probability that this would occur with the null hypothesis '
          + f'so we reject the null hypothesis')

# calculate bins
min_result = np.amin(result_array)  # min/max_result for calculating edges of histogram
max_result = np.amax(result_array)
range_result = max_result - min_result
print(min_result, max_result, range_result)
resolution = 100  # how far between bins
padding = 20  # how much empty space either side before rounding
min_bin = int(np.ceil(min_result / resolution) * resolution) - padding
max_bin = int(np.ceil(max_result / resolution) * resolution) + padding
bins = [i for i in range(min_bin, max_bin, resolution)]  # create list of bin edges

# plot histogram
plt.hist(result_array, bins=bins)
plt.title(f'A histogram of the results of red vs. black with the strategy of picking the opposite of the first card'
          + f'class width = {resolution}')
plt.xlabel('Correct guesses out of 10^6')
plt.ylabel('Frequency')
plt.show()
