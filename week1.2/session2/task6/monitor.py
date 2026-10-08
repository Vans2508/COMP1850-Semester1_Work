# Week 1.2, Session 2: Task 6

machine_temp = int(input("Enter the temp of the machine in Celsius"))
machine_pressure = int(input("Enter the PSI Pessure of the machine"))
machine_status = int(input("Enter the operational status of the machine 1-operating or 0-stopped"))

if machine_status == 1:
    if machine_temp > 80:
        print(f"The temperature is too high reommend shutting the machine")
    elif machine_temp >= 50 and temp < 80:
        print(f"The temperature is within safe limits")
    elif machine_temp < 50:
        print(f"The machine temperature is low. No action needed")
    else:
        print(f"Not a valid temperature")
    if machine_pressure > 100:
        print(f"High temperature spotted. Need maintenance")
    elif machine_pressure >= 70 and machine_pressure < 100:
        print(f"Stable temperature")
    elif machine_pressure < 70:
        print(f"The pressure is low. The system is operating normally")