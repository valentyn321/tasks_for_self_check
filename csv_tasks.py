import csv

with open('friends.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Alex'] + ['02.05.2001'] + ['Software Developer'])
    writer.writerow(['Dima'] + ['10.11.2000'] + ['UX/UI'])

with open('friends.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))