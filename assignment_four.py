class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary
    
    def __str__(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nBase Salary: ${self.base_salary:.2f}"
    
    def calculate_salary(self):
        return self.base_salary


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, benefits):
        super().__init__(name, employee_id, base_salary)
        self.benefits = benefits
    
    def __str__(self):
        return f"Full-Time Employee ID: {self.employee_id}\nName: {self.name}\nBase Salary: ${self.base_salary:.2f}\nBenefits: ${self.benefits:.2f}"
    
    def calculate_salary(self):
        return self.base_salary + self.benefits


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        base_salary = hourly_rate * hours_worked
        super().__init__(name, employee_id, base_salary)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def __str__(self):
        return f"Part-Time Employee ID: {self.employee_id}\nName: {self.name}\nHourly Rate: ${self.hourly_rate:.2f}\nHours Worked: {self.hours_worked}\nBase Salary: ${self.base_salary:.2f}"
    
    def calculate_salary(self):
        return self.base_salary


class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def display_employees(self):
        for emp in self.employees:
            print(emp)
            print()
    
    def calculate_total_salary(self):
        total_salary = 0
        for emp in self.employees:
            total_salary += emp.calculate_salary()
        return total_salary


# Implementation
if __name__ == "__main__":
    # Creating employees
    emp1 = FullTimeEmployee("John Doe", 1, 50000, 10000)
    emp2 = PartTimeEmployee("Jane Smith", 2, 20, 80)

    # Creating company
    company = Company()
    
    # Adding employees to the company
    company.add_employee(emp1)
    company.add_employee(emp2)
    
    # Displaying all employees
    print("Employee Details:")
    company.display_employees()
    
    # Calculating total salary expense
    total_salary = company.calculate_total_salary()
    print(f"Total Salary Expense: ${total_salary:.2f}")
