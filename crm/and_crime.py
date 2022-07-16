from flask import Flask,request, jsonify
from DBconnection import Db

app = Flask(__name__)

@app.route("/and_user_reg", methods=['post'])
def and_user_reg():
    name=request.form['name']
    gender=request.form['gender']
    place=request.form['place']
    pin=request.form['pin']
    email=request.form['email']
    phone=request.form['phone']
    pswd=request.form['pswd']
    qry="insert into login(username,password,type) values('"+email+"','"+pswd+"','user')"
    c=Db()
    lid=c.insert(qry)
    qry="insert into user values('null', '"+name+"', '"+gender+"', '"+place+"', '"+pin+"', '"+email+"', '"+phone+"', '"+str(lid)+"')"
    c=Db()
    res=c.insert(qry)
    if res>0:
        return jsonify(status="ok")
    else:
        return jsonify(status="no")

@app.route("/add_complaint",       methods=['post'])
def add_complaint():
    lid=request.form['lid']
    comp=request.form['comp']

    c=Db()
    qry="insert into complaint values(null,'"+comp+"',curdate(),'"+lid+"','','pending')"
    c=Db()
    res=c.insert(qry)
    if res>0:
        return jsonify(status="ok")
    else:
        return jsonify(status="no")


###########
@app.route("/in_message2",methods=['post'])
def add_complhhaint():
    fid=request.form['fid']
    toid=request.form['toid']
    msg=request.form['msg']

    qry="INSERT INTO chat(`from_id`,`to_id`,`msg`,`date`,`time`) VALUES('"+fid+"','"+toid+"','"+msg+"',curdate(),curtime())"
    print(qry)
    c=Db()
    res=c.insert(qry)
    if res>0:
        return jsonify(status="ok")
    else:
        return jsonify(status="no")

@app.route('/view_message2', methods=['POST'])
def msg():
    fid = request.form["fid"]
    toid = request.form["toid"]
    # name = request.form["name"]
    lmid = request.form['lastmsgid'];

    query="select from_id,msg,date,chat_id from chat where chat_id>'"+lmid+"' AND ((from_id='"+toid+"' and  to_id='"+fid+"') or (from_id='"+fid+"' and to_id='"+toid+"')  )  order by chat_id asc"
    print(query)
    c=Db()
    m = c.select(query)
    if m is not None:
        return jsonify(status='ok', res1=m)

    else:
        return jsonify(status='not found')

#######


@app.route("/and_user_login",methods=['post'])
def and_user_login():
    username=request.form['username']
    pswd=request.form['pswd']
    qry="select * from login where username='"+username+"' and password='"+pswd+"'"
    c=Db()
    res=c.select_one(qry)
    if res is not None:
       return jsonify(status="ok",lid=res["login_id"])
    else:
        return jsonify(status="no")

@app.route("/change_password",methods=['post'])
def change_password():
    lid=request.form['lid']
    cpass=request.form['cpass']
    npass=request.form['npass']
    qry="select * from login where login_id='"+lid+"' and password='"+cpass+"'"
    c=Db()
    res=c.select_one(qry)
    if res is not None:
        c.update("update login set password='"+npass+"' where login_id='"+lid+"'")
        return jsonify(status="ok")
    else:
        return jsonify(status="no")

@app.route("/and_user_profile",methods=['post'])
def and_user_profile():
    login_id=request.form['login_id']
    qry="select * from USER where login_id='"+login_id+"'"
    c=Db()
    res=c.select_one(qry)
    if res is None:
        return jsonify(status="no")
    else:
        return jsonify(status="ok",name=res['name'],gender=res['gender'],place=res['place'],pin=res['pin'],email=res['email'],phone=res['phone'])

@app.route("/and_view_complaint",methods=['post'])
def and_view_complaint():
    user_id=request.form['lid']
    qry="select * from complaint where u_id='"+user_id+"' order by complaint_id desc"
    c=Db()
    res=c.select(qry)
    if res is None:
        return jsonify(status="no")
    else:
        return jsonify(status="ok",data=res)



@app.route("/and_view_criminals",methods=['post'])
def and_view_criminals():
    qry="select * from criminal"
    c=Db()
    res=c.select(qry)
    if res is None:
        return jsonify(status="no")
    else:
        return jsonify(status="ok",data=res)


@app.route("/and_view_police",methods=['post'])
def and_view_police():
    qry="select * from police_station order by name"
    c=Db()
    res=c.select(qry)
    if res is None:
        return jsonify(status="no")
    else:
        return jsonify(status="ok",data=res)

@app.route("/view_lookout",methods=['post'])
def view_lookout():
    qry="SELECT criminal.*,`crime`.`crime_name` FROM criminal,lookout,`crime` WHERE lookout.cr_id=criminal.cr_id  AND `crime`.`c_id`=`criminal`.`crime_id`ORDER BY lookout_id DESC"
    c=Db()
    res=c.select(qry)
    if res is None:
        return jsonify(status="no")
    else:
        return jsonify(status="ok",data=res)



@app.route("/and_view_notification",methods=['post'])
def and_view_notification():
    qry="select * from notification where type='user' order by notification_id desc"
    c=Db()
    res=c.select(qry)
    if res is None:
        return jsonify(status="no")
    else:
        return jsonify(status="ok",data=res)

@app.route("/and_view_missingperson",methods=['post'])
def and_view_missingperson():
    qry="select * from missingperson"
    c=Db()
    res=c.select(qry)
    if res is None:
        return jsonify(status="no")
    else:
        return jsonify(status="ok",data=res)

@app.route('/and_missingpersonreporting',methods=['post'])
def and_missingpersonreporting():
    mid=request.form['mid']
    uid=request.form['lid']
    lat=request.form['latti']
    long=request.form['longi']
    place=request.form['place']
    info=request.form['info']
    qry="insert into report values(null,'"+mid+"','"+uid+"','"+lat+"','"+long+"','"+place+"','"+info+"',curdate())"
    c=Db()
    res=c.insert(qry)
    if res > 0:
        return jsonify(status="ok")
    else:
        return jsonify(status="no")





if __name__ == '__main__':
    app.run(host='0.0.0.0')
