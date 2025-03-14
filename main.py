import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.save.clicked.connect(self.saving)
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
        except ValueError as e:
            message = QMessageBox()
            message.setText(e.__str__())
            message.exec()

        #class Persons:
        #def __init__(self):
        #self.persons = []

        #with open('./data.txt', 'w+') as file:
        #    file.write(f'{name}, {surname}, {birth}, {pesel}, {post1}, {post2} \n')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
