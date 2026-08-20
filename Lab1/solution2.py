# Thought Process:
    # open file
    # create dictionary
    # loop through file by line, and then each word in that line
    # clean word by lowercase and strip
    # if already found, add 1 to value. if new, add word to dictionary and set value to 1
    # key is word, value is occurrence count
    # close file
    # sort dictionary into list of tuples by value in descending order
    # print the top 5 entries

file = open("words.txt", "r")

word_totals = {}

for line in file:
    words_in_line = line.lower().split()
    for word in words_in_line:
        target = word.strip()
        word_totals[target] = word_totals.get(target, 0) + 1

file.close()

sorted_totals = sorted(word_totals.items(), key=lambda item: item[1], reverse = True)

for key,val in sorted_totals[:5]:
    print(f"{key}: {val}")
