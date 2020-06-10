import datetime
import sqlite3
import builtins
from prettytable import PrettyTable

# TODO close connection in each class


class Admin(object):

    def __init__(self, con, id):
        self.id = id
        self.admin_db = AdminToDatabase(con, id)

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
        date_input = builtins.input("Enter the date: ")
        d = datetime.datetime.strptime(date_input, '%d-%m-%Y')
        rows = self.admin_db.get_total_bookings_month(d.strftime('%m'))
        print("Month wise:" + str(rows[0]))
        rows = self.admin_db.get_total_bookings_date(date_input)
        print("Day wise:" + str(rows[0]))
        weeknumber = d.strftime("%V")
        rows = self.admin_db.get_total_bookings_week(str(int(weeknumber)-1))
        print("Week wise:" + str(rows[0]))

    def show_employee_details(self, rows):
        """
            function to view employee details
        :return: True if executed successfully else False
        """
        x = PrettyTable()
        x.field_names = ["ID", "Username", "Password", "Name", "Email"]
        for row in rows:
            x.add_row([row[0], row[1], row[2], row[3], row[4]])
        print(x)

    def show_employee_booking_details(self, rows):
        x = PrettyTable()
        x.field_names = ["Cab Number", "Timing", "Route Id", "Source", "Destination", "Date", "Status"]
        for r in rows:
            x.add_row([r[11], r[12], r[1], r[7], r[8], r[2], r[4]])
        print(x)

    def number_2(self):
        """
            function to view bookings by employee id
        :return: True if executed successfully else False
        """
        print("Following is the list of Employees: ")
        rows = self.admin_db.get_all_employees()
        self.show_employee_details(rows)
        emp_id = builtins.input("Please enter the Employee Id for whom you want to see the booking details: ")
        rows = self.admin_db.get_employee_booking_details(int(emp_id))
        self.show_employee_booking_details(rows)

    def number_3(self):
        """
            function to add new cab
        :return: True if executed successfully else False
        """
        print("Please enter the following details for the new cab: ")
        cab_number = builtins.input("Enter Cab Number: ")
        another_time = "True"
        while another_time == "True":
            timings = builtins.input("Enter the timing for the cab: ")
            another_time = builtins.input("Do you want to add another timing?(True/False) ")
            self.admin_db.insert_cab_timings(cab_number, timings)
        source = builtins.input("Enter the source from where the cab starts?: ")
        cab_ids = self.admin_db.get_all_cab_ids(cab_number)
        final_dest = "False"
        while final_dest == "False":
            dest = builtins.input("Enter the destination: ")
            for id in cab_ids:
                self.admin_db.insert_new_cab_route(int(id[0]), source, dest)
            final_dest = builtins.input("Is this the Final destination?(True/False) ")
            if final_dest != "True":
                source = dest

    def show_cab_routes_and_timing(self, rows):
        x = PrettyTable()
        x.field_names = ["Cab Id", "Cab Number", "Timing", "Route Id", "Source", "Destination", "Seats"]
        for r in rows:
            x.add_row([r[0], r[1], r[2], r[3], r[5], r[6], r[7]])
        print(x)

    def number_4(self):
        """
            function to update cab route and timings
        :return: True if executed successfully else False
        """
        print("Following are all the routes and cab timings: ")
        rows = self.admin_db.get_all_cab_routes_and_timing()
        self.show_cab_routes_and_timing(rows)
        print("Following are the things you can update: ")
        print("1. Change an already existing cab time")
        print("2. Add new cab time")
        print("3. Change an already existing Route")
        print("4. Add a new cab route")
        update_param = builtins.input("Please enter the param number you want to update: ")
        if update_param == "1":
            cab_id = builtins.input("Print the Cab Id for which you want to change time: ")
            new_time = builtins.input("Enter the new time: ")
            self.admin_db.update_cab_timing(new_time, int(cab_id))
        elif update_param == "2":
            cab_number = builtins.input("Enter Cab Number: ")
            timings = builtins.input("Enter the timing for the cab: ")
            self.admin_db.insert_cab_timings(cab_number, timings)
        elif update_param == "3":
            route_id = builtins.input("Please enter the route id: ")
            new_source = builtins.input("Please Enter the new source: ")
            new_destination = builtins.input("Please Enter the new destination: ")
            self.admin_db.update_cab_route(new_source, new_destination, int(route_id))
        elif update_param == "4":
            cab_number = builtins.input("Please enter the cab number for which you want to add new route: ")
            source = builtins.input("Enter the source from where the cab starts?: ")
            cab_ids = self.admin_db.get_all_cab_ids(cab_number)
            final_dest = "False"
            while final_dest == "False":
                dest = builtins.input("Enter the destination: ")
                for id in cab_ids:
                    self.admin_db.insert_new_cab_route(int(id[0]), source, dest)
                final_dest = builtins.input("Is this the Final destination?(True/False) ")
                if final_dest != "True":
                    source = dest
        else:
            print("Please enter correct number")

    def number_5(self):
        """
            function to add a new employee
        :return: True if executed successfully else False
        """
        username = builtins.input("Please Enter the username for the new employee: ")
        password = builtins.input("Please Enter the password for the new employee: ")
        name = builtins.input("Please Enter the name of the new employee: ")
        email = builtins.input("Please Enter the email of the new employee: ")
        self.admin_db.create_new_employee(username, password, name, email)

    def number_6(self):
        """
            function to update an employee's details
        :return: True if executed successfully else False
        """
        self.admin_db.get_all_employees()
        self.show_employee_details()
        emp_id = builtins.input("Please Enter the employee id of the Employee: ")
        print("Following are the things you can update: ")
        print("1. Username")
        print("2. Password")
        print("3. Name")
        print("4. Email")
        update_param = builtins.input("Please enter the param number you want to update: ")
        if update_param == "1":
            username = builtins.input("Please enter the new username: ")
            self.admin_db.update_employee_username(username, int(emp_id))
        elif update_param == "2":
            password = builtins.input("Please enter the new password: ")
            self.admin_db.update_employee_pasword(password, int(emp_id))
        elif update_param == "3":
            name = builtins.input("Please enter the new name: ")
            self.admin_db.update_employee_name(name, int(emp_id))
        elif update_param == "4":
            email = builtins.input("Please enter the new Email: ")
            self.admin_db.update_employee_email(email, int(emp_id))
        else:
            print("Please enter correct number")


    def number_7(self):
        """
            function to delete an employee
        :return: True if executed successfully else False
        """
        self.admin_db.get_all_employees()
        self.show_employee_details()
        emp_id = builtins.input("Please enter the employee id: ")
        y = builtins.input("Are you sure?(Y?N) The Employee will be permanently deleted. ")
        if y == 'Y' or y == 'y':
            self.admin_db.delete_employee(int(emp_id))



