#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from data import get_bool_labels
from person import Person


def attendance(people: list[Person]) -> None:
    """Calculate and print attendance stats (x of y) for each date."""
    if not people:
        print("No data to process.")
        return

    # Determine the number of dates (length of bools list)
    num_dates = len(people[0].get_bool_values()) if people else 0

    for date_idx in range(num_dates):
        present_count = sum(
            1 for person in people if person.get_bool_values()[date_idx] == 1
        )
        total_people = len(people)
        print(f"Date {date_idx + 1}: {present_count} of {total_people} available.")


def avg_score(people: list[Person]) -> None:
    """Calculate and print average scores for non-zero attendance dates."""
    if not people:
        print("No data to process.")
        return

    num_dates = len(people[0].get_bool_values()) if people else 0

    for date_idx in range(num_dates):
        weighted_scores = []
        for person in people:
            if person.get_bool_values()[date_idx] == 1:  # Only count if present
                weighted_scores.append(person.get_weight())

        if weighted_scores:
            avg_score = sum(weighted_scores) / len(weighted_scores)
            print(f"Date {date_idx + 1}: Average Score: {avg_score:.1f}")
        else:
            print(f"Date {date_idx + 1}: No attendees.")


def generate_flags(people: list[Person], date_idx: int) -> str:
    """Generate flags for a specific date based on custom rules."""
    flags = []

    # Rule 1: Check if any high-weight person (>=8) is absent
    high_weight_absent = any(
        p.get_weight() >= 9 and p.get_bool_values()[date_idx] == 0 for p in people
    )
    if high_weight_absent:
        flags.append("⚠️ Missing Critical Personnel")

    # Add more rules here (e.g., low attendance, score variance, etc.)
    # flags.append("⚠️ New flag")

    return " | ".join(flags) if flags else ""


def generate_report(people: list[Person]) -> None:

    # get date labels from data cache
    # bool_labels = get_bool_labels()
    bool_labels = get_bool_labels()

    if not people:
        print("No data to process.")
        return

    num_dates = len(people[0].get_bool_values()) if people else 0

    print("\n--- Attendance Report ---")
    for date_idx in range(num_dates):
        # Attendance (x of y)
        present_count = sum(
            1 for person in people if person.get_bool_values()[date_idx] == 1
        )
        total_people = len(people)

        # avg score for this date/index, exclude 0's
        weighted_scores = [
            person.get_weight()
            for person in people
            if person.get_bool_values()[date_idx] == 1
        ]
        avg_score = (
            sum(weighted_scores) / len(weighted_scores) if weighted_scores else 0
        )

        # pull flags for current date index
        flags = generate_flags(people, date_idx)

        print(
            f"{bool_labels[date_idx]}: {present_count} of {total_people} available. | "
            f"Average Score: {avg_score:.1f} | "
            f"{flags}"
        )
