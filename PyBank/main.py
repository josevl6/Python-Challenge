import os
import csv

pyBank = os.path.join("raw_data", "budget_data_1.csv")

total_months = 0
total_revenue = 0
previous_revenue = 0
total_difference = 0
change_in_revenue = 0
average_revenue_change = 0
max_rev_dif = 0
min_rev_dif = 0

with open(pyBank, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    next(csv_reader)
    
    print("Financial Analysis")
    print("---------------------")

    for rows in csv_reader:
        total_months += 1
        
        total_revenue += int(rows[1])
        # print(rows)
        current_revenue = int(rows[1])
        
        if total_months >= 2:
            difference = current_revenue - previous_revenue
            total_difference += difference
            change_in_revenue = [difference]

            for i in change_in_revenue:
                if i > max_rev_dif:
                    max_rev_dif = i
                    date_max = rows[0]
            for j in change_in_revenue:
                if j < min_rev_dif:
                    min_rev_dif = j
                    date_min = rows[0]

        previous_revenue = current_revenue          

    average_revenue_change = total_difference / (total_months - 1)
    average_revenue_change = int(float((round(average_revenue_change,0))))

    # Print all values
    print("Total months: " + str(total_months))
    print("Total revenue: $" + str(total_revenue))
    print("Average revenue change: $" + str(average_revenue_change))
    print("Greatest Increase in Revenue: " + str(date_max) + " ($" + str(max_rev_dif) + ")")
    print("Greatest Decrease in Revenue: " + str(date_min) + " ($" + str(min_rev_dif) + ")")



    

   

    



