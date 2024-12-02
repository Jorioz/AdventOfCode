passing = 0
true_pass = 0

def check_increasing_or_decreasing(lst):
    return (all(0 < y - x <= 3 for x, y in zip(lst, lst[1:])) or
            all(0 < x - y <= 3 for x, y in zip(lst, lst[1:])))

def problem_dampener(lst):
    global passing, true_pass
    any_passing = False
    # Go through each element in the list and pop it out, creating a new temp list
    for i in range(len(lst)):
        temp = lst.copy()
        temp.pop(i)
        # After popping index, try to check if the list is increasing or decreasing
        if check_increasing_or_decreasing(temp):
            # If list passes after removing an index, it has passed the dampener
            any_passing = True
            break
    if any_passing:
        true_pass += 1
    # If we've gone through each element and none of them result in a passing list, then its unsafe & we dont add to count

with open('data.txt', 'r') as file:

    for line in file:
        report = [int(x) for x in line.split(" ")]
        if check_increasing_or_decreasing(report):
            passing += 1
        else:
            problem_dampener(report)



print("Part 1 - Passing: ",passing)
print("Part 2 - Passing w/ Dampener: ",passing + true_pass)
        
