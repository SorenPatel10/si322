# Thought Process:
    # open file
    # create line
    # read line by line to initialize line
    # check if decimal point. if so float, if not int
    # close file
    # sort list lowest to highest
    # print each element on a newline

file = open("numbers.txt", "r")

numbers = []
for line in file:
    numbers.append(float(line.strip()) if "." in line else int(line.strip()))        

file.close()

numbers.sort()
for num in numbers:
    print(num)