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
print(result_array)
print(type(result_array))
print(result_array.dtype)
average = int(round(np.mean(result_array)))
print(average)
std_dev = np.std(result_array)
print(std_dev)


