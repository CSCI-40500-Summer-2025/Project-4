import csv


def import_data():
    data = []
    with open("data/sample.csv", newline="") as csvfile:
        dummyreader = csv.reader(csvfile)
        for row in dummyreader:
            data.append(row)
    fmt_data = format_data(data)
    return fmt_data


def format_data(data: list):
    new_data = []
    for items in data[1::]:
        new_items = []
        bool_items = []
        for item in items:
            if item == "Yes" or item == "True":
                temp = 1
                bool_items.append(temp)
            elif item == "No" or item == "False":
                temp = 0
                bool_items.append(temp)
            else:
                temp = item
                new_items.append(temp)
        new_items.append(bool_items)
        new_data.append(new_items[1::])
    # print("old:")
    # print(data)
    # print("\n")
    # print("new:")
    # print(new_data)
    return new_data
