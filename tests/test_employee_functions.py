import builtins
import sqlite3
import unittest
import mock
from employee_functions import Employee


class TestEmployeeFunctions(unittest.TestCase):

    @mock.patch('employee_functions.Employee.number_1', return_value=True)
    @mock.patch('main.create_connection')
    @mock.patch('sqlite3.connect')
    def test_indirect(self, mockfunction, mockconnection, mocksql):
        g = Employee(mockconnection, 1)
        m = g.indirect(1)
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.get_cab_for_timing', return_value=True)
    @mock.patch('employee_functions.Employee.show_cab_for_timing', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.book_a_cab', return_value=True)
    def test_number_1(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Employee(mockconnection, 1)
        m = g.number_1()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.get_cab_for_timing', return_value=False)
    def test_number_1_false1(self, mockconnection, mockinput, mockgetcab):
        g = Employee(mockconnection, 1)
        m = g.number_1()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.get_cab_for_timing', return_value=True)
    @mock.patch('employee_functions.Employee.show_cab_for_timing', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.book_a_cab', return_value=False)
    def test_number_1_false2(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Employee(mockconnection, 1)
        m = g.number_1()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('employee_database.EmployeeDatabase.get_booking_details', return_value=True)
    @mock.patch('employee_functions.Employee.show_booking_details', return_value=True)
    def test_number_2(self, mockconnection, mockinput, mockgetcab):
        g = Employee(mockconnection, 1)
        m = g.number_2()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('employee_database.EmployeeDatabase.get_booking_details', return_value=False)
    def test_number_2_false(self, mockconnection, mockinput):
        g = Employee(mockconnection, 1)
        m = g.number_2()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('employee_database.EmployeeDatabase.get_booking_details', return_value=True)
    @mock.patch('employee_functions.Employee.show_booking_details', return_value=True)
    def test_number_3(self, mockconnection, mockinput, mockgetcab):
        g = Employee(mockconnection, 1)
        m = g.number_3()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('employee_database.EmployeeDatabase.get_booking_details', return_value=False)
    def test_number_3_false(self, mockconnection, mockinput):
        g = Employee(mockconnection, 1)
        m = g.number_3()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.get_upcoming_booking_details', return_value=True)
    @mock.patch('employee_functions.Employee.show_upcoming_bookings', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.cancel_booking', return_value=True)
    def test_number_4(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Employee(mockconnection, 1)
        m = g.number_4()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.get_upcoming_booking_details', return_value=True)
    @mock.patch('employee_functions.Employee.show_upcoming_bookings', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.cancel_booking', return_value=False)
    def test_number_4_false1(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Employee(mockconnection, 1)
        m = g.number_4()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('employee_database.EmployeeDatabase.get_upcoming_booking_details', return_value=False)
    def test_number_4_false2(self, mockconnection, mockinput, mockgetcab):
        g = Employee(mockconnection, 1)
        m = g.number_4()
        assert m is False

