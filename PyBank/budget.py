import csv
import os

budget_1 = os.path.join("budget_data_1.csv")

revenue = []
date = []
revenue_change = []

with open(budget_1, 'r') as csvfile:
    csv_reader1 = csv.reader(csvfile, delimiter=",")
    next(csv_reader1, None)
    for row in csv_reader1:
        revenue.append(float(row[1]))
        date.append(row[0])
        total_months = len(date)
        total_revenue = sum(revenue)
        avg_changein_rev = round(total_revenue/total_months, 0)

    for i in range(1, len(revenue)):
        revenue_change.append(revenue[i] - revenue[i-1])
        greatest_increase = max(revenue_change)
        greatest_decrease = min(revenue_change)
        date_of_increase = str(date[revenue_change.index(max(revenue_change))])
        date_of_decrease = str(date[revenue_change.index(min(revenue_change))])

    print("Financial Analysis")
    print("----------------------------------------")
    print("Total Months: " + str(int(total_months)))
    print("Total Revenue: $" + str(int(total_revenue)))
    print("Average Revenue Change: $" + str(int(avg_changein_rev)))
    print("Greatest Increase in Revenue: " +  date_of_increase +  " ($" + str(int(greatest_increase)) +")")
    print("Greatest Decrease in Revenue: " +  date_of_decrease +  " ($" + str(int(greatest_decrease)) + ")")


Financial_Analysis = os.path.join("PyBank.csv")
with open(Financial_Analysis, 'w', newline="") as datafile:
    csvWriter = csv.writer(datafile)
    csvWriter.writerow(["Financial Analysis"])
    csvWriter.writerow(["----------------------------------------"])
    csvWriter.writerow(["Total Months: " + str(int(total_months))])
    csvWriter.writerow(["Total Revenue: $" + str(int(total_revenue))])
    csvWriter.writerow(["Average Revenue Change: $" + str(int(avg_changein_rev))])
    csvWriter.writerow(["Greatest Increase in Revenue: " +  date_of_increase +  " ($" + str(int(greatest_increase)) +")"])
    csvWriter.writerow(["Greatest Decrease in Revenue: " +  date_of_decrease +  " ($" + str(int(greatest_decrease)) + ")"])