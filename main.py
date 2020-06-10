import sqlite3
from menu import Menu
# #TODO encrypt/Decrypt passwords


def create_connection(db):
    """ create a database connection to the SQLite database
            specified by the db_file
        :param db: database file
        :return: Connection object or None
        """
    conn = None
    try:
        conn = sqlite3.connect(db)
        return conn
    except sqlite3.Error as e:
        print(e)


def login_as_admin(con, username, passw):
    """
        function to login as Admin and redirect it to it's menu
    :param con: connection object
    :param username: Username
    :param passw: Password
    :return: 1
    """
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM Admin where Username=? AND Password=?", (username, passw))

        row = cur.fetchone()
        if row is None:
            print('Please enter correct data')
        else:
            b = Menu()
            b.admin_menu(con, row[0])
        return True
    except sqlite3.Error as e:
        print(e)
        return False


def login_as_employee(con, username, passw):
    """
        function to login as Employee and redirect it to it's menu
    :param con: connection object
    :param username: username string
    :param passw: password string
    :return: 1
    """
    try:
        cur = con.cursor()
        cur.execute("SELECT * FROM Employee where Username=? AND Password=?", (username, passw))

        row = cur.fetchone()
        if row is None:
            print('Please enter correct data')
        else:
            m = Menu()
            m.employee_menu(con, row[0])
        return True
    except sqlite3.Error as e:
        print(e)
        return False


if __name__ == '__main__':

    database = '/home/nineleaps/PycharmProjects/cabBooking/booking'

    conn = create_connection(database)
    print("1 for Admin , 2 for Employee")
    type_of_user = input("Login as:")
    userName = input("Username:")
    password = input("Password:")
    if type_of_user == '1':
        login_as_admin(conn, userName, password)
    elif type_of_user == '2':
        login_as_employee(conn, userName, password)
    else:
        print("Please enter correct data")
