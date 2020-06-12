import builtins
import sqlite3
import unittest
import mock
from admin_functions import Admin


class TestAdminFunctions(unittest.TestCase):

    @mock.patch('admin_functions.Admin.number_1', return_value=True)
    @mock.patch('main.create_connection')
    @mock.patch('sqlite3.connect')
    def test_indirect(self, mockfunction, mockconnection, mocksql):
        g = Admin(mockconnection, 1)
        m = g.indirect(1)
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value="12-01-2020")
    @mock.patch('admin_database.AdminToDatabase.get_total_bookings_month', return_value=[True])
    @mock.patch('admin_database.AdminToDatabase.get_total_bookings_date', return_value=[True])
    @mock.patch('admin_database.AdminToDatabase.get_total_bookings_week', return_value=[True])
    def test_number_1(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Admin(mockconnection, 1)
        m = g.number_1()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.get_all_employees', return_value=True)
    @mock.patch('admin_functions.Admin.show_employee_details', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.get_employee_booking_details', return_value=True)
    @mock.patch('admin_functions.Admin.show_employee_booking_details', return_value=True)
    def test_number_2(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab, mockshowbooking):
        g = Admin(mockconnection, 1)
        m = g.number_2()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.get_all_employees', return_value=True)
    @mock.patch('admin_functions.Admin.show_employee_details', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.get_employee_booking_details', return_value=False)
    def test_number_2_false1(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Admin(mockconnection, 1)
        m = g.number_2()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.get_all_employees', return_value=False)
    def test_number_2_false2(self, mockconnection, mockinput, mockgetcab):
        g = Admin(mockconnection, 1)
        m = g.number_2()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.insert_cab_timings', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_ids', return_value=["10"])
    @mock.patch('admin_database.AdminToDatabase.insert_new_cab_route', return_value=True)
    def test_number_3(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Admin(mockconnection, 1)
        m = g.number_3()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.insert_cab_timings', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_ids', return_value=False)
    def test_number_3_false(self, mockconnection, mockinput, mockgetcab, mockshowcab):
        g = Admin(mockconnection, 1)
        m = g.number_3()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value='1')
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_functions.Admin.show_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.update_cab_timing', return_value=True)
    def test_number_4_true1(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Admin(mockconnection, 1)
        m = g.number_4()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value='1')
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_functions.Admin.show_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.update_cab_timing', return_value=False)
    def test_number_4_false1(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Admin(mockconnection, 1)
        m = g.number_4()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value='2')
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_functions.Admin.show_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.insert_cab_timings', return_value=True)
    def test_number_4_true2(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Admin(mockconnection, 1)
        m = g.number_4()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value='2')
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_functions.Admin.show_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.insert_cab_timings', return_value=False)
    def test_number_4_false2(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Admin(mockconnection, 1)
        m = g.number_4()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value='3')
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_functions.Admin.show_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.update_cab_route', return_value=True)
    def test_number_4_true3(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Admin(mockconnection, 1)
        m = g.number_4()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value='3')
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_functions.Admin.show_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.update_cab_route', return_value=False)
    def test_number_4_false3(self, mockconnection, mockinput, mockgetcab, mockshowcab, mockbookcab):
        g = Admin(mockconnection, 1)
        m = g.number_4()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value='7')
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_routes_and_timing', return_value=True)
    @mock.patch('admin_functions.Admin.show_cab_routes_and_timing', return_value=True)
    def test_number_4_false5(self, mockconnection, mockinput, mockgetcab, mockshowcab):
        g = Admin(mockconnection, 1)
        m = g.number_4()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value='4')
    @mock.patch('admin_database.AdminToDatabase.get_all_cab_routes_and_timing', return_value=False)
    def test_number_4_false6(self, mockconnection, mockinput, mockgetcab):
        g = Admin(mockconnection, 1)
        m = g.number_4()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.create_new_employee', return_value=True)
    def test_number_5(self, mockconnection, mockinput, mockgetcab):
        g = Admin(mockconnection, 1)
        m = g.number_5()
        assert m is True

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.create_new_employee', return_value=False)
    def test_number_5_false(self, mockconnection, mockinput, mockgetcab):
        g = Admin(mockconnection, 1)
        m = g.number_5()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.get_all_employees', return_value=False)
    def test_number_7_false1(self, mockconnection, mockinput, mockgetcab):
        g = Admin(mockconnection, 1)
        m = g.number_7()
        assert m is False

    @mock.patch('main.create_connection')
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.get_all_employees', return_value=True)
    @mock.patch('admin_database.AdminToDatabase.delete_employee', return_value=False)
    @mock.patch('admin_functions.Admin.show_employee_details', return_value=True)
    def test_number_7_false2(self, mockconnection, mockinput, mockgetcab, mockshowemp, mockdeleteemp):
        g = Admin(mockconnection, 1)
        m = g.number_7()
        assert m is False




