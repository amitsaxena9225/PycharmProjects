
class Employee:  # parent class

    raise_amt = 1.04  # class variable

    def __init__(self, first, last, pay):  #constrauctor
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay =self.pay * self.raise_amt
        #self.pay = int(self.pay * Employee.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        #super().__init__(self,first, last, pay)
        Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self,first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Amit', 'Saxena', 50000, 'Python')
dev_2 = Developer('XXXX', 'ZZZZZ', 60000, 'Java')

mgr_1 = Manager('Manager1', 'Surname1', 90000, [dev_1])
emps =  Employee('Sanjay', 'bbbbb', 50000,)

print (emps.apply_raise())

#print (dev_1.raise_amt)

#print (mgr_1.fullname())

#print(mgr_1.raise_amt)

#mgr_1.add_emp(dev_2)
#mgr_1.remove_emp(dev_2)

#print (mgr_1.print_emps())
