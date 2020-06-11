import datetime
import builtins
from prettytable import PrettyTable
from employee_database import EmployeeDatabase
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
        return True

    def number_1(self):
        """
            function to book a cab
        :return: True if executed successfully else False
        """
        source = builtins.input("Please Enter the source: ")
        dest = builtins.input("Please Enter the destination: ")
        timing = builtins.input("Please Enter the timing: ")
        rows = self.employee_db.get_cab_for_timing(timing)
        if rows:
            self.show_cab_for_timing(rows)
            another_route = "True"
            while another_route == "True":
                route_id = builtins.input("Please enter the route id: ")
                cab_book = self.employee_db.book_a_cab(int(route_id))
                if cab_book is True:
                    another_route = builtins.input("Do you want to add another route?(True/False) ")
                    return True
                else:
                    print("Problem encountered while booking cab, Please try again")
                    return False
        else:
            print("No cabs encountered")
            return False

    def show_booking_details(self, rows):
        x = PrettyTable()
        x.field_names = ["Cab Number", "Timing", "Route Id", "Source", "Destination", "Date", "Status"]
        for r in rows:
            x.add_row([r[11], r[12], r[1], r[7], r[8], r[2], r[4]])
        print(x)
        return True

    def number_2(self):
        """
            function to view all the past bookings
        :return: True if executed successfully else False
        """
        status = 'PAST'
        rows = self.employee_db.get_booking_details(status)
        if rows:
            self.show_booking_details(rows)
            return True
        else:
            print('No booking details available')
            return False

    def number_3(self):
        """
            function to view all upcoming bookings
        :return: True if executed successfully else False
        """
        status = 'UPCOMING'
        rows = self.employee_db.get_booking_details(status)
        if rows:
            self.show_booking_details(rows)
            return True
        else:
            print('No booking details available')
            return False

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
        rows = self.employee_db.get_upcoming_booking_details(time_delta.strftime("%H:%M"))
        if rows:
            self.show_upcoming_bookings(rows)
            cancel_booking = builtins.input("Please enter the Booking Id of the booking you want to cancel: ")
            cancel_booking_status = self.employee_db.cancel_booking(int(cancel_booking))
            if cancel_booking_status:
                print("Booking cancelled successfully")
                return True
            else:
                print("Problem Encountered while cancelling booking. Please try again.")
                return False
        else:
            print("There are no upcoming bookings that can be cancelled")
            return False

