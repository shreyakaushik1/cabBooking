import builtins
import sqlite3
import unittest
import mock
from employee_functions import Employee


class MyTestCase(unittest.TestCase):

    @mock.patch('employee_functions.Employee.number_1', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_indirect(self, mockfunction, mockconnection):
        mocksql = mock.Mock()
        g = Employee(mocksql, 1)
        m = g.indirect(1)
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number1(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        mocksql.cursor().fetchone.return_value = (1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None, None)
        mocksql.cursor().fetchall.return_value = [(1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None, None)]
        g = Employee(mocksql, 1)
        m = g.number_1()
        assert m is True

    @mock.patch('sqlite3.connect')
    def test_number2(self, mockconnection):
        mocksql = mock.Mock()
        mocksql.cursor().fetchall.return_value = [(1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None, None, 'shreya', 'shreya', 'shreya', 'shreya')]
        g = Employee(mocksql, 1)
        m = g.number_2()
        assert m is True

    @mock.patch('sqlite3.connect')
    def test_number3(self, mockconnection):
        mocksql = mock.Mock()
        mocksql.cursor().fetchall.return_value = [(1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None,
                                                   None, 'shreya', 'shreya', 'shreya', 'shreya')]
        g = Employee(mocksql, 1)
        m = g.number_3()
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number4(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().commit.return_value = True
        mocksql.cursor().fetchone.return_value = (1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None, None)
        mocksql.cursor().fetchall.return_value = [(1, 'shrey', 'shrey', 'Shreya', 'Bangalore', 560034, 27, None, None,
                                                   None, 'shreya', 'shreya', 'shreya', 'shreya')]
        g = Employee(mocksql, 1)
        m = g.number_4()
        assert m is True

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number1_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Employee(mocksql, 1)
        m = g.number_1()
        assert m is False

    @mock.patch('sqlite3.connect')
    def test_number2_exception(self, mockconnection):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Employee(mocksql, 1)
        m = g.number_2()
        assert m is False

    @mock.patch('sqlite3.connect')
    def test_number3_exception(self, mockconnection):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Employee(mocksql, 1)
        m = g.number_3()
        assert m is False

    @mock.patch('builtins.input', return_value=True)
    @mock.patch('sqlite3.connect')
    def test_number4_exception(self, mockconnection, mockinput):
        mocksql = mock.Mock()
        mocksql.cursor().execute.side_effect = sqlite3.Error
        g = Employee(mocksql, 1)
        m = g.number_4()
        assert m is False