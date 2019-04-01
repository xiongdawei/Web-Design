import datetime

time1 = datetime.datetime.now()

time1 = time1.strftime('%Y-%m-%d %H:%M:%S')


t_str = '2019-03-18 00:00:00'
time2 = datetime.datetime.strptime(t_str,'%Y-%m-%d %H:%M:%S')


d1 = datetime.datetime.strptime(time1, '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2019-03-18 00:00:00', '%Y-%m-%d %H:%M:%S')
delta = d1 - d2
Duty_Table_Single = [['James','Flora','liucong'],['Shane','Frank','Barry'],['Rachel','Catherine','Lena'],['Leon','Cassandra'],['Brett','Elina']]
Duty_Table_Double = [['Micheal','Nancy','Tony'],['Chelsea','Hermione'],['Horace','Summer','Erica'],['Ella','David_D'],['Grace','Joerica','George']]


#d = datetime.datetime.strptime(t_str, '%Y-%m-%d')

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

print(judge())






