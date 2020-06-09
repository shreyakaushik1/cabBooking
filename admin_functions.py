import datetime
import sqlite3
import builtins
from prettytable import PrettyTable

# TODO close connection in each class


class Admin(object):

    def __init__(self, con, id):
        self.id = id
        self.conn = con
        self.cur = self.conn.cursor()

    def indirect(self, i):
        """
            function to redirect to a specific function
        :param i: number of the method to be called
        :return: method called
        """
        method_name = 'number_' + str(i)
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()

    def number_1(self):
        """
            function to view total bookings for day, week and month wise
        :return: True if executed successfully else False
        """
        try:
            date_input = builtins.input("Enter the date: ")
            d = datetime.datetime.strptime(date_input, '%d-%m-%Y')
            self.cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                         "Cab.Id = Routes.`Cab Id` WHERE strftime('%m',DATE(`Date`)) = ?", (d.strftime('%m'), ))
            rows = self.cur.fetchone()
            print("Month wise:" + str(rows[0]))
            self.cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE strftime('%d-%m-%Y',DATE(`Date`)) = ?", (date_input,))
            rows = self.cur.fetchone()
            print("Day wise:" + str(rows[0]))
            weeknumber = d.strftime("%V")
            self.cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE strftime('%W',DATE(`Date`)) = ?", (str(int(weeknumber)-1),))
            rows = self.cur.fetchone()
            print("Week wise:" + str(rows[0]))
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def employee_details(self):
        """
            function to view employee details
        :return: True if executed successfully else False
        """
        try:
            print("Following is the list of Employees: ")
            self.cur.execute("SELECT * FROM Employee")
            rows = self.cur.fetchall()
            x = PrettyTable()
            x.field_names = ["ID", "Username", "Password", "Name", "Email"]
            for row in rows:
                x.add_row([row[0], row[1], row[2], row[3], row[4]])
            print(x)
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def number_2(self):
        """
            function to view bookings by employee id
        :return: True if executed successfully else False
        """
        try:
            self.employee_details()
            emp_id = builtins.input("Please enter the Employee Id for whom you want to see the booking details: ")
            self.cur.execute("SELECT * FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE `Employee Id` = ?", (int(emp_id), ))
            rows = self.cur.fetchall()
            x = PrettyTable()
            x.field_names = ["Cab Number", "Timing", "Route Id", "Source", "Destination", "Date", "Status"]
            for r in rows:
                x.add_row([r[11], r[12], r[1], r[7], r[8], r[2], r[4]])
            print(x)
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def number_3(self):
        """
            function to add new cab
        :return: True if executed successfully else False
        """
        try:
            print("Please enter the following details for the new cab: ")
            cab_number = builtins.input("Enter Cab Number: ")
            another_time = "True"
            while another_time == "True":
                timings = builtins.input("Enter the timing for the cab: ")
                another_time = builtins.input("Do you want to add another timing?(True/False) ")
                self.cur.execute("INSERT INTO Cab (`Cab Number`, `Timing`) values (?,?)", (cab_number, timings))
                self.conn.commit()
            source = builtins.input("Enter the source from where the cab starts?: ")
            self.cur.execute("SELECT `Id` FROM Cab where `Cab Number` = ?", (cab_number, ))
            cab_ids = self.cur.fetchall()
            final_dest = "False"
            while final_dest == "False":
                dest = builtins.input("Enter the destination: ")
                for id in cab_ids:
                    self.cur.execute("INSERT INTO Routes (`Cab Id`, `Source`, `Destination`, `Seats`) values (?,?,?,?)", (int(id[0]), source, dest, 4))
                    self.conn.commit()
                final_dest = builtins.input("Is this the Final destination?(True/False) ")
                if final_dest != "True":
                    source = dest
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def change_cab_time(self):
        """
            function to change cab timing
        :return: True if executed successfully else False
        """
        try:
            cab_id = builtins.input("Print the Cab Id for which you want to change time: ")
            new_time = builtins.input("Enter the new time: ")
            self.cur.execute("UPDATE Cab SET `Timing` = ? WHERE `Id` = ?",
                             (new_time, int(cab_id)))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def add_new_time(self):
        """
            function to add new timings for cab
        :return: True if executed successfully else False
        """
        try:
            cab_number = builtins.input("Enter Cab Number: ")
            timings = builtins.input("Enter the timing for the cab: ")
            self.cur.execute("INSERT INTO Cab (`Cab Number`, `Timing`) values (?,?)", (cab_number, timings))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def change_route(self):
        """
            function to change route details
        :return: True if executed successfully else False
        """
        try:
            route_id = builtins.input("Please enter the route id: ")
            new_source = builtins.input("Please Enter the new source: ")
            new_destination = builtins.input("Please Enter the new destination: ")
            self.cur.execute("UPDATE Routes SET `Source` = ? , `Destination` = ? WHERE `Id` = ?",
                             (new_source, new_destination, int(route_id)))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def add_new_route(self):
        """
            function to add new route details for a cab
        :return: True if executed successfully else False
        """
        try:
            cab_number = builtins.input("Please enter the cab number for which you want to add new route: ")
            source = builtins.input("Enter the source from where the cab starts?: ")
            self.cur.execute("SELECT `Id` FROM Cab where `Cab Number` = ?", (cab_number,))
            cab_ids = self.cur.fetchall()
            final_dest = "False"
            while final_dest == "False":
                dest = builtins.input("Enter the destination: ")
                for id in cab_ids:
                    self.cur.execute("INSERT INTO Routes (`Cab Id`, `Source`, `Destination`, `Seats`) values (?,?,?,?)",
                                     (int(id[0]), source, dest, 4))
                    self.conn.commit()
                final_dest = builtins.input("Is this the Final destination?(True/False) ")
                if final_dest != "True":
                    source = dest
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def number_4(self):
        """
            function to update cab route and timings
        :return: True if executed successfully else False
        """
        try:
            print("Following are all the routes and cab timings: ")
            self.cur.execute("SELECT * FROM Cab join Routes on Routes.`Cab Id` = Cab.Id")
            rows = self.cur.fetchall()
            x = PrettyTable()
            x.field_names = ["Cab Id", "Cab Number", "Timing", "Route Id", "Source", "Destination", "Seats"]
            for r in rows:
                x.add_row([r[0], r[1], r[2], r[3], r[5], r[6], r[7]])
            print(x)
            print("Following are the things you can update: ")
            print("1. Change an already existing cab time")
            print("2. Add new cab time")
            print("3. Change an already existing Route")
            print("4. Add a new cab route")
            update_param = builtins.input("Please enter the param number you want to update: ")
            if update_param == "1":
                self.change_cab_time()
            elif update_param == "2":
                self.add_new_time()
            elif update_param == "3":
                self.change_route()
            elif update_param == "4":
                self.add_new_route()
            else:
                print("Please enter correct number")
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def number_5(self):
        """
            function to add a new employee
        :return: True if executed successfully else False
        """
        try:
            username = builtins.input("Please Enter the username for the new employee: ")
            password = builtins.input("Please Enter the password for the new employee: ")
            name = builtins.input("Please Enter the name of the new employee: ")
            email = builtins.input("Please Enter the email of the new employee: ")
            self.cur.execute("INSERT INTO Employee (`Username`, `Password`, `Name`, `Email`) values (?,?,?,?)",
                                     (username, password, name, email))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def number_6(self):
        """
            function to update an employee's details
        :return: True if executed successfully else False
        """
        try:
            self.employee_details()
            emp_id = builtins.input("Please Enter the employee id of the Employee: ")
            print("Following are the things you can update: ")
            print("1. Username")
            print("2. Password")
            print("3. Name")
            print("4. Email")
            update_param = builtins.input("Please enter the param number you want to update: ")
            if update_param == "1":
                username = builtins.input("Please enter the new username: ")
                self.cur.execute("UPDATE Employee SET `Username` = ? WHERE `Id` = ?",(username, int(emp_id)))
                self.conn.commit()
            elif update_param == "2":
                password = builtins.input("Please enter the new password: ")
                self.cur.execute("UPDATE Employee SET `Password` = ? WHERE `Id` = ?", (password, int(emp_id)))
                self.conn.commit()
            elif update_param == "3":
                name = builtins.input("Please enter the new name: ")
                self.cur.execute("UPDATE Employee SET `Name` = ? WHERE `Id` = ?", (name, int(emp_id)))
                self.conn.commit()
            elif update_param == "4":
                email = builtins.input("Please enter the new Email: ")
                self.cur.execute("UPDATE Employee SET `Email` = ? WHERE `Id` = ?", (email, int(emp_id)))
                self.conn.commit()
            else:
                print("Please enter correct number")
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def number_7(self):
        """
            function to delete an employee
        :return: True if executed successfully else False
        """
        self.employee_details()
        emp_id = builtins.input("Please enter the employee id: ")
        y = builtins.input("Are you sure?(Y?N) The Employee will be permanently deleted. ")
        try:
            if y == 'Y' or y == 'y':
                self.cur.execute("DELETE FROM Employee WHERE `Id`=?", (int(emp_id),))
                self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False






