from PyQt6.QtGui.QRawFont import weight


class Address:
    def __init__(self, post1, post2):
        self.post1 = post1
        self.post2 = post2

class Person:
    def  __init__(self, name, surname, birth, id, post1, post2):
        self.name = name
        self.surname = surname
        self.birth = birth
        self.id = id
        self.address = Address(post1, post2)

    def validate_pesel(self):
        if self.id.isdigit() and len(self.id) == 11:
            weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
            sum = sum()
            rest = (sum % 10) - 10
            control_number = 0
            if rest == 10:
                control_number = 0
            else:
                s

        raise ValueError("Invalid pesel")