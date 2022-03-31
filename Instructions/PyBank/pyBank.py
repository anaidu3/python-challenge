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

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    #for row in csvreader:
        #print(row)
    
    #initialize variables
    months = 0
    net_total_amount = 0
    profit_change_list = []
    previous_amount = 0

    for line in csvreader:
        months = months + 1
        net_total_amount = net_total_amount + int(line[1])
        previous_amount = net_total_amount
        profit_change_list.append([line[0],previous_amount-int(line+1[1])])
    
    print(profit_change_list)
    #average_profit_change = sum(profit_change_list)/months
    
    greatest_increase_amount = max(profit_change_list)
    index_increase_date = profit_change_list.index(greatest_increase_amount)
    greatest_increase_date = profit_change_list(index_increase_date)

    greatest_decrease_amount = min(profit_change_list)
    index_decrease_date = profit_change_list.index(greatest_increase_amount)
    greatest_decrease_date = profit_change_list(index_decrease_date)


    #The total number of months included in the dataset
    print(f"Financial Analysis \n---------------------")
    print(f"Total months: {months}") 
    print(f"Total: ${net_total_amount}")
    print(f'Average change:{average_profit_change}')


#change_from_previous.append([row[0], revenue - previous_revenue])
#maxChangeMonth = dateProfitLossesList[changeList.index(max(changeList))]

#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period