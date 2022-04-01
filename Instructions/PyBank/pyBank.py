#pyBank homework

# Import the necessary dependies for os.path.join()
import os
import csv

# Read in a .csv file
csv_path = os.path.join("Resources", "budget_data.csv")

#improved opening
with open(csv_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
  
    #initialize variables
    month_list = []
    profit_list = []
    profit_change_list = []

    for line in csvreader:
        month_list.append(line[0])
        profit_list.append(int(line[1]))

    #number of months
    months = len(month_list)
   
    #net total amount
    net_total_amount = sum(profit_list)

    #creates a list of the changes each month
    for i in range(len(profit_list)-1):
        profit_change_list.append(profit_list[i+1]-profit_list[i])
    
    #average profit change
    average_profit_change = round(sum(profit_change_list)/(len(profit_list)-1),2)
    
    #greatest increase
    greatest_increase_amount = max(profit_change_list)
    index_increase_date = profit_change_list.index(greatest_increase_amount)
    greatest_increase_date = month_list[index_increase_date+1]

    #greatest decrease
    greatest_decrease_amount = min(profit_change_list)
    index_decrease_date = profit_change_list.index(greatest_decrease_amount)
    greatest_decrease_date = month_list[index_decrease_date+1]

    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period 

    print(f"Financial Analysis \n---------------------")
    print(f"Total months: {months}") 
    print(f"Total: ${net_total_amount}")
    print(f"Average change: ${average_profit_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

    #export a text file with the results.
    output = (
            f"Financial Analysis \n"
            f"---------------------\n"
            f"Total months: {months}\n"
            f"Total: ${net_total_amount}\n"
            f"Average change: ${average_profit_change}\n"
            f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n"
            f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount}\n")
    with open('PyBank.txt','w') as f:
        f.write(output)