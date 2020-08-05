import os
import csv
csv_path = os.path.join('Resources','budget_data.csv')

#open file
with open(csv_path) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    csvlist = list(csvreader)
    csvreader = iter(csvlist)
    total = 0
    greatest_increase = [None,0]
    greatest_decrease = [None,0]


    for row in csvreader:
        row = list(row) # paranoid
        row[1] = int(row[1])
        total += row[1]
        print(greatest_decrease) # debugging
        if row[1] > greatest_increase[1]:
            greatest_increase = row
        if row[1] < greatest_decrease[1]:
            greatest_decrease = row
        
        
        print(row)

        

    print(f'There are {len(csvlist)} months in the dataset\nTotal net amount is ${total}\nThe average of changes is {int(total/len(csvlist))}')
    if greatest_decrease[0] is not None:
        print(f'The date {greatest_decrease[0]} was the greatest decrease, with the amount {greatest_decrease[1]}')
    if greatest_increase[0] is not None:
        print(f'The date {greatest_increase[0]} was the greatest increase, with the amount {greatest_increase[1]}')