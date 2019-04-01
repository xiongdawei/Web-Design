import itchat
import time


itchat.auto_login(hotReload=True)
#itchat.send("If you receive this message, it means David X's program is working", toUserName = daizhibo0804)
#itchat.send("If you receive this message, it means that David X's program is working", toUserName = "joandavidkevin")
#itchat.send("Hello, filehelper", toUserName="filehelper")

#name = itchat.search_friends(name= u'Dby')
#daizhibo = name[0]["UserName"]
message_content = "If you see this message, it means that david X's program is working"
apologize = "If you see this message, it means that David X is coding on his new project, please feel free and do your own stuff"
alarm = "Hi, it's time for you to clean the room! Thank you for your cooperation. The classroom becomes better with your generous contributions."
#itchat.send(message_content,daizhibo)

def send_message(namee, message_content):
    middle = itchat.search_friends(name=namee)
    user_wechat_name = middle[0]["UserName"]
    itchat.send(message_content,user_wechat_name)

#name1 = "James"
#name2 = "Hermione"

#send_message(name1,apologize)
#send_message(name2,apologize)

Duty_Table_Single = [['James','Flora','liucong'],['Shane','Frank','Barry'],['Rachel','Catherine','Lena'],['Leon','Cassandra'],['Brett','Elina']]
Duty_Table_Double = [['Micheal','Nancy','Tony'],['Chelsea','Hermione'],['Horace','Summer','Erica'],['Ella','David_D'],['Grace','Joerica','George']]

today = int(time.strftime('%w'))
today = today-1

def send_message_eachone(today,Table):
    today_list = Table[today]
    numm = len(today_list)
    for i in range(0,numm):
        send_message(today_list[i],alarm)
send_message_eachone(today,Duty_Table_Single)


