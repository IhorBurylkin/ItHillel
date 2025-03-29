from .Human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __str__(self):
        return f'{super().__str__()}, Record book: {self.record_book}'
    
    def __hash__(self):
        return hash(str(self))
