import time
import os
import schedule
import datetime

now = datetime.datetime.now()
print(now)

def get_time(n):
    while True:
        now = datetime.datetime.now()
        print(now)
        print('------------------------------------------------------------------------')
        time.sleep(5)

def job4():
    print('Job4')
    print('Job4-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(20)
    print('Job4-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print('------------------------------------------------------------------------')
get_time(5)
if __name__ == "__main__":
    schedule.every().day.at('11:21').do(job4)
    while True:
        schedule.run_pending()

