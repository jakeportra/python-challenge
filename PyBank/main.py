#Import modules
import pandas as pd

#Read CSV file, put in dataframe

bank_data = "../../../ClassRepo6/UofM-STP-DATA-PT-11-2019-U-C/03-Python/Homework/PyBank/Resources/budget_data.csv"
bank_df = pd.read_csv(bank_data)

#The total number of months included in the dataset

total_months = len(bank_df.index)

#The net total amount of "Profit/Losses" over the entire period

profit_loss = bank_df['Profit/Losses'].sum()

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

greatest_increase = bank_df['Profit/Losses'].max()

#The greatest decrease in losses (date and amount) over the entire period

greatest_loss = bank_df['Profit/Losses'].min()

#Print Analysis

print("Financial Analysis") 
print("----------------------------")
print(f"Total Months: {total_months}")
print("Total Profit (+) / Loss (-): $", "{:0,.2f}".format(float(profit_loss)))
print("Average Change: ")
print("Greatest Increase in Profits: ", "{:0,.2f}".format(float(greatest_increase)))
print("Greatest Decrease in Profits: ", "{:0,.2f}".format(float(greatest_loss)))

#Export text file

bank_df.to_csv("Output/bank_df.csv", index=False, header=True)

