from crontab import CronTab

my_cron = CronTab(user='nineleaps')
job = my_cron.new(command='python /home/nineleaps/PycharmProjects/cabBooking/task.py', comment='dateinfo')
job.day.every(1)

my_cron.write()

# for job in my_cron:
#     if job.comment == 'dateinfo':
#         job.hour.every(10)
#         my_cron.write()
#         print ('Cron job modified successfully')

# my_cron.remove_all()
# my_cron.write()