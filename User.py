class Users:
    def __init__(self, name, age, email, phone):
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone

    def __str__(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def contact_info(self):
        return f"{self.name}'s contact information is: phone number: {self.phone}, email: {self.email}."


robert= Users("Robert", 31, "robert@random.com", "555-555-1111")
alisha=Users("Alisha", 31, "alisha@email.com", "557-775-1234")
mike=Users("Mike", 55, "mike@rocks.com", "554-445-1234")

print(robert)
print(alisha.contact_info())