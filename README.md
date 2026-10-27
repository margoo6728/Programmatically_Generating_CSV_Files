# Programmatically_Generating_CSV_Files
ECPI 202610E OL SDC205L AO Python for Data Analytics Lab

## 4.3 Project: Programmatically Generating CSV Files

# Criteria
- Create a function called insertData that takes in two arguments.
  - The first argument is a path to a csv file; the second argument is a comma-separated string to be inserted into the csv file.
  - The function should open a file with sufficient permissions to append to the csv file or create and append if the file does not already exist.
  - This function must use a try-except statement to catch errors while writing.
  - Within the try-except statement, write the comma-separated data.
- Create a function called viewData that takes in one argument as the path of the file.
  -  The function should display the contents of the csv file and the path of the file being read.
  - Use the minimal permissions needed to read the file.
  - The function should contain a try-except statement to handle errors while reading the file.
- Modify the getInput function.
  - Add a try-except statement that takes the input from previous weeks and stores it into a csv file called ZooData.csv using the insertData function. 
  - On a successful write to the csv file, display "The following data was saved at <current date/time>: <data>." This should display what was saved to the csv file. Do this for each entry.
- Modify the flow control for the menu to call the viewData function if a user enters "2" from the main menu.
- Add a comment stating what the function does above each function that now exists in your project.
