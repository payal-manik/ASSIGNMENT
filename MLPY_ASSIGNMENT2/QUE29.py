# Create a function that flattens a nested list.

def flatten_list(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result += flatten_list(item)  
        else:
            result.append(item)  
    return result


nested = [1, [2, [3, 4], 5], 6]
print(flatten_list(nested))















# Step-by-step Explanation:
# 1. result = []
# This is an empty list where we will store the final flat values.

# 2. for item in lst:
# We go through each item in the input list lst.

# 3. if type(item) == list:
# We check: Is this item a list?

# ✅ Yes: It’s a nested list → we call the same function again (flatten_list(item)) to flatten that inner list.

# ❌ No: It’s a normal value → we add it to our result list.

# 4. result += flatten_list(item)
# This adds the flattened version of the inner list to our result.

# 5. result.append(item)
# This adds a normal item (like a number or string) to our result.

# 6. return result
# After the loop, we return the flat list.
