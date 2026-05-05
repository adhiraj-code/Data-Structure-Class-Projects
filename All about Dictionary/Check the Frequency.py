original_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 1}

unique_value_dict = {}

seen_values = set()

for key, value in original_dict.items():

    if value not in seen_values:

        unique_value_dict[key] = value

        seen_values.add(value)

print(unique_value_dict)

# Output: {'a': 1, 'b': 2, 'd': 3}