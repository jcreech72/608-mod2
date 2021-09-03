#Central_With_statistics Module 2 Project
import statistics
from typing import Counter
total = 0
value_counter = 0
values = [47, 95, 88, 73, 88, 84]
for value in values:
    total += value  #add current value to running total
    value_counter += 1  #indicate one more value processed
print('The values are defined as', sorted(values))
print(f'The count of values is {value_counter}')
print('The Mean is', statistics.mean(values))
print('The Median is', statistics.median(values))
print('The Mode is', statistics.mode(values))
print('The sum of values is ', sum(values))