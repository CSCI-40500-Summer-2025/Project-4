#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: person.py
# Author: Ragib Asif
# Email: ragib.asif30@myhunter.cuny.edu
# GitHub: https://github.com/ragibasif
# LinkedIn: https://www.linkedin.com/in/ragibasif/
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Ragib Asif
# Version 1.0.0
#
# Person class module.
#

from data import get_data
from person import Person


def test_person_class():
    data = get_data()
    data = data[1::]
    people = []
    for item in data:
        print(item)
        person = Person(item[0], item[1])
        people.append(person)

    mod_weights = input(
        "Would you like to change any weights? Type y/Y to change weights: "
    )

    if mod_weights == "y" or mod_weights == "Y":
        new_people = []
        for person in people:
            person.show_fields()
            change_weight = input(
                f"Would you like to change {person.get_name()}'s weight?."
                " If yes, type new weight. If no, leave blank: "
            )
            if change_weight.isdigit():
                change_weight = int(change_weight)
                if change_weight >= 0 and change_weight <= 10:
                    person.set_weight(change_weight)
                    print(f"Updated {person.get_name()}:")
                    person.show_fields()
            print("\n")
            new_people.append(person)
        people = new_people
    for person in people:
        person.show_fields()


def main():
    test_person_class()


if __name__ == "__main__":
    main()
