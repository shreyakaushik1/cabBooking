import datetime
import sqlite3
import builtins
from prettytable import PrettyTable

# TODO close connection in each class


class Employee(object):

    def __init__(self, con, id):
        """
            function to initialize Employee class
        :param con: Database connection object
        :param id: Employee Id
        """
        self.id = id
        self.employee_db = EmployeeDatabase(con, id)

    def indirect(self, i):
        """
            function to redirect to a specific function
        :param i: number of the method to be called
        :return: method called
        """
        method_name = 'number_' + str(i)
        method = getattr(self, method_name, lambda: 'Invalid')
        return method()

    def show_cab_for_timing(self, rows):
        x = PrettyTable()
        x.field_names = ["Cab Number", "Timing", "Route Id", "Source", "Destination", "Seats Available"]
        for r in rows:
            x.add_row([r[1], r[2], r[3], r[5], r[6], r[7]])
        print(x)

    def number_1(self):
        """
            function to book a cab
        :return: True if executed successfully else False
        """
        source = builtins.input("Please Enter the source: ")
        dest = builtins.input("Please Enter the destination: ")
        timing = builtins.input("Please Enter the timing: ")
        rows = self.employee_db.get_cab_for_timing(timing)
        self.show_cab_for_timing(rows)
        another_route = "True"
        while another_route == "True":
            route_id = builtins.input("Please enter the route id: ")
            self.employee_db.book_a_cab(int(route_id))
            another_route = builtins.input("Do you want to add another route?(True/False) ")

    def show_booking_details(self, rows):
        x = PrettyTable()
        x.field_names = ["Cab Number", "Timing", "Route Id", "Source", "Destination", "Date", "Status"]
        for r in rows:
            x.add_row([r[11], r[12], r[1], r[7], r[8], r[2], r[4]])
        print(x)

    def number_2(self):
        """
            function to view all the past bookings
        :return: True if executed successfully else False
        """
        status = 'PAST'
        rows = self.employee_db.get_booking_details(status)
        self.show_booking_details(rows)


    def number_3(self):
        """
            function to view all upcoming bookings
        :return: True if executed successfully else False
        """
        status = 'UPCOMING'
        rows = self.employee_db.get_booking_details(status)
        self.show_booking_details(rows)

    def show_upcoming_bookings(self, rows):
        x = PrettyTable()
        x.field_names = ["Booking Id", "Cab Number", "Timing", "Route Id", "Source", "Destination", "Date", "Status"]
        for r in rows:
            x.add_row([r[0], r[11], r[12], r[1], r[7], r[8], r[2], r[4]])
        print(x)

    def number_4(self):
        """
            function to cancel an upcoming booking
        :return: True if executed successfully else False
        """
        print("Following are the upcoming bookings: ")
        time_delta = datetime.datetime.now() + datetime.timedelta(minutes=30)
        print(time_delta.strftime("%H:%M"))
        rows = self.employee_db.get_upcoming_booking_details(time_delta.strftime("%H:%M"))
        self.show_upcoming_bookings(rows)
        cancel_booking = builtins.input("Please enter the Booking Id of the booking you want to cancel: ")
        self.employee_db.cancel_booking(int(cancel_booking))


class EmployeeDatabase(object):

    def __init__(self, con, id):
        """
            function to initialize Employee class
        :param con: Database connection object
        :param id: Employee Id
        """
        self.id = id
        self.conn = con
        self.cur = self.conn.cursor()

    def get_cab_for_timing(self, timing):
        try:
            self.cur.execute("SELECT * FROM Cab join Routes on Cab.Id = Routes.`Cab Id` "
                             "WHERE `Timing` > ? and `seats` > 0", (timing,))
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print(e)
            return False

    def book_a_cab(self, route_id):
        try:
            self.cur.execute("INSERT INTO Booking (`Route Id`, `Date`, `Employee Id`, `Status`) values (?,?,?,?)",
                             (route_id, datetime.datetime.today(), self.id, "UPCOMING"))
            self.conn.commit()
            self.cur.execute("SELECT `Seats` FROM Routes WHERE `Id` = ?", (route_id,))
            seat = self.cur.fetchone()
            self.cur.execute("UPDATE Routes SET `Seats` = ? WHERE `Id` = ?",
                             (int(seat[0]) - 1, route_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def get_booking_details(self, status):
        try:
            self.cur.execute("SELECT * FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE Status = ? and `Employee Id` = ?", (status, self.id))
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print(e)
            return False

    def get_upcoming_booking_details(self, time_delta):
        try:
            self.cur.execute("SELECT * FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE Status = ? and `Employee Id` = ? and `Timing` > ?",
                             ('UPCOMING', self.id, time_delta))
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print(e)
            return False

    def cancel_booking(self, booking_id):
        try:
            self.cur.execute("UPDATE Booking SET `Status` = ? WHERE `Id` = ?",
                             ("CANCELLED", booking_id))
            self.conn.commit()
            self.cur.execute("SELECT `Route Id` FROM Booking WHERE `Id` = ?", (booking_id,))
            route_id = self.cur.fetchone()
            self.cur.execute("SELECT `Seats` FROM Routes WHERE `Id` = ?", (int(route_id[0]),))
            seat = self.cur.fetchone()
            self.cur.execute("UPDATE Routes SET `Seats` = ? WHERE `Id` = ?",
                             (int(seat[0]) + 1, int(route_id[0])))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
