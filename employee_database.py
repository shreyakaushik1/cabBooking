import sqlite3
import datetime


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