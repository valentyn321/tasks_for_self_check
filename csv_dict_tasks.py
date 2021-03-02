import csv

with open('friends.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'date_of_birth', 'occupation']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'Alex', 'date_of_birth':'02.05.2001', 'occupation':'Software Developer'})
    writer.writerow({'name': 'Dima', 'date_of_birth':'10.11.2000', 'occupation':'UX/UI'})

with open('friends.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['date_of_birth'], row['occupation'])