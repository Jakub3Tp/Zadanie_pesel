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
        pesel_year = int(self.id[:2])
        pesel_month = int(self.id[2:4])
        pesel_day = int(self.id[4:6])

        # Określenie stulecia
        if 1 <= pesel_month <= 12:
            century = 1900
        elif 21 <= pesel_month <= 32:
            century = 2000
            pesel_month -= 20
        elif 41 <= pesel_month <= 52:
            century = 2100
            pesel_month -= 40
        elif 61 <= pesel_month <= 72:
            century = 2200
            pesel_month -= 60
        elif 81 <= pesel_month <= 92:
            century = 1800
            pesel_month -= 80
        else:
            return False  # Niepoprawny PESEL

        full_year = century + pesel_year
        birth_date = datetime.strptime(self.birth, "%Y-%m-%d")

        return birth_date.year == full_year and birth_date.month == pesel_month and birth_date.day == pesel_day
