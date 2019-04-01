import time
from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'date', run_date='2019-03-27 00:03:40')
    scheduler.start()