# Marleyna Goodrich
# 4.3 Project: Programmatically Generating CSV Files

from datetime import datetime

# Assign CSV file path
path = "C:\\PythonFiles\\ZooData.csv"

# Append data to the CSV file
def insertData(path, data):
    try:
        with open(path, 'a') as csvfile:
            csvfile.write(data + "\n")
        return True
    except OSError as error:
        print("Error saving data:", error)
        return False

# Opens and displays the data in the CSV file
def viewData(path):
    try:
        with open(path, 'r') as csvfile:
            print("The file", path)
            print(csvfile.read())
    except OSError as error:
        print("Error reading data:", error)

# Convert numerical values based on the selected data type
def convertedData(value):
    if conversionType == "1":
        return (value - 32) * 5 / 9
    elif conversionType == "2":
        return value / 2.205
    elif conversionType == "3":
        return value * 2.54

# Collect dates and numerical values based on the selected data type
def getInput():
    global conversionType

    # Display data type options for the user
    print("What type of data would you like to enter?")
    print("1 Temperature (Fahrenheit)")
    print("2 Weight (Pounds)")
    print("3 Rain Amount (Inches)")

    conversionType = input()

    while conversionType not in ("1", "2", "3"):
        print("Invalid selection. Please enter 1, 2, or 3.")
        conversionType = input()

    # Request the number of entries
    try:
        numberOfEntries = int(input("How many entries are you inputting?\n"))

        if numberOfEntries <= 0:
            print("Please enter a number greater than zero.")
            return

    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

     # Repeat data entry based on the number of entries selected
    for entry in range(numberOfEntries):
        entryDate = input("Enter a date:\n")

        try:
            # Request a numerical value based on selected data type
            if conversionType == "1":
                value = float(input("Enter the highest temp for the inputted date:\n"))
            elif conversionType == "2":
                value = float(input("Enter the weight in pounds for the inputted date:\n"))
            else:
                value = float(input("Enter the rain amount in inches for the inputted date:\n"))

            # Call convertedData with a float argument
            convertedValue = convertedData(value)

            # Organize data into a comma-separated string
            data = f"{entryDate},{value},{convertedValue}"

            # Save the data into the CSV file
            if insertData(path, data):
                print("The following data was saved at", datetime.now(), ":", data)

        except ValueError:
            print("Invalid numerical input. Entry was not saved.")

# Display Spreadsheet Automation Menu
print("margoo6728's Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1 Input Data")
print("2 View Current Data")
print("3 Generate Report")

number = input()

timestamp = datetime.now()
print(f"You selected {number} at {timestamp}\n")

# Call getInput when option 1 selected
if number == "1":
    getInput()

elif number == "2":
    viewData(path)

else:
    print("Error: The chosen functionality is not implemented yet")
