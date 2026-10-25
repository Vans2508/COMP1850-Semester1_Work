# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence

sequence =[]
for next_num in range(L):
    if next_num == 0:
        sequence.append(0)
    else:
        candidate = sequence[-1] - next_num
        if  candidate > 0 and candidate not in sequence:
            sequence.append(candidate)
        else:
            sequence.append(sequence[-1] + next_num)
# You should store the sequence in an appropriate data structure named 'sequence'


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence