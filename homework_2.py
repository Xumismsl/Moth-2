class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f'Добрый денек мой дружок меня зовут: {self.name}\n'
              f'Родился я: {self.birth_date}\n'
              f'По профессии : {self.occupation}\n'
              f'Высшее образование : {"Есть" if self.higher_education else "Нету"}\n')


class Classmate(Person):
    def introduce(self):
        print(f'Привет я: {self.name}\n'
              f'Также если ты не знал я твой одноклассник и мне очень приятно с тобой познакомиться\n'
              f'Я родился: {self.birth_date}\n '
              f'По профессии: {self.occupation}\n'
              f'Высшее образование : {'Есть' if self.higher_education else 'Нет'}\n')


class Friend(Person):
    def introduce(self):
        print(f'Привет я: {self.name}\n'
              f'Также если ты не знал я твой лучший друг\n'
              f'Я родился: {self.birth_date}\n '
              f'По профессии: {self.occupation}\n'
              f'Высшее образование : {'Есть' if self.higher_education else 'Нет'}\n')


classmate_one = Classmate('Смирнов', '1988-03-17', 'Врач', True)

classmate_two = Classmate('Кузнецова', '1992-09-05', 'Программист', True)

classmate_one.introduce()
classmate_two.introduce()

friends = Friend('Лебедев', '2001-12-11', 'Фотограф', False)
friends.introduce()
