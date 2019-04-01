import time
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import itchat
import logging
logging.basicConfig()
itchat.auto_login(hotReload=True)

alarm = "Hi, it's time for you to clean the room! Thank you for your cooperation. The classroom becomes better with your generous contributions."

Duty_Table_Single = [['James','Flora','liucong'],['Shane','Frank','Barry'],['Rachel','Catherine','Lena'],['Leon','Cassandra'],['Brett','Elina']]
Duty_Table_Double = [['Micheal','Nancy','Tony'],['Chelsea','Hermione'],['Horace','Summer','Erica'],['Ella','David_D'],['Grace','Joerica','George']]

today = int(time.strftime('%w'))
today = today-1

def job_func():
    itchat.send(msg = "cyka Blyat", toUserName = None)

def judge():
    time1 = datetime.datetime.now()
    time1 = time1.strftime('%Y-%m-%d %H:%M:%S')
    d1 = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.strptime('2019-03-11 00:00:00', '%Y-%m-%d %H:%M:%S')
    delta = d1 - d2
    diff = delta.days
    ans = diff/7
    if ans%2 == 0:
        return Duty_Table_Single
    else:
        return Duty_Table_Double

def send_message(namee, message_content):
    middle = itchat.search_friends(name=namee)
    user_wechat_name = middle[0]["UserName"]
    itchat.send(message_content,user_wechat_name)

def send_message_eachone(today,Table):
    today_list = Table[today]
    numm = len(today_list)
    for i in range(0,numm):
        send_message(today_list[i],alarm)

def send_message_fixed():
    Table = judge()
    today_table = Table[today]
    numm = len(today_table)
    for i in range(0,numm):
        send_message(today_table[i],alarm)

sched = BlockingScheduler()
sched.add_job(send_message_fixed,'cron', day_of_week = 'mon-fri', hour = 12 , minute = 00
              , end_date='2020-05-05')
sched.add_job(send_message_fixed,'cron', day_of_week = 'mon-fri', hour = 16 , minute = 30 , end_date='2020-05-05')
sched.start()