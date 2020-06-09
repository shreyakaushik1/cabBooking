import sqlite3
import smtplib, ssl
import datetime


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


if __name__ == "__main__":
    database = '/home/nineleaps/PycharmProjects/cabBooking/booking'
    conn = create_connection(database)
    cur = conn.cursor()
    date_input = datetime.datetime.strftime(datetime.datetime.today(), '%d-%m-%Y')
    print(date_input)
    cur.execute("SELECT count(*) FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                "Cab.Id = Routes.`Cab Id` WHERE strftime('%d-%m-%Y',DATE(`Date`)) = ?", (date_input,))
    rows = cur.fetchall()
    cur.execute("SELECT count('Employee Id'), `Destination`  FROM Booking join Routes on Booking.`Route Id` = Routes.Id join Cab on "
                "Cab.Id = Routes.`Cab Id` WHERE strftime('%d-%m-%Y',DATE(`Date`)) = ? GROUP BY `Destination`", (date_input,))
    emps = cur.fetchall()
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "herewegoagain478@gmail.com"
    receiver_email = "shreyasgnr@gmail.com"
    password = "sacredgames"
    message = "Total bookings done today: " + str(rows)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
