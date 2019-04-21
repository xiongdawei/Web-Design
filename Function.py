from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, url_for, redirect
from flask_script import Manager



app = Flask(__name__)
Base = declarative_base()
engine1 = create_engine('mysql+pymysql://root:cykablyat@localhost:3306/classtime')
DBSession = sessionmaker(bind = engine1)

engine2 = create_engine('mysql+pymysql://root:cykablyat@localhost:3306/User_Data')
DBSession_A = sessionmaker(bind = engine2)

manager = Manager(app)

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

    def get_user_datacurrent(self,name):
        session = DBSession_A()
        results = session.query(user_data).filter(user_data.Name == name).first()
        group1 = results.Group1
        group2 = results.Group2
        group3 = results.Group3
        group4 = results.Group4
        group5 = results.Group5
        group6 = results.Group6
        tok = results.TOK
        final = []
        final.append(group1)
        final.append(group2)
        final.append(group3)
        final.append(group4)
        final.append(group5)
        final.append(group6)
        final.append(tok)
        return final



    def serach_byname(self,namee):
        session = DBSession()
        results = session.query(classslot).filter(classslot.name == namee)
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
        results = session.query(classslot).filter(classslot.place == namee).all()
        message_teacher = results.teacher
        message_serial = results.serial
        message_week = results.week
        message_name = results.name
        return message_name, message_teacher,message_serial,message_week

    def serach_bytime(self,name):
        session = DBSession()
        results = session.query(classslot).filter(classslot.serial == name).one()
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
        results = session.query(classslot).filter(classslot.name== data).all()
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
            return None
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

    def select_choice_new(self,name):
        allchoice = []
        f = function()
        listt = f.get_user_datacurrent(name)
        for i in listt:
            result = f.multi_search_name(i)
            allchoice.append(result)
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
print(a.get_user_datacurrent('CC'))