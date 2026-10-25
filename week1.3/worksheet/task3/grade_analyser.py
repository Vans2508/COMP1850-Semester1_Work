# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
filename = input("Enter a file_name ")
output_filename = filename + "_out.csv"
# open the file
with open(filename, 'r') as input_file, open(output_filename, "w") as output_file:
    next(input_file)
    for line in input_file:
        row = line.strip().split(",") 

        student_id = row[0] # stores the student_id of the student

        modules = [int(value) for value in row[1:] if value !=""] #stores the grades for one student
        average_grade = sum(modules) / len(modules) #finds the average grade of one student by dividing the sum of all the modules by the number of modules
        if average_grade >= 70 and average_grade <= 100:
            classification = "1"
        elif average_grade >= 60:
            classification = "2:1" 
        elif average_grade >= 50:
            classification = "2:2"
        elif average_grade >= 40:
            classification = "3"
        else:
            classification = "F"
        output_file.write(f"{student_id},{average_grade:.2f},{classification}\n")

# read in the data, and for each student calculate their average grade and classification



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder