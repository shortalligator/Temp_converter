from datetime import date

calculations = ['10.0°F to is -12°C', '20.0°F to is -7°C',
                '30.0°F to is -1°C', '40.0°F to is 4°C',
                '50.0°F to is 10°C', '60.0°F to is 16°C']

# get current dat for the heading of the filename
today = date.today()

# Get dat, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

filename = f"temperatures_{year}_{month}_{day}"
write_to = f"{filename}.txt"

with open(write_to, "w") as text_file:

    text_file.write("***** Temperature Calculations *****\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history (oldest to Newest)...\n")

    # write the item to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")
