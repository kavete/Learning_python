from datetime import datetime


class Person:
    def __init__(self, name, email, dob, gender, favourite_teams):
        self.name = name
        self.email = email
        self.dob = dob
        self.gender = gender
        self.teams = favourite_teams

    def print_details(self):
        print(self.name)
        print(self.gender)
        print(".......TEAMS.......")
        for team in self.teams:
            print(team)
        print("........")

    def calc_age(self):
        today = datetime.now()
        dob = datetime.strptime(self.dob, "%d-%m-%Y")
        delta = today - dob
        print(delta.days // 365, "years old")


person1 = Person("Brian", "etevak@gmail.com", "18-12-2001", "Male", ["Manchester City", "Barcelona"])

person1.print_details()
person1.calc_age()
