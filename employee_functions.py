import datetime
import sqlite3
import builtins
from prettytable import PrettyTable

# TODO close connection in each class


class Employee(object):

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
            function to book a cab
        :return: True if executed successfully else False
        """
        source = builtins.input("Please Enter the source: ")
        dest = builtins.input("Please Enter the destination: ")
        timing = builtins.input("Please Enter the timing: ")
        try:
            self.cur.execute("SELECT * FROM Cab join Routes on Cab.Id = Routes.`Cab Id` WHERE `Timing` > ? and `seats` > 0", (timing,))
            rows = self.cur.fetchall()
            x = PrettyTable()
            x.field_names = ["Cab Number", "Timing", "Route Id", "Source", "Destination", "Seats Available"]
            for r in rows:
                x.add_row([r[1], r[2], r[3], r[5], r[6], r[7]])
            print(x)
            another_route = "True"
            while another_route == "True":
                route_id = builtins.input("Please enter the route id: ")
                self.cur.execute("INSERT INTO Booking (`Route Id`, `Date`, `Employee Id`, `Status`) values (?,?,?,?)",
                                 (int(route_id), datetime.datetime.today(), self.id, "UPCOMING"))
                self.conn.commit()
                self.cur.execute("SELECT `Seats` FROM Routes WHERE `Id` = ?", (int(route_id),))
                seat = self.cur.fetchone()
                self.cur.execute("UPDATE Routes SET `Seats` = ? WHERE `Id` = ?",
                                 (int(seat[0])-1, int(route_id)))
                self.conn.commit()
                another_route = builtins.input("Do you want to add another route?(True/False) ")
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def number_2(self):
        """
            function to view all the past bookings
        :return: True if executed successfully else False
        """
        try:
            self.cur.execute("SELECT * FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE Status = ? and `Employee Id` = ?", ('PAST', self.id))
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
            function to view all upcoming bookings
        :return: True if executed successfully else False
        """
        try:
            self.cur.execute("SELECT * FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE Status = ? and `Employee Id` = ?", ('UPCOMING', self.id))
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

    def number_4(self):
        """
            function to cancel an upcoming booking
        :return: True if executed successfully else False
        """
        try:
            print("Following are the upcoming bookings: ")
            time_delta = datetime.datetime.now() + datetime.timedelta(minutes=30)
            print(time_delta.strftime("%H:%M"))
            self.cur.execute(
                "SELECT * FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on Cab.Id = Routes.`Cab Id` WHERE Status = ? and `Employee Id` = ? and `Timing` > ?",
                ('UPCOMING', self.id, time_delta.strftime("%H:%M")))
            rows = self.cur.fetchall()
            x = PrettyTable()
            x.field_names = ["Booking Id", "Cab Number", "Timing", "Route Id", "Source", "Destination", "Date", "Status"]
            for r in rows:
                x.add_row([r[0], r[11], r[12], r[1], r[7], r[8], r[2], r[4]])
            print(x)
            cancel_booking = builtins.input("Please enter the Booking Id of the booking you want to cancel: ")
            self.cur.execute("UPDATE Booking SET `Status` = ? WHERE `Id` = ?",
                             ("CANCELLED", int(cancel_booking)))
            self.conn.commit()
            self.cur.execute("SELECT `Route Id` FROM Booking WHERE `Id` = ?", (int(cancel_booking),))
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
