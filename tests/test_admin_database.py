import builtins
import sqlite3
import unittest
import mock
from admin_database import AdminToDatabase


class TestAdminDatabase(unittest.TestCase):

    @mock.patch('sqlite3.connect')
    def test_delete_employee_error(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().execute.side_effect = sqlite3.Error
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.delete_employee(1)
        assert r is False

    @mock.patch('sqlite3.connect')
    def test_delete_employee(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().commit.side_effect = True
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.delete_employee(1)
        assert r is True

    @mock.patch('sqlite3.connect')
    def test_update_employee_username(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().commit.side_effect = True
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.update_employee_username('username',1)
        assert r is True

    @mock.patch('sqlite3.connect')
    def test_update_employee_username_error(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().execute.side_effect = sqlite3.Error
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.update_employee_username('username',1)
        assert r is False

    @mock.patch('sqlite3.connect')
    def test_update_employee_pasword(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().commit.side_effect = True
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.update_employee_pasword('username', 1)
        assert r is True

    @mock.patch('sqlite3.connect')
    def test_update_employee_pasword_error(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().execute.side_effect = sqlite3.Error
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.update_employee_pasword('username', 1)
        assert r is False

    @mock.patch('sqlite3.connect')
    def test_update_employee_name(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().commit.side_effect = True
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.update_employee_name('username', 1)
        assert r is True

    @mock.patch('sqlite3.connect')
    def test_update_employee_name_error(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().execute.side_effect = sqlite3.Error
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.update_employee_name('username', 1)
        assert r is False

    @mock.patch('sqlite3.connect')
    def test_update_employee_email(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().commit.side_effect = True
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.update_employee_pasword('username', 1)
        assert r is True

    @mock.patch('sqlite3.connect')
    def test_update_employee_email_error(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().execute.side_effect = sqlite3.Error
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.update_employee_pasword('username', 1)
        assert r is False

    @mock.patch('sqlite3.connect')
    def test_create_new_employee(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().commit.side_effect = True
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.create_new_employee('username','password', 'name', 'email')
        assert r is True

    @mock.patch('sqlite3.connect')
    def test_create_new_employee_error(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().execute.side_effect = sqlite3.Error
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.create_new_employee('username','password', 'name', 'email')
        assert r is False

    @mock.patch('sqlite3.connect')
    def test_get_all_cab_routes_and_timing(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().fetchall.side_effect = [True]
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.get_all_cab_routes_and_timing()
        assert r is True

    @mock.patch('sqlite3.connect')
    def test_get_all_cab_routes_and_timing_error(self, mockconnection):
        mockconnection = mock.Mock()
        mockconnection.cursor().execute.side_effect = sqlite3.Error
        test_class = AdminToDatabase(mockconnection, 1)
        r = test_class.get_all_cab_routes_and_timing()
        assert r is False

