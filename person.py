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
            sum = sum(int(id[i]) * weight[i] for i in range(10))
            rest = sum % 10
            if rest == 0:
                control = 0
            else:
                control = 10 - rest
            return True
        else:
            raise ValueError("Invalid pesel")
    
    def validate_date(self):
        year = self.birth.datetime.date

        if year >= 1900:
            print('01')
        elif year >= 2000:
            print('21')
        elif year >= 2100:
            print('41')
        elif year >= 2200:
            print('61')
