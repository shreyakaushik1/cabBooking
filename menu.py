import builtins

from admin_functions import Admin
from employee_functions import Employee


class Menu(object):

    def admin_menu(self, con, id):
        """
            function to view admin menu
        :param con: database connection object
        :param id: admin id
        :return:
        """
        entry = ''
        while entry != 'exit':
            print('Following are the functions you can perform.')
            print('1 - Check total bookings')
            print('2 - Check bookings of an Employee')
            print('3 - Add new cab')
            print('4 - Update cab route and timings')
            print('5 - Add new Employee')
            print('6 - Update employee details')
            print('7 - Delete an employee')

            entry = builtins.input('Please enter the code associated with the function you want to perform:')
            if entry != 'exit':
                s = Admin(con, id)
                s.indirect(entry)

    def employee_menu(self, con, id):
        """
            function to view employee's functions
        :param con: database connection object
        :param id: employee id
        :return:
        """
        entry = ''
        while entry != 'exit':
            print('Following are the functions you can perform.')
            print('1 - Book a cab')
            print('2 - View all my Past bookings')
            print('3 - View all my Upcoming bookings')
            print('4 - Cancel an upcoming booking')

            entry = input('Please enter the code associated with the function you want to perform:')
            if entry != 'exit':
                s = Employee(con, id)
                s.indirect(entry)
