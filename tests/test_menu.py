import unittest
import mock
from menu import Menu
import builtins
import sqlite3


class MyTestCase(unittest.TestCase):

    @mock.patch('sqlite3.connect')
    @mock.patch('builtins.input', side_effect=['2', 'exit'])
    @mock.patch('admin_functions.Admin.indirect')
    def test_adminmenu(self, mockdata, mock_input, mocksql):
        mocksql = mock.Mock()
        m = Menu()
        m.admin_menu(mocksql, 1)
        mockdata.assert_called_once()

    @mock.patch('sqlite3.connect')
    @mock.patch('builtins.input', side_effect=['2', 'exit'])
    @mock.patch('employee_functions.Employee.indirect')
    def test_employeemenu(self, mockdata, mock_input, mocksql):
        mocksql = mock.Mock()
        m = Menu()
        m.employee_menu(mocksql, 1)
        mockdata.assert_called_once()


if __name__ == '__main__':
    unittest.main()
