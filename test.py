class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"{self.name} - {self.age}")

user1 = User("Ankit", 24)
user1.display()
print(user1.name)
user2 = User("Rahul", 34)
user2.display()


item = ["abc", "def", "geh"]

for index, it in enumerate(item, start=1):
    print(f"{index}. {it}")