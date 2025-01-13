# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.year = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.year = 1
    student2.name = "Olivia"
    student2.age = 21
    student2.year = 3
    student3.name = "Sarah"
    student3.age = 20
    student3.year = 2

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, year {student1.year}.')
    print(f'{student2.name}, {student2.age} years old, year {student2.year}.')
    print(f'{student3.name}, {student3.age} years old, year {student3.year}.')

if __name__ == "__main__":
    main()