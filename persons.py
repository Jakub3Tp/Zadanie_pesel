from datetime import date

from person import Person


class Persons:
    def __init__(self):
        self.persons = []

    def save_to_file(self, path):
        with open(path, 'w') as file:
            for person in self.persons:
                file.write(f"{person.name}, {person.surname}, {person.pesel}, {person.birth}, {person.address.post1}, {person.address.post2}\n")

    def load_from_file(self, path):
        with open(path, 'r') as file:
            data = file.read()

        if data != "":
            data = data.split("\n")
            for person in data:
                if person != "":
                    person_data = person.split(";")
                    name = person_data[0]
                    surname = person_data[1]
                    birth = date.fromisoformat(person_data[2])
                    pesel = person_data[3]
                    post1 = person_data[4]
                    post2 = person_data[5]

                    self.persons.append(Person(name, surname, birth, pesel, post1, post2))
