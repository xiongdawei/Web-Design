from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, url_for, redirect, session, make_response
from flask_script import Manager
from Function import function
import os
import random

app = Flask(__name__)
app.config['SECRET_KET'] = os.urandom(24)
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



#a = function()
#lalala = a.select_choice('Mandarin2','English HL1','Math HL3','Computer Science HL','Visual Art SL','Business SL','TOK1')
"""
@app.route('/', methods=["POST","GET"])
def choose():
    app.config['SECRET_KET'] = os.urandom(24)
    if request.method == 'POST':
        a = function()
        namee = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        group1 = request.form.get('group1')
        group2 = request.form.get('group2')
        group3 = request.form.get('group3')
        group4 = request.form.get('group4')
        group5 = request.form.get('group5')
        group6 = request.form.get('group6')
        pe = request.form.get('pe')
        tok = request.form.get('TOK')
        classs = request.form.get('class')
        data = user_data(Name=namee,Email=email,Password=password,Group1=group1,Group2=group2,Group3=group3,Group4=group4,Group5=group5,Group6=group6,PE=pe,TOK=tok,Class=classs)
        a.add_user_data(data)
        response = make_response('')
        response.set_cookie('Name',namee)
        return redirect('/result')
    else:
        return render_template('college_data002.html')



@app.route('/result')
def index():
    a = function()
    user_id = request.cookies.get('Name')
    lalala = a.select_choice_new(user_id)
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
                           mon40=result40,mon41=result41,mon43=result42,mon44=result43,mon45=result45,mon46=result46,mon47=result47,
                           mon50=result50,mon51=result51,mon53=result52,mon54=result53,mon55=result55,mon56=result56,mon57=result57,mon58=result58)


"""


@app.route('/')
def index():
    response = make_response('')
    response.set_cookie('Name', "David_XX")
    return redirect('/result')

@app.route('/result')
def rere():
    name = request.cookies.get('Name')
    name = str(name)
    a = function()
    listt = a.
    return listt







if __name__=='__main__':
    app.run(debug=True)

