# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)
import data

dataset = data.Dataset("data.txt")
print(f"Dataset size: {len(dataset)}")
print(f"Mean: {dataset.mean()}")
print(f"Median: {dataset.median()}")
for value in dataset:
    print(value)    
