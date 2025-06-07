import csv


def get_data():
    data = []
    with open("data/dummy_mini.csv", newline="") as csvfile:
        dummyreader = csv.reader(csvfile)
        for row in dummyreader:
            data.append(row)
    return data
