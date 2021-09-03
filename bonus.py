#Central_With_statistics Module 2 Project
import statistics
total = 0
values = 0
from typing import Counter
values = range(101)
for counter in range(101):
    print(counter, end=' ')
    total = total + counter
  
print(f'The sum of numbers = {total}')
print(f'The counter is {counter}')
#print('The values are defined as', sorted(values))
print('The Mean is', statistics.mean(values))
print('The Median is', statistics.median(values))
print('The Mode is', statistics.mode(values))
#print('The sum of values is ', sum(values))