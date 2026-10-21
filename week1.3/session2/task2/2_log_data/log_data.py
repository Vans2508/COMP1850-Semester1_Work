# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.


# open and read the file

# find all failed login attempts (POST /login with the response 401)
# and print these out in a human-readable format:
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20


# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data
import csv
from pathlib import Path

log_file = Path(__file__).with_name("site.log")

try:
    with log_file.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if (
                row["Request"] == "POST /login"
                and row["Status_Code"] == "401"
            ):
                print(
                    f"IP address {row['IP_Address']} "
                    f"failed to login at {row['Time']} "
                    f"on {row['Date']}"
                )

except FileNotFoundError:
    print(f"Error: The file '{log_file}' was not found.")

except PermissionError:
    print(f"Error: Permission denied when opening '{log_file}'.")

except KeyError as error:
    print(f"Error: Missing expected column {error}.")