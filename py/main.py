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

from person import Person


def venv_demo():
    print("Script is running.")
    print("Script is finished running.")


def test_person_class():
    people = []
    person_1 = Person("John Doe", "john@example.com")
    person_2 = Person("Alice Smith", "alice.smith@test.org")
    person_3 = Person("Bob Johnson", "bjohnson@mail.net")
    person_4 = Person("Emma Wilson", "emma.w@demo.com", 7)
    person_5 = Person("Michael Brown", "michael.b@sample.io")
    person_6 = Person("Sarah Davis", "sarahd@fake.org", 9)
    person_7 = Person("David Lee", "dlee@example.org", 0)
    person_8 = Person("Olivia Taylor", "otaylor@testmail.com", 6)
    person_9 = Person("James Miller", "james.m@demo.org", 4)
    person_10 = Person("Sophia Clark", "s.clark@example.net", 8)
    people.append(person_1)
    people.append(person_2)
    people.append(person_3)
    people.append(person_4)
    people.append(person_5)
    people.append(person_6)
    people.append(person_7)
    people.append(person_8)
    people.append(person_9)
    people.append(person_10)
    print(people)
    for person in people:
        person.show_fields()


def main():
    # test_person_class()
    venv_demo()


if __name__ == "__main__":
    main()
