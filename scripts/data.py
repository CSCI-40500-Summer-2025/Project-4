# File: data.py
# Author(s): Ragib Asif, Jason Ongjoco

"""
Imports the data from a csv file and formats it.
"""

import csv

CSV_FILE: str = "data.csv"


def import_data() -> list[object]:

    data: list[object] = []
    with open(file=CSV_FILE, newline="", encoding="utf_8") as csvfile:
        dummyreader = csv.reader(csvfile)

        for row in dummyreader:
            data.append(row)

    fmt_data: list[object] = format_data(data)
    return fmt_data


# cache labels for report to use
bool_labels: list[str] = list()


def format_data(data: list[object]) -> list[object]:
    new_data: list[object] = []
    bool_headers = data[0][2::]
    bool_names: list[str] = list()

    for _, value in enumerate(bool_headers):
        bool_names.append(str(value))

    global bool_labels

    bool_labels = bool_names
    for items in data[1::]:
        new_items: list[object] = []
        bool_items: list[object] = []
        # turning yes/no, true/false answers to integers
        for item in items:
            if item == "Yes" or item == "True":
                bool_items.append(1)
            elif item == "No" or item == "False":
                bool_items.append(0)
            else:
                new_items.append(item)

        new_items.append(bool_items)
        new_data.append(new_items[1::])
    return new_data


def get_bool_labels() -> list[str]:
    return bool_labels
