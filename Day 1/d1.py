left_list = []
right_list = []
total_distance = 0
similarity = 0
with open('data.txt', 'r') as file:
    for line in file:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

# Loop through left list
for num in left_list:
    if num in right_list:
        # Calculate similarity score
        score = num * right_list.count(num)
        similarity += score
    
while left_list and right_list:
    # Get min of left and right list
    smallest_left = min(left_list)
    smallest_right = min(right_list)
    # Get the difference between the two (absolute)
    difference = abs(smallest_right - smallest_left)
    # Add the difference to the total distance
    total_distance += difference

    # Remove the smallest from the list
    left_list.remove(smallest_left)
    right_list.remove(smallest_right)

print("Part 1 - Total Distance: ",total_distance)
print("Part 2 - Similarity: ",similarity)
