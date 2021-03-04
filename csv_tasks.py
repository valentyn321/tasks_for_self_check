import csv

friends_string = [
    ["Alex, 02.05.2001, Software Developer"],
    ["Dima, 10.11.2000, UX/UI"],
    ["Valentyn, 03.02.2001, Python Dev"],
]


def write_by_one_operation(lst):
    with open("friends.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quotechar="|", quoting=csv.QUOTE_MINIMAL)
        writer.writerows(lst)


def write_line_by_line(lst):
    with open("friends.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quotechar="|", quoting=csv.QUOTE_MINIMAL)
        for row in lst:
            writer.writerow(row)


def read_csv():
    with open("friends.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
        for row in reader:
            print(", ".join(row))
