def slice(sequence, start=None, stop=None, step=1):
    if step == 0:
        return "Step cannot be zero"
    
    length = len(sequence)
    
    # Set default values for start and stop
    start = 0 if start is None else start
    stop = length if stop is None else stop
    
    # Adjust negative indices
    if start < 0:
        start += length
    if stop < 0:
        stop += length
    
    # Initialize result list
    result = []
    
    # Handle positive step
    if step > 0:
        i = start
        while i < stop and i < length:
            result.append(sequence[i])
            i += step
    # Handle negative step
    else:
        i = start
        while i > stop and i >= 0:
            result.append(sequence[i])
            i += step
    
    
    return ''.join(result) if isinstance(sequence, str) else result


print(sliceOp("hello", 1, 4, 1))  # Output: 'ell'

