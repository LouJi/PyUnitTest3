import unittest
import employee

'''
WET version
'''

class  TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1=employee.Employee('John', 'Smith', 72000)
        emp_2=employee.Employee('Jane', 'Doe', 85000)

        self.assertEqual(emp_1.email, 'John.Smith@company.com')
        self.assertEqual(emp_2.email, 'Jane.Doe@company.com')

        emp_1.first= 'Joe'
        emp_2.last= 'Smith'

        self.assertEqual(emp_1.email, 'Joe.Smith@company.com')
        self.assertEqual(emp_2.email, 'Jane.Smith@company.com')

    def test_fullname(self):
        emp_1=employee.Employee('John', 'Smith', 72000)
        emp_2=employee.Employee('Jane', 'Doe', 85000)

        self.assertEqual(emp_1.fullname, 'John Smith')
        self.assertEqual(emp_2.fullname, 'Jane Doe')

        emp_1.last = 'Jones'
        emp_2.last = 'Main'

        self.assertEqual(emp_1.fullname, 'John Jones')
        self.assertEqual(emp_2.fullname, 'Jane Main')

    def test_apply_raise(self):
        emp_1 = employee.Employee('John', 'Smith', 72000)
        emp_2 = employee.Employee('Jane', 'Doe', 85000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 75600)
        self.assertEqual(emp_2.pay, 89250)

#to run the test in the terminal of the Python IDE and in cmd prompt use the python filename.
if __name__ == '__main__':
    unittest.main()
