#central-native Module 2 Project
"""Values to calculate central tendancy """

#Initialization phase
total = 0  # sum of values
value_counter = 0  
values = [47, 95, 88, 73, 88, 84]  # list of values

#processing phase
for value in values:
    total += value  #add current value to running total
    value_counter += 1  #indicate one more value processed

#termination phase
average = total / value_counter
print(f'The values mean is {average:.2f}')
print(f'The sum of the values is {total}')
print(f'The count of values is {value_counter}')
print(f'The median of the values is {value}')
#to get mode had to do this
values = [47, 95, 88, 73, 88, 84]
occurrences = []
for item in values :
    count = 0
    for x in values :
        if x == item :
            count += 1
    occurrences.append(count)

duplicates = set()
index = 0
while index < len(values) :
    if occurrences[index] != 1 :
        duplicates.add(values[index])
    index += 1

print(f'The Mode value is {duplicates}')