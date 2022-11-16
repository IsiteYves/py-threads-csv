# importing csv module
import csv
import sys

# csv file name
filename = "eg.csv"

# initializing the titles and rows list
fields = []
rows = []

with open("eg.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    temp = header[0]
    header[0] = header[1]
    header[1] = temp
    for row in csvreader:
        temp2 = row[0]
        row[0] = row[1]
        row[1] = temp2
        rows.append(row)

with open("eg.csv", 'w+') as csvfile:
    csvwriter = csv.writer(csvfile, lineterminator='\n')
    csvwriter.writerow(header)
    csvwriter.writerows(rows)

temp3 = sys.stdout
for i in range(len(header)):
    if (len(str(header[i]).split((','))) > 1):
        temp3.write(f'"{header[i]}"')
    else:
        temp3.write(header[i])

    if i != len(header)-1:
        temp3.write(',')
temp3.write('\n')

for newrow in rows:
    for j in range(len(newrow)):
        if (len(str(newrow[j]).split((','))) > 1):
            temp3.write(f'"{newrow[j]}"')
        else:
            temp3.write(newrow[j])

        if j != len(newrow)-1:
            temp3.write(',')
    temp3.write('\n')
