#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: person.py
# Author: Ragib Asif, Jason Ongjoco
#
# Person class module.
#

from data import import_data
from person import Person
from report import generate_report


def people_create() -> list[Person]:

    data: list[object] = import_data()
    people: list[Person] = []
    for item in data:
        person = Person(str(item[0]), bools=item[1])
        people.append(person)
        person.dump_memory()

    mod_weights = input(
        "Weights are 0-10, default is 5. \n"
        "A score of 9 or more is considered critical personnel.\n"
        "Would you like to change any weights? Type y/Y to change weights: "
    )

    if mod_weights == "y" or mod_weights == "Y":
        people: list[Person] = change_weights(people)
    for person in people:
        person.dump_memory()

    return people


def change_weights(people: list[Person]) -> list[Person]:

    new_people: list[Person] = []
    for person in people:
        person.dump_memory()
        change_weight = input(
            f"Change {person.get_name()}'s weight? Type new weight, or leave blank: "
        )
        if change_weight.isdigit():
            old_weight: int = person.get_weight()
            change_weight = int(change_weight)
            if change_weight >= 0 and change_weight <= 10:
                person.set_weight(change_weight)
                print(
                    f"Updated {person.get_name()} from {old_weight} to {person.get_weight()}")
        print("\n")
        new_people.append(person)
    people = new_people
    return people


def main() -> None:
    """Entry point of the program."""

    people: list[Person] = people_create()
    generate_report(people=people)


if __name__ == "__main__":
    main()
