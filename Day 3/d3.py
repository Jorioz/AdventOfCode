import re

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
main_pattern = r"mul\((\d+),(\d+)\)"

toggle = True
buffer = ""
matches = []
sum = 0

with open('data.txt', 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            break

        buffer += char

        if re.search(do_pattern, buffer):
            toggle = True
            buffer = ""
        elif re.search(dont_pattern, buffer):
            toggle = False
            buffer = ""

        if toggle:
            found = re.findall(main_pattern, buffer)
            for match in found:
                num1, num2 = match
                sum += int(num1) * int(num2)
            buffer = re.sub(main_pattern, '', buffer)

print("Sum:", sum)