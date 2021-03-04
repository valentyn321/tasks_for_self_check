import csv


fieldnames = ["name", "date_of_birth", "occupation"]
friends = [
    {
        "name": "Alex",
        "date_of_birth": "02.05.2001",
        "occupation": "Software Developer",
    },
    {"name": "Dima", "date_of_birth": "10.11.2000", "occupation": "UX/UI Developer"},
]


def writer_by_one_operation(lst):
    with open("friends.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(friends)


def writer_line_by_line(lst):
    with open("friends.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for friend in friends:
            writer.writerow(friend)


def read_and_print():
    with open("friends.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row["name"], row["date_of_birth"], row["occupation"])


read_and_print()