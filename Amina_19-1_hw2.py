class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):

    def __init__(self, first_name, last_name, salary, company_bank, company_name):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


    def get_salary(self):
        print(f"компания: {self.company_name}\n"
              f"капитал: {self.company_bank}\n"
              f"зарплата сотрудника: {self.salary}")
        if self.company_bank < self.salary:
            print(f"\nу компании недостаточно средств! на {self.salary -  self.company_bank}")
        else:
            j = self.company_bank - self.salary
            print(f"\nв банке {self.company_name} осталось:  {j}")


    def person_info(self):
        print(f"\nинфо сотрудника: \n"
              f"first name: {self.first_name}\n"
              f"last name: {self.last_name}\n"
              f"salary: {self.salary}")


s = Person("Gkxhuhf", "Hdjlhk", 45678, 100000, '"SRKG"')
s.get_salary()
s.person_info()
