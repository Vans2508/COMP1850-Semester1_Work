# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables) #prints the string common in both the sets
print(both)

# Why does the following code diplay five items?

food = fruit.union(vegetables) #prints all the items in both the sets without duplicating
print(food)

# Add an item to fruit
fruit.add("grapes")
print(fruit)
# Remove an item from vegetables
vegetables.remove("leek")
print(vegetables)
# Find and display symmetric difference of the two sets
print(fruit.symmetric_difference(vegetables))
