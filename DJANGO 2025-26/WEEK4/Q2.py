from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
try:
    e = Employee()
except TypeError as error:
    print("Error:", error)

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return "Part-time salary calculated."

pte = PartTimeEmployee()
print(pte.calculate_salary())
