#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: person.py
# Author: Ragib Asif, Jason Ongjoco
# Person class module.



class Person:

    DEFAULT_WEIGHT: int = 5
    DEFAULT_BOOLS: list = []

    def __init__(self, name, weight=DEFAULT_WEIGHT, bools=DEFAULT_BOOLS) -> None:
        self.name = name
        self.email = "example@email.com"
        self.weight = weight
        self.bools = bools
        # TODO: more fields (example: address, phone #, age, affiliation, etc.)

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def get_weight(self) -> int:
        return self.weight

    def get_bools(self) -> list:
        return self.bools

    def set_name(self, name: str) -> None:
        self.name = name

    def set_email(self, email: str) -> None:
        self.email = email

    def set_weight(self, weight: int) -> None:
        # prototype: 0 - 10 (integers)
        self.weight = weight
        # future: negative numbers, floating point numbers

    def set_bools(self, bools: list) -> None:
        self.bools = bools

    def trunc_data(self) -> None:
        print("Name: ", self.name, "   Weight: ", self.weight)

    def show_fields(self) -> None:
        print("Name: ", self.name, "   Weight: ", self.weight)
        #print("Email: ", self.email)
        #print("Weight", self.weight)
        #print("Bools", self.bools)
