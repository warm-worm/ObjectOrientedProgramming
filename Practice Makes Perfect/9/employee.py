class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
    def __str__(self):
        first_letter = self.name[0]
        result = self.surname + first_letter + str(self.seniority)
        if self.age >= 18:
            return result.upper()
        else:
            return result.lower()
        
employee1 = C("Anna", "May", 17, 7) #child labor holy crap
employee2 = C("George", "Brown", 21, 4)

print(employee1)
print(employee2)