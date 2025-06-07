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


class Person:

    DEFAULT_WEIGHT: int = 5

    def __init__(self, name, email, weight=DEFAULT_WEIGHT) -> None:
        self.name = name
        self.email = email
        self.weight = weight
        # TODO: more fields (example: address, phone #, age, affiliation, etc.)

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def get_weight(self) -> int:
        return self.weight

    def set_name(self, name: str) -> None:
        self.name = name

    def set_email(self, email: str) -> None:
        self.email = email

    def set_weight(self, weight: int) -> None:
        # prototype: 0 - 10 (integers)
        self.weight = weight
        # future: negative numbers, floating point numbers

    def show_fields(self) -> None:
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Weight", self.weight)
