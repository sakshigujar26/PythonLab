def count_substring(main_string, sub_string, overlap_allowed=True):
    if overlap_allowed:
        count = sum(1 for i in range(len(main_string)) if main_string.startswith(sub_string, i))
        print("Overlapping allowed")
    else:
        count = main_string.count(sub_string)
        print("Overlapping not allowed")

    return count

#


# Call the function and print the result
result = count_substring('sggggsss', 'ggs', True)
print("Count:", result)

