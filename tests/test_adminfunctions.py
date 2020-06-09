import builtins
import sqlite3
import unittest
import mock
from admin_functions import Admin


class AdminTestCase(unittest.TestCase):

    @mock.patch('admin_functions.Admin.number_1', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_indirect(self, mockfunction, mockconnection):
        mocksql = mock.Mock()
        g = Admin(mocksql, 1)
        m = g.indirect(1)
        assert m is True

    @mock.patch('builtins.input', return_value='12-01-2020')
    @mock.patch('sqlite3.connect')
    def test_number1(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        mocksql.cursor().fetchone.return_value = (1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None, None)
        g = Admin(mocksql, 1)
        m = g.number_1()
        assert m is True

    @mock.patch('admin_functions.Admin.employee_details', return_value=True)
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number2(self, mockconnection, mockinput, mockfunc):
        mocksql = mock.Mock()
        mocksql.cursor().fetchall.return_value = [(1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None, None, 'shreya', 'shreya', 'shreya', 'shreya')]
        g = Admin(mocksql, 1)
        m = g.number_2()
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number3(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        mocksql.cursor().fetchall.return_value = [(1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None,
                                                   None, 'shreya', 'shreya', 'shreya', 'shreya')]
        g = Admin(mocksql, 1)
        m = g.number_3()
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number4(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().fetchall.return_value = [(1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None,
                                                   None, 'shreya', 'shreya', 'shreya', 'shreya')]
        g = Admin(mocksql, 1)
        m = g.number_4()
        assert m is True

    @mock.patch('builtins.input', return_value='12-02-2020')
    @mock.patch('sqlite3.connect')
    def test_number1_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.number_1()
        assert m is False

    @mock.patch('admin_functions.Admin.employee_details', return_value=True)
    @mock.patch('builtins.input', return_value='12')
    @mock.patch('sqlite3.connect')
    def test_number2_exception(self, mockconnection, mockinput, mockfunc):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.number_2()
        assert m is False

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number3_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.number_3()
        assert m is False

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number4_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.number_4()
        assert m is False

    @mock.patch('sqlite3.connect')
    def test_employeedetails(self, mockconnection):
        mocksql = mock.Mock()
        mocksql.cursor().fetchall.return_value = [(1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None,
                                                   None, 'shreya', 'shreya', 'shreya', 'shreya')]
        g = Admin(mocksql, 1)
        m = g.employee_details()
        assert m is True

    @mock.patch('sqlite3.connect')
    def test_employeedetails_exception(self, mockconnection):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.employee_details()
        assert m is False

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_changecabtime(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        g = Admin(mocksql, 1)
        m = g.change_cab_time()
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_employeedetails_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.change_cab_time()
        assert m is False

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_addnewtime(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        g = Admin(mocksql, 1)
        m = g.add_new_time()
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_addnewtime_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.add_new_time()
        assert m is False

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_changeroute(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        g = Admin(mocksql, 1)
        m = g.change_route()
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_changeroute_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.change_route()
        assert m is False

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_addnewroute(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        mocksql.cursor().fetchall.return_value = [(1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None,
                                                   None, 'shreya', 'shreya', 'shreya', 'shreya')]
        g = Admin(mocksql, 1)
        m = g.add_new_route()
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_addnewroute_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.add_new_route()
        assert m is False

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number5(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        g = Admin(mocksql, 1)
        m = g.number_5()
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number5_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.number_5()
        assert m is False

    @mock.patch('admin_functions.Admin.employee_details', return_value=True)
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number6(self, mockconnection, mockinput, mockfunc):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        g = Admin(mocksql, 1)
        m = g.number_6()
        assert m is True

    @mock.patch('admin_functions.Admin.employee_details', return_value=True)
    @mock.patch('builtins.input', return_value="1")
    @mock.patch('sqlite3.connect')
    def test_number6_exception(self, mockconnection, mockinput, mockfunc):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Admin(mocksql, 1)
        m = g.number_6()
        assert m is False

    @mock.patch('admin_functions.Admin.employee_details', return_value=True)
    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number7(self, mockconnection, mockinput, mockfunc):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        g = Admin(mocksql, 1)
        m = g.number_7()
        assert m is True

