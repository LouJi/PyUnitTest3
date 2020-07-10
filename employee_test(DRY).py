import unittest
from unittest.mock import patch
import employee

'''
DRY version
'''

class  TestEmployee(unittest.TestCase):

    def setUp(self):
        #pass
        self.emp_1= employee.Employee('John', 'Smith', 72000)
        self.emp_2= employee.Employee('Jane', 'Doe', 85000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'John.Smith@company.com')
        self.assertEqual(self.emp_2.email, 'Jane.Doe@company.com')

        self.emp_1.first= 'Joe'
        self.emp_2.last= 'Smith'

        self.assertEqual(self.emp_1.email, 'Joe.Smith@company.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@company.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'John Smith')
        self.assertEqual(self.emp_2.fullname, 'Jane Doe')

        self.emp_1.last = 'Jones'
        self.emp_2.last = 'Main'

        self.assertEqual(self.emp_1.fullname, 'John Jones')
        self.assertEqual(self.emp_2.fullname, 'Jane Main')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 75600)
        self.assertEqual(self.emp_2.pay, 89250)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok= True
            mocked_get.return_value.text= 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Smith/May')
            self.assertEqual(schedule, 'Success')

#to run the test in the terminal of the Python IDE and in cmd prompt use the python filename.
if __name__ == '__main__':
    unittest.main()
