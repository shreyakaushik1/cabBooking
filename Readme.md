# Cab Booking Console Application

About project:

A Console Application where a user can book a cab between different client locations. Multiple employees can book the same cab to travel to client locations or in between stops. Each cab will have a dedicated route and will travel to and fro at different timings.


To run the project:
1. Open terminal in project folder
2. Run `source venv/bin/activate`
3. Run `export PYTHONPATH='.'`
4. Run `python main.py`

Credentials:

For Admin:

username = admin\
password = admin

For Employee:

username = nate\
password = nate


To run unit tests:\
Run `coverage run -m pytest`

To start cron job:\
Run `python scheduler.py`