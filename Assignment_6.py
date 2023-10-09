# Assignment 1 

# 1. Create a JSON file (employee.json) containing employee information of minimum 5 employees. Each employee information consists of Name, DOB, Height, City, State. Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. 
# Finally print the list of the Employee objects.


import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def read_employee_data(filename):
    employee_list = []

    with open(filename, 'r') as file:
        data = json.load(file)
        for employee_data in data['employees']:
            name = employee_data['Name']
            dob = employee_data['DOB']
            height = employee_data['Height']
            city = employee_data['City']
            state = employee_data['State']

            employee = Employee(name, dob, height, city, state)
            employee_list.append(employee)

    return employee_list

if __name__ == "__main__":
    filename = 'employee.json'
    employees = read_employee_data(filename)

    for employee in employees:
        print(f"Name: {employee.name}")
        print(f"DOB: {employee.dob}")
        print(f"Height: {employee.height}")
        print(f"City: {employee.city}")
        print(f"State: {employee.state}")
        print()


# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.


import json

states_and_capitals = {
    "Rajasthan": "Jaipur",
    "Andhra Pradesh": "Amaravati",
    "Tamil Nadu": "Chennai",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    
}

with open("indian_states_and_capitals.json", "w") as json_file:
    json.dump(states_and_capitals, json_file, indent=4)

print("JSON file created successfully!")


# Assignment 2
# 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.


class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"\nName: {self.name} \nAge: {self.age}")

    def get_info(self):
        print(f"Coat color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, height_cm):
        super().__init__(name, age, coat_color)
        self.height_cm = height_cm

    def bark(self):
        print("Bark: Howl.")

    def height(self):
        print("Height: ", (self.height_cm))


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def bark(self):
        print("Bark: Growl.")

    def weight_kg(self):
        print(f"Weight: {self.weight} kg")


dog1 = JackRussellTerrier("Tommy - Jack Russell Terrier", 3, "White and Brown", "25 cm")
dog2 = Bulldog("Bruno - Bulldog", 5, "Brown", 10)

dog1.description()
dog1.get_info()
dog1.bark()
dog1.height()

dog2.description()
dog2.get_info()
dog2.bark()
dog2.weight_kg()
