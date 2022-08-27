from flask import Flask, render_template, request 
app = Flask(__name__)
import mysql.connector

Qid = 0

name=None
email=None
dob=None
phone=None

@app.route('/', methods=['GET','POST']) # To render Homepage
def home():
    return render_template('mywebsite.html')


@app.route('/log', methods=['GET','POST']) # To render Homepage
def log():
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def abqc():
    userid=request.form['uname']
    password = request.form['pass']    

    conn = mysql.connector.connect(host="localhost" , database = 'jaivik',user="root", password="jaivik@12345",use_pure=True)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quiz WHERE userid = %s AND password = %s', (userid, password))
    check = cursor.fetchall()

    if check:
        return render_template('AdminHomePage.html')
    else:
        # flash ='Invalid Credentials. Please try again.'
        return render_template('login.html')
   


@app.route('/reg',methods=['GET','POST'])
def abcd():
    return render_template('reg.html')


@app.route('/reg1',methods=['GET','POST'])
def reg():
    global name,email,dob,phone

    name=request.form['name']
    email=request.form['email']
    dob = request.form['date']
    phone = request.form['phone']
        
    conn = mysql.connector.connect(host="localhost" , database = 'jaivik',user="root", password="jaivik@12345",use_pure=True)
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM quiz")
    data = cursor.fetchall()
    length = len(data)
    i=0
    while i<length:
        if(str(email) == str((data[i])[0])):
            return str(email+" "+"already exist")
        i = i+1
    return render_template('userid.html')
    # return "hello"
 

@app.route('/logged',methods=['GET','POST'])
def abzc():
    
    global name,email,dob,phone
    
    uname=request.form['uname']
    password = request.form['pass']
    type = request.form['type']
    
    
    s = "INSERT INTO quiz(name,email,DOB,phone,userid,password,type)" "VALUES (%s, %s, %s, %s, %s,%s, %s)" 
    a = (name,email,dob,phone,uname,password,type)
    conn = mysql.connector.connect(host="localhost" , database = 'jaivik',user="root", password="jaivik@12345",use_pure=True)
    cursor = conn.cursor()
    cursor.execute(s,a)
    conn.commit()
    return render_template('login.html')
    # return uname+password+type



@app.route('/insertQue',methods=['GET','POST'])
def openQuePage():
    return render_template('addQuestion.html')

@app.route('/insertQueData',methods=['GET','POST'])
def queData():
    global Qid

    que = request.form['que']
    op1 = request.form['option1']
    op2 = request.form['option2']
    op3 = request.form['option3']
    op4 = request.form['option4']
    radio = request.form['ans']

    Qid = Qid+1

    mydb = mysql.connector.connect(host="localhost", database='jaivik', user="root", password="jaivik@12345", use_pure=True)
    cur = mydb.cursor()
    s="INSERT INTO qanda(Qid,Question,Option1,Option2,Option3,Option4,CorrectID) ""VALUES (%s, %s, %s, %s, %s, %s, %s) "
    d= (str(Qid), que, op1, op2, op3, op4,radio)
    cur.execute(s,d)
    mydb.commit()
    cur.close()
    mydb.close()
    

    return render_template('addQuestion.html')

@app.route('/ab',methods=['GET','POST'])
def dbData():
   
    return render_template('index.html')

    # mydb = mysql.connector.connect(host="localhost", database='jaivik', user="root", password="jaivik@12345", use_pure=True)
    # cur = mydb.cursor()
    # cur.execute("SELECT * FROM qanda")
    # data = cur.fetchall()
    # i = 0
    # j = 0
    # count = 1
    # listlen = len(data)
    # dict = {}
    # # mainDict = {}
    # datalist = []

    # while i<listlen:
    #     dict.update({'numb': count})
    #     dict.update({'question': (data[i])[j+1]})
    #     dict.update({'option1':(data[i])[j+2]})
    #     dict.update({'option2':(data[i])[j+3]})
    #     dict.update({'option3':(data[i])[j+4]})
    #     dict.update({'option4':(data[i])[j+5]})

    #     if (data[i])[j+6] == 'option1':
    #         dict.update({'answer':(data[i])[j+2]})
    #     elif (data[i])[j+6] == 'option2':
    #         dict.update({'answer':(data[i])[j+3]})
    #     elif (data[i])[j+6] == 'option3':
    #         dict.update({'answer':(data[i])[j+4]})
    #     elif (data[i])[j+6] == 'option4':
    #         dict.update({'answer':(data[i])[j+5]})

    #     datalist.append(dict.copy()) 
    #     # mainDict.update({str(i+1):dict.copy()})
    #     dict.clear()       
    #     count = count + 1
    #     i=i+1
    
    # cur.close()
    # mydb.close()
    # return render_template('index.html')




if __name__ == '__main__':
    # app.secret_key="secreat123"
    app.run(host="0.0.0.0",port=85)
    
    # return render_template('login.html')
     # sql = '''SELECT * from jaivik'''
    # cursor.execute(sql)
    # cursor.execute(s,a)