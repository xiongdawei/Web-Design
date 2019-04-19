from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, url_for
import re
import sys
import types

import cgi, cgitb

import re

#from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
Base = declarative_base()
engine1 = create_engine('mysql+pymysql://root:cykablyat@localhost:3306/classtime')
DBSession = sessionmaker(bind = engine1)

engine2 = create_engine('mysql+pymysql://root:cykablyat@localhost:3306/User_Data')
DBSession_A = sessionmaker(bind = engine2)

class classslot(Base):
    __tablename__ = 'classslot'
    name = Column(String(200),primary_key=True,nullable= False, index = True)
    place = Column(Integer,primary_key=True,nullable= False, index = True)
    teacher = Column(String(200),primary_key=True,nullable = False, index = True)
    serial = Column(Integer,primary_key=True,nullable = False, index = True )
    week = Column(Integer,primary_key=True, nullable = False, index = True)

class user_data(Base):
    __tablename__ = 'user_data'
    Name = Column(String(50), primary_key=True, nullable=False, index=True)
    Email = Column(String(50), nullable=False, index=True)
    Password = Column(String(20), nullable=False, index=True)
    Group1 = Column(String(10), nullable=False, index=True)
    Group2 = Column(String(10), nullable=False, index=True)
    Group3 = Column(String(10), nullable=False, index=True)
    Group4 = Column(String(10), nullable=False, index=True)
    Group5 = Column(String(10), nullable=False, index=True)
    Group6 = Column(String(10), nullable=False, index=True)
    PE = Column(String(10), nullable=False, index=True)
    TOK = Column(String(10), nullable=False, index=True)
    Class = Column(Integer, nullable=False, index=True)

