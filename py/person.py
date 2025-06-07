class Person:
    def __init__(self, name, email, weight):
        self.name = name
        self.email = email
        self.weight = weight
        # TODO: more fields (example: address, phone #, age, affiliation, etc.)

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_weight(self):
        return self.weight

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_weight(self, weight):
        # prototype: 0 - 10 (integers)
        self.weight = weight
        # future: negative numbers, floating point numbers

    def show_fields(self):
        print("Name: ", self.name)
        print("Email: ", self.email)
        print("Weight", self.weight)
