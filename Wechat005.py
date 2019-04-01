"""
today = int(time.strftime('%w'))
today = today-1
print(today)

Duty_Table_Single = [['James','Flora','Eric'],['Shane','Frank','Barry'],['Rachel','Cathering','Lena'],['Leon','Cassandra'],['Brett','Elina']]
how_many = len(Duty_Table_Single[today])
print(Duty_Table_Single[today])

def send_message_to_eachone()
"""
import time

timee = time.localtime(time.time())
print(timee.tm_wday)

timeee = int(time.strftime('%w'))
print(timeee)