class function():
    def __init__(self):
        pass

    def add(self,data):
        session = DBSession()
        session.add(data)
        session.commit()
        session.close()

    def add_user_data(self,data):
        """
        :param data: This is the user data, including the all the parameters in user_data
        :return: done
        """
        session = DBSession_A()
        session.add(data)
        session.commit()
        session.close()

    def serach_byname(self,namee):
        session = DBSession()
        results = session.query(classslot).filter(classslot.name == namee).one()
        message_place = results.place
        message_serial = results.serial
        message_week = results.week
        message_teacher = results.teacher
        return message_teacher, message_place,message_serial,message_week

    def serach_byteacher(self,namee):
        session = DBSession()
        results = session.query(classslot).filter(classslot.teacher == namee).one()
        message_place = results.place
        message_serial = results.serial
        message_week = results.week
        message_name = results.name
        return message_name, message_place,message_serial,message_week

    def serach_byplace(self,namee):
        session = DBSession()
        results = session.query(classslot).filter(classslot.place == namee).one()
        message_teacher = results.teacher
        message_serial = results.serial
        message_week = results.week
        message_name = results.name
        return message_name, message_teacher,message_serial,message_week

    def serach_bytime(self,name):
        session = DBSession()
        results = session.query(classslot).filter(classslot.serial == namee).one()
        message_place = results.place
        message_teacher = results.teacher
        message_week = results.week
        message_name = results.name
        return message_name, message_place,message_teacher,message_week

    def update_name(self,data, new_data):
        session = DBSession()
        result = session.query(classslot).filter_by(name = data).first()
        result.name = new_data
        session.commit()
        session.close()

    def update_place(self,data, new_data):
        session = DBSession()
        result = session.query(classslot).filter_by(place = data).first()
        result.place = new_data
        session.commit()
        session.close()

    def update_teacher(self,data,new_data):
        session = DBSession()
        result = session.query(classslot).filter_by(teacher = data).first()
        result.teacher = new_data
        session.commit()
        session.close()

    def update_serial(self,data, new_data):
        session = DBSession()
        result = session.query(classslot).filter_by(serial = data).first()
        result.serial = new_data
        session.commit()
        session.close()

    def update_week(self,data, new_data):
        session = DBSession()
        result = session.query(classslot).filter_by(week = data).first()
        result.week = new_data
        session.commit()
        session.close()

    def delete_name(self,data):
        session = DBSession()
        session.query(classslot).filter((classslot.name == data)).delete()
        session.commit()
        session.close()

    def delete_place(self,data):
        session = DBSession()
        session.query(classslot).filter((classslot.place == data)).delete()
        session.commit()
        session.close()

    def delete_teacher(self,data):
        session = DBSession()
        session.query(classslot).filter((classslot.teacher == data)).delete()
        session.commit()
        session.close()

    def delete_serial(self,data):
        session = DBSession()
        session.query(classslot).filter((classslot.serial == data)).delete()
        session.commit()
        session.close()

    def delete_week(self,data):
        session = DBSession()
        session.query(classslot).filter((classslot.week == data)).delete()
        session.commit()
        session.close()

    def delete_time(self,serial,week):
        session = DBSession()
        session.query(classslot).filter((classslot.week == week and classslot.serial == serial)).delete()
        session.commit()
        session.close()

    def multi_search_name(self,data):
        session = DBSession()
        results = session.query(classslot).filter(classslot.name.like('%'+data+'%')).all()
        abc = []
        for r in results:
            sub = []
            sub.append(r.name)
            sub.append(r.teacher)
            sub.append(r.place)
            sub.append(r.serial)
            sub.append(r.week)
            abc.append(sub)
        if abc == []:
            return 'There is no such data'
        else:
            return abc

    def complex_search_name(self,data):
        a = function()
        session = DBSession()
        ret1 = session.query(classslot).filter(classslot.name.like('%'+data+'%')).all()
        abc = []
        for ret in ret1:
            abc.append(ret.name)
            abc.append(ret.teacher)
            abc.append(ret.week)
            abc.append(ret.place)
            abc.append(ret.serial)
        if abc == []:
            return 'There is no such data'
        else:
            return a.eliminate(abc)

    def complex_search_time(self,serial,week):
        a = function()
        session = DBSession()
        results = session.query(classslot).filter(classslot.serial == serial, classslot.week == week).all()
        abc = []
        for result in results:
            abc.append(result.name)
        if abc ==[]:
            return "There is no such data"
        else:
            return a.eliminate(abc)

    def eliminate(self,check):
        null = []
        for i in check:
            if i not in null:
                null.append(i)
        return null

    def shorten(self,data):
        data = ''.join(data.split())
        return data.lower()

    def comprehensive_search(self,serial,week,name):
        session = DBSession()
        results = session.query(classslot).filter(classslot.serial == serial, classslot.week == week, classslot.name ==name).all()
        abc = []
        for result in results:
            b = []
            b.append(result.name)
            b.append(result.teacher)
            b.append(result.place)
            b.append(result.serial)
            b.append(result.week)
            abc.append(b)
        if abc ==[]:
            return "There is no such data"
        else:
            return abc

    def select_choice(self,group1,group2,group3,group4,group5,group6,tok):
        allchoice = []
        f = function()
        result1 = f.multi_search_name(group1)
        result2 = f.multi_search_name(group2)
        result3 = f.multi_search_name(group3)
        result4 = f.multi_search_name(group4)
        result5 = f.multi_search_name(group5)
        result6 = f.multi_search_name(group6)
        tokk = f.multi_search_name(tok)
        allchoice.append(result1)
        allchoice.append(result2)
        allchoice.append(result3)
        allchoice.append(result4)
        allchoice.append(result5)
        allchoice.append(result6)
        allchoice.append(tokk)
        return allchoice

    def specify(self,data,serial,week):
        """
        :param data: A Student's full choices of classes
        :param serial: The Time Slot
        :param week: Which work data
        :return: a particular class on the screen
        """
        for i in range(0,7):
            sub = data[i]
            for j in range(0,len(sub)):
                subsub = sub[j]
                if subsub[3]==serial and subsub[4]==week:
                    subsub = subsub[:3]
                    return subsub





a = function()
lalala = a.select_choice('mandarin1','english sl','math hl1','physics hl','computer science hl','economics sl','tok1')

