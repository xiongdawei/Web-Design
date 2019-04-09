from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template
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
    name = Column(String(200), primary_key=True,nullable= False, index = True)
    place = Column(Integer,primary_key=True ,nullable= False, index = True)
    teacher = Column(String(200),primary_key=True ,nullable = False, index = True)
    serial = Column(Integer, primary_key= True ,nullable = False, index = True )
    week = Column(Integer,primary_key= True, nullable = False, index = True)

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

    def serach_byserial(self,namee):
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

    def multi_search_name(self,data):
        session = DBSession()
        results = session.query(classslot).filter_by(name = data).all()
        abc = []
        for r in results:
            abc.append(r.place)
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
            abc.append(result.name)
            abc.append(result.teacher)
            abc.append(result.place)
            abc.append(result.serial)
            abc.append(result.week)
        if abc ==[]:
            return "There is no such data"
        else:
            return abc

    def in_college(self,data1):
        """
        This function intents to help me identify whether the input value is in the current available courses.
        :param data1: Data1 is the subject you wish to specifiy
        :param data2: Data2 is the user input which may not be qualified
        :return: The final result which must be accurate in order to eliminate unexpected error.
        """
        while True:
            a = function()
            b = []
            possible_course = a.complex_search_name(data1)
            message = 'Please tell us which course your take: '
            for data in possible_course:
                data = str(data) + ' '
                message += data
            print(message)
            ans = a.shorten(str(input('>>>'))).lower()
            for i in possible_course:
                b.append(a.shorten(i))
            if ans in b:
                return ans
            else:
                print 'There is no such data, please try again'
                continue

#data = classslot(name='avd', place = 100, teacher = 'daizhibo', serial = 5, week = 5)

a = function()
#print(a.serach_byname('Math SL'))
#a.update_name('bylat','cyka')
#print(a.multi_search_name("Mandarin"))
#print(a.complex_search_name('econ'))
#print(a.complex_search_time(2,3))
#print(a.complex_search_name('Man')) # Group1
#print(a.complex_search_name('Math')) # Group2
#print(a.complex_search_name('English'))

@app.route('/')
def index():
    a = function()
    result = a.comprehensive_search(1,1,'Mandarin1')
    return render_template('timetable.html', mon1 = result)























"""
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

