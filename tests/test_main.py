import mock
import pytest
from doubles import allow, expect
from main import login_as_admin, login_as_employee, create_connection
import unittest
import sqlite3


class TestClass1(unittest.TestCase):

    @mock.patch('menu.Menu.admin_menu')
    @mock.patch('sqlite3.connect')
    def test_loginasadmin(self, mockConnection, mock_menu):
        mocksql = mock.Mock()
        mocksql.cursor().fetchone.return_value = (1, 'aj')
        m = login_as_admin(mocksql, 'hhhhh', 'hhhhh')
        assert m == 1

    @mock.patch('menu.Menu.employee_menu')
    @mock.patch('sqlite3.connect')
    def test_loginasemployee(self, mockConnection, mock_menu):
        mocksql = mock.Mock()
        mocksql.cursor().fetchone.return_value = (1, 'aj')
        m = login_as_employee(mocksql, 'hhhhh', 'hhhhh')
        assert m == 1

    @mock.patch('sqlite3.connect', return_value='1')
    def test_createconnection(self, mockconnection):
        db = '/home/nineleaps/PycharmProjects/cabBooking/booking'
        m = create_connection(db)
        assert m == '1'

    @mock.patch('builtins.print')
    @mock.patch('sqlite3.connect', side_effect=sqlite3.Error)
    def test_createconnectionexception(self, mockconnection, mock_print):
        db = '/home/nineleaps/PycharmProjects/cabBooking/booking'
        create_connection(db)
        mock_print.assert_called_once()


if __name__ == '__main__':
    unittest.main()
