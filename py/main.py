#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: person.py
# Author: Ragib Asif, Jason Ongjoco
#
# Person class module.
#

from data import import_data
from person import Person
from py.report import generate_report


def people_create() -> list:
    data: list = import_data()
    people = []
    for item in data:
        person = Person(item[0], bools=item[1])
        people.append(person)
        person.show_fields()

    mod_weights = input(
        "Would you like to change any weights? Type y/Y to change weights: "
    )

    if mod_weights == "y" or mod_weights == "Y":
        people: list = change_weights(people)
    for person in people:
        person.show_fields()
    return people


def change_weights(people: list) -> list:
    new_people = []
    for person in people:
        person.show_fields()
        change_weight = input(
            f"Would you like to change {person.get_name()}'s weight?."
            " If yes, type new weight. If no, leave blank: "
        )
        if change_weight.isdigit():
            old_weight = person.get_weight()
            change_weight = int(change_weight)
            if change_weight >= 0 and change_weight <= 10:
                person.set_weight(change_weight)
                print(f"Updated {person.get_name()} from {old_weight} to {person.get_weight()}")
        print("\n")
        new_people.append(person)
    people = new_people
    return people


def main():
    # import_data()
    people = people_create()
    generate_report(people)


if __name__ == "__main__":
    main()
