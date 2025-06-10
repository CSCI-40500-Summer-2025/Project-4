#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: person.py
# Author: Ragib Asif, Jason Ongjoco
# Person class module.


class Person:

    DEFAULT_WEIGHT: int = 5
    DEFAULT_BOOLS: list[tuple[str, bool]] = []
    DEFAULT_EMAIL: str = "example@email.com"

    def __init__(self, name: str, email: str = DEFAULT_EMAIL, weight: int = DEFAULT_WEIGHT, bools: list[tuple[str, bool]] = DEFAULT_BOOLS) -> None:
        self.name: str = name
        self.email: str = email
        self.weight: int = weight
        self.bools: list[tuple[str, bool]] = bools
        # TODO: more fields (example: address, phone #, age, affiliation, etc.)

    def get_name(self) -> str:
        return self.name

    def get_email(self) -> str:
        return self.email

    def get_weight(self) -> int:
        return self.weight

    def get_bool_values(self) -> list[bool]:
        temp_list: list[bool] = list()
        for _, value in self.bools:
            temp_list.append(bool(value))
        return temp_list

    def set_name(self, name: str) -> None:
        self.name = name

    def set_email(self, email: str) -> None:
        self.email = email

    def set_weight(self, weight: int) -> None:
        # prototype: 0 - 10 (integers)
        self.weight = weight
        # future: negative numbers, floating point numbers

    def set_bools(self, bools: list[tuple[str, bool]]) -> None:
        self.bools = bools

    def trunc_data(self) -> None:
        print("Name: ", self.name, "   Weight: ", self.weight)

    def dump_memory(self) -> None:
        """DEBUGGING: This function shows whats currently stored in all the variables of the class."""
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Weight: ", self.weight)
        print("Bools: ", self.bools)
