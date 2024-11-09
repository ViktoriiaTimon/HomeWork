import csv

with open("rmc.csv", newline="") as f1:
    reader1 = csv.reader(f1)
    data1 = [tuple(row) for row in reader1]

with open("r-m-c.csv", newline="") as f2:
    reader2 = csv.reader(f2)
    data2 = [tuple(row) for row in reader2]


set1 = set(data1)
set2 = set(data2)
set_3 = set1 | set2

print(list(set_3))
with open('compare_result.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(set_3)