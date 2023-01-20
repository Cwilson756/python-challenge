#import modules

import os
import csv 

#create file path to csv

budgetpath = os.path.join("PyBank","resources","budget_data.csv")
output = os.path.join("PyBank", "analysis", "budget_analysis.txt")

#declare variables

net_total = 0
greatest_value = 0
greatest_month = str("")
lowest_value = 0
lowest_month = str("")
new_line = "\n"
average = 0
months = 0

#open and read csv file

with open(budgetpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row = next(csv_file)

    #loop through rows in the CSV file

    for row in csv_reader:

        #count rows to determine months

        months = months + 1
         
        #add up values in profit loss column to get net total 

        net_total += int(row[1])

        #determine average by taking net total and dividing by months (each profit loss is acompanied by a month)

        average = int(net_total/months)

        #save the lowest and highest value changes and month of said change

        if int(row[1]) > greatest_value:
            greatest_value = int(row[1])
            greatest_month = row[0]

        if int(row[1]) < lowest_value:
            lowest_value = int(row[1])
            lowest_month = row[0]

#print out financial analysis    

print(f'Financial Analysis{new_line}---------------------------- {new_line}Total Months: {months}{new_line}Total: ${net_total} {new_line}Average Change: ${average} {new_line}Greatest Increase in Profits: {greatest_month} (${greatest_value}) {new_line}Greatest Decrease in Profits: {lowest_month} (${lowest_value})')

#export text file with results
with open(output, "w") as f:
    analysis = (f'Financial Analysis{new_line}---------------------------- {new_line}Total Months: {months}{new_line}Total: ${net_total} {new_line}Average Change: ${average} {new_line}Greatest Increase in Profits: {greatest_month} (${greatest_value}) {new_line}Greatest Decrease in Profits: {lowest_month} (${lowest_value})')
    f.write(analysis)
