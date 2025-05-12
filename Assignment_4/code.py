def modify_line(line):
    return line.upper()

try:
    with open('sample.txt', 'r') as file:
        lines = file.readlines()

    modified_lines = [modify_line(line) for line in lines]

    with open('sample.txt', 'w') as file:
        file.writelines(modified_lines)

except FileNotFoundError:
    print("Error: 'sample.txt' not found.")
