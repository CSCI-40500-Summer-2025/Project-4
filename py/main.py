from person import Person


def test_person_class():
    people = []
    person_1 = Person("John Doe", "john@example.com", 5)
    person_2 = Person("Alice Smith", "alice.smith@test.org", 12)
    person_3 = Person("Bob Johnson", "bjohnson@mail.net", 3)
    person_4 = Person("Emma Wilson", "emma.w@demo.com", 7)
    person_5 = Person("Michael Brown", "michael.b@sample.io", 0)
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
    test_person_class()


if __name__ == "__main__":
    main()
