import csv

csv_file = "finalfinal.csv"

rows = []

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Read the header row
    header.append("cost")  # Add a new column header

    for row in reader:
        if row[0] != "city":
            dam = int(float(row[6]) * 500)
            row.append(dam)
        rows.append(row)

with open('finalfinal.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)  # Write the modified header
    writer.writerows(rows)  # Write the modified rows
