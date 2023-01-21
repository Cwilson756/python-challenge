#import modules

import os
import csv 

#create file path to csv

budgetpath = os.path.join("PyBank","resources","budget_data.csv")
output = os.path.join("PyBank", "analysis", "budget_analysis.txt")

#declare variables

net_total = 0
greatest_month = str("")
lowest_month = str("")
new_line = "\n"
average_change = 0
months = 0
past_month = 0
current_month = 0
monthly_change = 0
n = 0
changes = {}

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

        #if it is the first month save the current month but perform no calculations

        if months == 1:
            current_month = int(row[1])

        #save current and past month, calculate monthly change, add it to a list
            
        else:
            past_month = current_month
            current_month = int(row[1])
            monthly_change = (current_month - past_month)
            changes.update({row[0]:monthly_change})

#calculate average change and find greatest and lowest change months

average_change = round((sum(changes.values()) / len(changes)), 2)

lowest_month = min(changes.items(), key=lambda x: x[1])
greatest_month = max(changes.items(), key=lambda x: x[1])

#print out financial analysis    

print(f'Financial Analysis{new_line}---------------------------- {new_line}Total Months: {months}{new_line}Total: ${net_total} {new_line}Average Change: ${average_change} {new_line}Greatest Increase in Profits: {greatest_month[0]} (${greatest_month[1]}) {new_line}Greatest Decrease in Profits: {lowest_month[0]} (${lowest_month[1]})')

#export text file with results
with open(output, "w") as f:
    analysis = (f'Financial Analysis{new_line}---------------------------- {new_line}Total Months: {months}{new_line}Total: ${net_total} {new_line}Average Change: ${average_change} {new_line}Greatest Increase in Profits: {greatest_month[0]} (${greatest_month[1]}) {new_line}Greatest Decrease in Profits: {lowest_month[0]} (${lowest_month[1]})')
    f.write(analysis)
