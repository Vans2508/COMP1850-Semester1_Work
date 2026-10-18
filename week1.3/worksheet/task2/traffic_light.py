"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0 #records how many times it has looped in the maxtime

step_current_state = 0 #records how many times the current state has been looped

maxtime = int(input())  # read an integer number of steps (>0)

state_order = list(states.keys()) #converting the order of the states as a list from the dictionary

current_state_index = 0 # this records which state we currently looping through

# Simulate the traffic light system up to time=maxtime in 1-second steps
while maxtime > 0 and systime <= maxtime :
    
    current_state = state_order[current_state_index]
    
# At the end of each step you should output the time and state using the statement on line 14
    print(f"Time {systime:03} State {current_state}")
    
    step_current_state += 1
    systime += 1
    
    if step_current_state == states.get(current_state):
        step_current_state = 0
        current_state_index = (current_state_index + 1) % len(state_order)
