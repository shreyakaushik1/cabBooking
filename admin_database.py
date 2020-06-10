import sqlite3


class AdminToDatabase(object):

    def __init__(self, con, id):
        self.id = id
        self.conn = con
        self.cur = self.conn.cursor()

    def delete_employee(self, id):
        try:
            self.cur.execute("DELETE FROM Employee WHERE `Id`=?", (id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def update_employee_username(self, username, emp_id):
        try:
            self.cur.execute("UPDATE Employee SET `Username` = ? WHERE `Id` = ?", (username, emp_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def update_employee_pasword(self, password, emp_id):
        try:
            self.cur.execute("UPDATE Employee SET `Password` = ? WHERE `Id` = ?", (password, emp_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def update_employee_name(self, name, emp_id):
        try:
            self.cur.execute("UPDATE Employee SET `Name` = ? WHERE `Id` = ?", (name, emp_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def update_employee_email(self, email, emp_id):
        try:
            self.cur.execute("UPDATE Employee SET `Email` = ? WHERE `Id` = ?", (email, emp_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def create_new_employee(self, username, password, name, email):
        try:
            self.cur.execute("INSERT INTO Employee (`Username`, `Password`, `Name`, `Email`) values (?,?,?,?)",
                             (username, password, name, email))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def get_all_cab_routes_and_timing(self):
        try:
            self.cur.execute("SELECT * FROM Cab join Routes on Routes.`Cab Id` = Cab.Id")
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print(e)
            return False

    def get_all_cab_ids(self, cab_number):
        try:
            self.cur.execute("SELECT `Id` FROM Cab where `Cab Number` = ?", (cab_number,))
            cab_ids = self.cur.fetchall()
            return cab_ids
        except sqlite3.Error as e:
            print(e)
            return False

    def insert_new_cab_route(self, id, source, dest):
        try:
            self.cur.execute("INSERT INTO Routes (`Cab Id`, `Source`, `Destination`, `Seats`) values (?,?,?,?)",
                            (id, source, dest, 4))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def get_total_bookings_month(self, month):
        try:
            self.cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE strftime('%m',DATE(`Date`)) = ?", (month,))
            rows = self.cur.fetchone()
            return rows
        except sqlite3.Error as e:
            print(e)
            return False

    def get_total_bookings_date(self, day):
        try:
            self.cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE strftime('%d-%m-%Y',DATE(`Date`)) = ?", (day,))
            rows = self.cur.fetchone()
            return rows
        except sqlite3.Error as e:
            print(e)
            return False

    def get_total_bookings_week(self, week):
        try:
            self.cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE strftime('%W',DATE(`Date`)) = ?", (week,))
            rows = self.cur.fetchone()
            return rows
        except sqlite3.Error as e:
            print(e)
            return False

    def get_all_employees(self):
        try:
            self.cur.execute("SELECT * FROM Employee")
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print(e)
            return False

    def get_employee_booking_details(self, emp_id):
        try:
            self.cur.execute("SELECT * FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                             "Cab.Id = Routes.`Cab Id` WHERE `Employee Id` = ?", (emp_id,))
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print(e)
            return False

    def insert_cab_timings(self, cab_number, timings):
        try:
            self.cur.execute("INSERT INTO Cab (`Cab Number`, `Timing`) values (?,?)", (cab_number, timings))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def update_cab_timing(self, new_time, cab_id):
        try:
            self.cur.execute("UPDATE Cab SET `Timing` = ? WHERE `Id` = ?",
                             (new_time, cab_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False

    def update_cab_route(self, source, dest, route_id):
        try:
            self.cur.execute("UPDATE Routes SET `Source` = ? , `Destination` = ? WHERE `Id` = ?",
                             (source, dest, route_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            return False