class AdminToDatabase(object):

    def __init__(self, con, id):
        self.id = id
        self.conn = con
        self.cur = self.conn.cursor()

    def delete_employee(self, id):
        self.cur.execute("DELETE FROM Employee WHERE `Id`=?", (id,))
        self.conn.commit()

    def update_employee_username(self, username, emp_id):
        self.cur.execute("UPDATE Employee SET `Username` = ? WHERE `Id` = ?", (username, emp_id))
        self.conn.commit()

    def update_employee_pasword(self, password, emp_id):
        self.cur.execute("UPDATE Employee SET `Password` = ? WHERE `Id` = ?", (password, emp_id))
        self.conn.commit()

    def update_employee_name(self, name, emp_id):
        self.cur.execute("UPDATE Employee SET `Name` = ? WHERE `Id` = ?", (name, emp_id))
        self.conn.commit()

    def update_employee_email(self, email, emp_id):
        self.cur.execute("UPDATE Employee SET `Email` = ? WHERE `Id` = ?", (email, emp_id))
        self.conn.commit()

    def create_new_employee(self, username, password, name, email):
        self.cur.execute("INSERT INTO Employee (`Username`, `Password`, `Name`, `Email`) values (?,?,?,?)",
                         (username, password, name, email))
        self.conn.commit()

    def get_all_cab_routes_and_timing(self):
        self.cur.execute("SELECT * FROM Cab join Routes on Routes.`Cab Id` = Cab.Id")
        rows = self.cur.fetchall()
        return rows

    def get_all_cab_ids(self, cab_number):
        self.cur.execute("SELECT `Id` FROM Cab where `Cab Number` = ?", (cab_number,))
        cab_ids = self.cur.fetchall()
        return cab_ids

    def insert_new_cab_route(self, id, source, dest):
        self.cur.execute("INSERT INTO Routes (`Cab Id`, `Source`, `Destination`, `Seats`) values (?,?,?,?)",
                         (id, source, dest, 4))
        self.conn.commit()

    def get_total_bookings_month(self, month):
        self.cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                         "Cab.Id = Routes.`Cab Id` WHERE strftime('%m',DATE(`Date`)) = ?", (month,))
        rows = self.cur.fetchone()
        return rows

    def get_total_bookings_date(self, day):
        self.cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                         "Cab.Id = Routes.`Cab Id` WHERE strftime('%d-%m-%Y',DATE(`Date`)) = ?", (day,))
        rows = self.cur.fetchone()
        return rows

    def get_total_bookings_week(self, week):
        self.cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                         "Cab.Id = Routes.`Cab Id` WHERE strftime('%W',DATE(`Date`)) = ?", (week,))
        rows = self.cur.fetchone()
        return rows

    def get_all_employees(self):
        self.cur.execute("SELECT * FROM Employee")
        rows = self.cur.fetchall()
        return rows

    def get_employee_booking_details(self, emp_id):
        self.cur.execute("SELECT * FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                         "Cab.Id = Routes.`Cab Id` WHERE `Employee Id` = ?", (emp_id,))
        rows = self.cur.fetchall()
        return rows

    def insert_cab_timings(self, cab_number, timings):
        self.cur.execute("INSERT INTO Cab (`Cab Number`, `Timing`) values (?,?)", (cab_number, timings))
        self.conn.commit()

    def update_cab_timing(self, new_time, cab_id):
        self.cur.execute("UPDATE Cab SET `Timing` = ? WHERE `Id` = ?",
                         (new_time, cab_id))
        self.conn.commit()

    def update_cab_route(self, source, dest, route_id):
        self.cur.execute("UPDATE Routes SET `Source` = ? , `Destination` = ? WHERE `Id` = ?",
                         (source, dest, route_id))
        self.conn.commit()