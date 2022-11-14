# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join(r'C:\Users\Peter\Source\Repos\python-challenge\PyBank', 'Resources', 'budget_data.csv')

# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # number of the rows excluding header would be the number of month
    total_month = 0

    # create a list of all the entries from second column of the file
    pl = []

    # create a list of all the month from first column of the file
    month = []

    # Read each row of data after the header and do the analysis
    for row in csvreader:
        total_month = total_month + 1

        # add all the entries from second column of the file
        pl.append(int(row[1]))

        # add all the entries from first column of the file
        month.append(row[0])

    # sum of the profit/loss list is the total
    total = sum(pl)

    # create a list for the change over months
    change = []
    for i in range(len(pl)):

        # difference between each month would be the movement
        change.append(pl[i] - pl[i-1])

    # the first entry is not the movement so invalid, we remove it form the list
    change.pop(0)

    # average  change would be total divided by total number of entries
    average = round(sum(change) / len(change),2)

    # greatest increase would be the maximum of the list
    greatest_increase = max(change)

    # greatest increase month would be the same row of the greatest increase
    greatest_month = month[change.index(greatest_increase) + 1]

    # greatest decrease would be the minimum of the list
    greatest_decrease = min(change)

    # greatest decrease month would be the same row of the greatest decrease
    least_month = month[change.index(greatest_decrease) + 1]

# print out the results in the terminal
print("Financial Analysis")
print("--------------------------------")
print(f"Total Month: {total_month}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {least_month} (${greatest_decrease})")

# export the analysis into test file
with open(os.path.join(r"C:\Users\Peter\Source\Repos\python-challenge\PyBank\analysis","pybank.txt"),"w") as f:
    f.write("Financial Analysis" "\n")
    f.write("--------------------------------""\n")
    f.write(f"Total Month: {total_month}""\n")
    f.write(f"Total: ${total}""\n")
    f.write(f"Average Change: ${average}""\n")
    f.write(f"Greatest Increase in Profits: {greatest_month} (${greatest_increase})""\n")
    f.write(f"Greatest Decrease in Profits: {least_month} (${greatest_decrease})""\n")
