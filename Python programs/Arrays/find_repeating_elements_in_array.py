def find_repeating_elements(arr):
    element_count = {element: arr.count(element) for element in arr}
    repeating_elements = [element for element, count in element_count.items() if element_count[element] > 1]
    return repeating_elements

# Example
arr = [4, 2, 3, 4, 2, 1, 3, 6]
result = find_repeating_elements(arr)
for i in result:
    print(i)
