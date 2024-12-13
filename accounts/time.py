import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the current date and time without milliseconds
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Print the current date and time without milliseconds
print("Current Date and Time:", formatted_datetime)
