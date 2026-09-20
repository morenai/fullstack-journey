# List of courses for practicing list operations.
courses = ['History', 'Math', 'Physics', 'Compsci']

# Print the full list.
print(courses)

# Count how many elements the list contains.
print(len(courses))

# Access an item by its index; Python indexing starts at 0.
print(courses[3])

# A negative index gets the last item in the list.
print(courses[-1])

# Slice the list from index 0 up to, but not including, index 3.
print(courses[0:3])


# Object-oriented programming in Python.
# The Employee class represents an employee with a first name, last name, and salary.
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

# Create an example employee.
emp1 = Employee('miguel', 'garcia', 50000)
# emp2 = Employee()

# Display the emp1 object.
print(emp1)
# print(emp2)

# These lines show how we could change attributes after creating the object.
# emp1.first = 'John'
# emp1.last = 'Smith '
# emp1.email = 'john.smith@example.com'
# emp1.pay = 50000

# emp2.first = 'Jane'
# emp2.last = 'Doe'
# emp2.email = 'jane.doe@example.com'
# emp2.pay = 60000

# Print each employee attribute.
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.pay)
