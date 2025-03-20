import sys

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog
from person import Person
from persons import Persons


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.persons = Persons()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.save.clicked.connect(self.saving)
        self.ui.comboBox.addItems([f'{p.name} {p.surname}' for p in self.persons.persons])
        self.persons.load_from_file("dane.csv")
        self.show()

    def saving(self):
        name = self.ui.name.text()
        surname = self.ui.surname.text()
        birth = self.ui.dateEdit.date().toPyDate()
        pesel = self.ui.pesel.text()
        post1 = self.ui.post1.text()
        post2 = self.ui.post2.text()

        try:
            self.persons.persons.append(Person(name, surname, birth, post1, post2, pesel))
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems([f'{p.name} {p.surname}' for p in self.persons.persons])
        except ValueError as e:
            message = QMessageBox()
            message.setText(e.__str__())
            message.exec()

        #with open('./data.txt', 'w+') as file:
        #    file.write(f'{name}, {surname}, {birth}, {pesel}, {post1}, {post2} \n')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    app.exec()
    sys.exit(window.persons.save_to_file("dane.csv"))
