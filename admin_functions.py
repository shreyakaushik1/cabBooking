import datetime
import builtins
from prettytable import PrettyTable
from admin_database import AdminToDatabase

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
        month_wise_rows = self.admin_db.get_total_bookings_month(d.strftime('%m'))
        if month_wise_rows:
            print("Month wise:" + str(month_wise_rows[0]))
        else:
            print("Month wise data not available")
        date_wise_rows = self.admin_db.get_total_bookings_date(date_input)
        if date_wise_rows:
            print("Day wise:" + str(date_wise_rows[0]))
        else:
            print("Date wise data not available")
        weeknumber = d.strftime("%V")
        week_wise_rows = self.admin_db.get_total_bookings_week(str(int(weeknumber)-1))
        if week_wise_rows:
            print("Week wise:" + str(week_wise_rows[0]))
        else:
            print("Week wise data not available")
        return True

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
        if rows:
            self.show_employee_details(rows)
            emp_id = builtins.input("Please enter the Employee Id for whom you want to see the booking details: ")
            rows = self.admin_db.get_employee_booking_details(int(emp_id))
            if rows:
                self.show_employee_booking_details(rows)
                return True
            else:
                print("Booking details of the employee not available")
                return False
        else:
            print("Employee details not available")
            return False

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
            insert_cab_time = self.admin_db.insert_cab_timings(cab_number, timings)
            if insert_cab_time:
                another_time = builtins.input("Do you want to add another timing?(True/False) ")
            else:
                print("Adding cab time failed. Please try again")
        cab_ids = self.admin_db.get_all_cab_ids(cab_number)
        if cab_ids:
            source = builtins.input("Enter the source from where the cab starts?: ")
            final_dest = "False"
            while final_dest == "False":
                dest = builtins.input("Enter the destination: ")
                for id in cab_ids:
                    insert_cab_route = self.admin_db.insert_new_cab_route(int(id[0]), source, dest)
                    if not insert_cab_route:
                        print("Cab route not added. Please try again")
                final_dest = builtins.input("Is this the Final destination?(True/False) ")
                if final_dest != "True":
                    source = dest
            return True
        else:
            print("Problem occurred. Please try again")
            return False

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
        if rows:
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
                update_cab_time = self.admin_db.update_cab_timing(new_time, int(cab_id))
                return update_cab_time
            elif update_param == "2":
                cab_number = builtins.input("Enter Cab Number: ")
                timings = builtins.input("Enter the timing for the cab: ")
                insert_cab_timing = self.admin_db.insert_cab_timings(cab_number, timings)
                return insert_cab_timing
            elif update_param == "3":
                route_id = builtins.input("Please enter the route id: ")
                new_source = builtins.input("Please Enter the new source: ")
                new_destination = builtins.input("Please Enter the new destination: ")
                update_cab_route = self.admin_db.update_cab_route(new_source, new_destination, int(route_id))
                return update_cab_route
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
            return True
        else:
            print("No cab routes available")
            return False

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