@app.route('/')
def index():
    a = function()
    result10 = a.specify(lalala,1,1)
    result11 = a.specify(lalala,2,1)
    result12 = a.specify(lalala,3,1)
    result13 = a.specify(lalala,4,1)
    result15 = a.specify(lalala,6,1)
    result16 = a.specify(lalala,7,1)
    result17 = a.specify(lalala,8,1)
    result18 = a.specify(lalala,9,1)
    result20 = a.specify(lalala,1,2)
    result21 = a.specify(lalala,2,2)
    result22 = a.specify(lalala,3,2)
    result23 = a.specify(lalala,4,2)
    result25 = a.specify(lalala,6,2)
    result26 = a.specify(lalala,7,2)
    result27 = a.specify(lalala,8,2)
    result28 = a.specify(lalala,9,2)
    result30 = a.specify(lalala,1,3)
    result31 = a.specify(lalala,2,3)
    result32 = a.specify(lalala,3,3)
    result33 = a.specify(lalala,4,3)
    result35 = a.specify(lalala,6,3)
    result36 = a.specify(lalala,7,3)
    result37 = a.specify(lalala,8,3)
    result38 = a.specify(lalala,9,3)
    result40 = a.specify(lalala,1,4)
    result41 = a.specify(lalala,2,4)
    result42 = a.specify(lalala,4,4)
    result43 = a.specify(lalala,5,4)
    result45 = a.specify(lalala,6,4)
    result46 = a.specify(lalala,7,4)
    result47 = a.specify(lalala,8,4)
    result48 = a.specify(lalala,9,4)
    result50 = a.specify(lalala,1,5)
    result51 = a.specify(lalala,2,5)
    result52 = a.specify(lalala,4,5)
    result53 = a.specify(lalala,5,5)
    result55 = a.specify(lalala,6,5)
    result56 = a.specify(lalala,7,5)
    result57 = a.specify(lalala,8,5)
    result58 = a.specify(lalala,9,5)

    return render_template('timetable.html',mon10 = result10, mon11 = result11,mon12=result12,mon13=result13,mon15=result15,mon16=result16,mon17=result17,mon18=result18,mon20=result20,
                           mon21=result21,mon22=result22,mon23=result23,mon25=result25,mon26=result26,mon27=result27,mon28=result28,
                           mon30=result30,mon31=result31,mon32=result32,mon33=result33,mon35=result35,mon36=result36,mon37=result37,mon38=result38,
                           mon40=result40,mon41=result41,mon43=result42,mon44=result43,mon45=result45,mon46=result46,mon47=result47,mon48=result48,
                           mon50=result50,mon51=result51,mon53=result52,mon54=result53,mon55=result55,mon56=result56,mon57=result57,mon58=result58)

if __name__=='__main__':
    app.run(debug=True)








"""

data = classslot(name='avd', place = 100, teacher = 'daizhibo', serial = 5, week = 5)

a = function()
#print(a.serach_byname('Math SL'))
#a.update_name('bylat','cyka')
#print(a.multi_search_name("Mandarin"))
#print(a.complex_search_name('econ'))
#print(a.complex_search_time(2,3))
#print(a.complex_search_name('Man')) # Group1
#print(a.complex_search_name('Math')) # Group2
print(a.complex_search_name('English'))

form = cgi.FieldStorage()
data1 = form.getvalue('username')
data2 = form.getvalue('psw')


@app.route('/')
def index():
    a = function()
    result = a.comprehensive_search(1,1,'Mandarin1')
    return render_template('timetable.html', mon1 = result)



@app.route('/abc')
def query(name):
    classslot1 = classslot.query.filter(classslot.name == 'Mandarin1').first()
    print(classslot1.name)
    print(classslot1.place)
    return 'Hello World'


@app.route('/bca')
def deletee():
    classslot2 = classslot.query.filter(classslot.teacher == 'davidd').first()
    db.session.delete(classslot2)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug= True)


def hello_world():
    result = classslot.query.filter(classslot.name == 'math').first()
    db.session.delete(result)
    db.session.commit()

"""
