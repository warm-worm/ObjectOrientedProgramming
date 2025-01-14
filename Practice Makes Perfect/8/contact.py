class Contact:
    def __init__(self, name, telephone, email):
        self.name = name
        self.email = email
        self.telephone = telephone
    def __str__(self):
        return f"{self.name}    {self.email}    {self.telephone}"
    
