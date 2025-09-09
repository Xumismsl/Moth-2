class Person:
    def __init__(self, name , birth_date,occupation,higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print('Общие сведения о человеке\n'
              f'name: {self.name}\n'
              f'birth date: {self.birth_date}\n'
              f'occupation: {self.occupation}\n'
              f'higher education: {"Есть" if self.higher_education else "Нету"}\n')


user_1 = Person(name='Диванович',birth_date= 2007,occupation='Преподователь',higher_education=True)
user_1.introduce()
user_2 = Person(name='Гилемович',birth_date= 2007, occupation='Директор',higher_education=True)
user_2.introduce()
user_3 = Person(name='Выключатель',birth_date= 2007,occupation='Студент',higher_education=False)
user_3.introduce()
