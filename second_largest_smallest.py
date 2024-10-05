def extract_numeric_from_iterable(item):
    
    numeric_values = []
    
    if isinstance(item, tuple):
        # Extract numbers from tuple
        numeric_values.extend([i for i in item if isinstance(i, (int, float))])
    
    elif isinstance(item, dict):
        # Extract numbers from dictionary keys and values
        for k, v in item.items():
            if isinstance(k, (int, float)):
                numeric_values.append(k)
            if isinstance(v, (int, float)):
                numeric_values.append(v)
    
    return numeric_values

def find_second_smallest_and_largest(lst):
    
    numeric_values = []
    
    # Loop through the list to extract numeric values
    for item in lst:
        if isinstance(item, (int, float)):
            
            numeric_values.append(item)
        elif isinstance(item, (tuple, dict)):
            # Extract numeric values from tuple or dictionary
            numeric_values.extend(extract_numeric_from_iterable(item))
    

    if len(numeric_values) < 2:
        return "Not enough numeric values"
    
   
    sorted_values = sorted(numeric_values)
    
    # Get the second smallest and second largest
    second_smallest = sorted_values[1]  
    second_largest = sorted_values[-2]  
    
    return second_smallest, second_largest


mixed_list = [3, 'hello', (5, 10), 8, {'a': 1, 'b': 12, 2: 14}, 15, 2, 9]

result = find_second_smallest_and_largest(mixed_list)
print("Second Smallest:", result[0])
print("Second Largest:", result[1])

