import random

from flask import Flask,render_template,request,redirect,jsonify
from flask.globals import session
from dbcontext import conn
from werkzeug.utils import secure_filename
import os
import time
app = Flask(__name__)
app.secret_key="1234"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def log():
    return render_template('login.html')

@app.route('/logs',methods=['post'])
def logs():
    us=request.form['username']
    ps=request.form['pass']
    db=conn()
    qry="select * from login where username='"+us+"' and password='"+ps+"'"
    res=db.selectone(qry)
    if res!=None:
        user=res[3]
        session['log_id']=res[0]
        if user=='admin':
            return render_template('Admin/Home.html')
        elif user=='police':
            rr=db.selectone("select p_id from police_station where email='"+us+"'")
            if rr is not None:
                pid=rr[0]
                session['pol_id']=pid
                return render_template('Police/Home.html')
    else:
        return '''<script>
        alert("Incorrect password or username")
        window.location='/'
        </script>'''

@app.route('/adm_home')
def adm_home():
    return render_template('Admin/Home.html')

@app.route('/adm_addpolicestation')
def adm_addpolicestation():
    return render_template('Admin/AddPoliceStation.html')

@app.route('/adm_add',methods=['post'])
def adm_add():
    db=conn()
    name=request.form['name']
    place=request.form['place']
    post=request.form['post']
    pin=request.form['pin']
    city=request.form['city']
    district=request.form['district']
    email=request.form['mail']
    phone=request.form['phone']
    fax=request.form['fax']
    file = request.files['photo']
    pswd=str(random.randint(0000,9999))
    qq="select * from login where username='"+email+"'"
    rr=db.selectone(qq)
    if rr is None:
        if file and allowed_file(file.filename):
            timestr = time.strftime("%Y%m%d-%H%M%S")
            filename = timestr + secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        qry1 = "insert into login values(null,'" + email + "','"+pswd+"','police')"
        db.nonreturn(qry1)
        qry="insert into police_station values(null,'"+name+"','"+place+"','"+post+"','"+pin+"','"+city+"','"+district+"','"+filename+"','"+email+"','"+phone+"','"+fax+"')"
        db.nonreturn(qry)
        return redirect('/adm_addpolicestation')
    else:
        return'''<script>
        alert("Email already exists")
        window.location='/adm_addpolicestation'
        </script>'''


@app.route('/plc_delete_police/<id>/<email>')
def plc_delete_police(id,email):
    db=conn()
    qry="delete from police_station where p_id='"+id+"'"
    res=db.nonreturn(qry)
    qq="delete from login where username='"+email+"'"
    db.nonreturn(qq)
    return redirect('/adm_viewpolicestation')

@app.route('/plc_edit_police/<id>')
def plc_edit_police(id):
    db=conn()
    qry="select * from police_station where p_id='"+id+"'"
    res=db.selectone(qry)
    return render_template('Admin/edit_police.html',data=res)

@app.route('/adm_editpolice',methods=['post'])
def adm_editpolice():
    db=conn()
    hid=request.form['hid']
    name=request.form['name']
    place=request.form['place']
    post=request.form['post']
    pin=request.form['pin']
    print(pin)
    city=request.form['city']
    district=request.form['district']
    email=request.form['mail']
    phone=request.form['phone']
    fax=request.form['fax']
    file = request.files['photo']
    if file and allowed_file(file.filename):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = timestr + secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        qry="update police_station set name='"+name+"',place='"+place+"',post='"+post+"',pin='"+pin+"',city='"+city+"',district='"+district+"',email='"+email+"',phone='"+phone+"',fax='"+fax+"',photo='"+filename+"' where p_id='"+hid+"'"
        db.nonreturn(qry)
    else:
        qry = "update police_station set name='" + name + "',place='" + place + "',post='" + post + "',pin='" + pin + "',city='" + city + "',district='" + district + "',email='" + email + "',phone='" + phone + "',fax='" + fax + "' where p_id='" + hid + "'"
        db.nonreturn(qry)


    return redirect('/adm_viewpolicestation')

@app.route('/adm_viewpolicestation')
def adm_viewpolicestation():
    db=conn()
    qry="Select police_station.p_id,police_station.name,police_station.place,police_station.post,police_station.pin,police_station.city,police_station.district,police_station.photo,police_station.email,police_station.phone,police_station.fax from police_station"
    res=db.selectall(qry)
    return render_template('Admin/ViewPoliceStation.html',res=res)


@app.route('/adm_viewcomplaints')
def adm_viewcomplaints():
    db = conn()
    qry="select complaint.complaint_id,complaint.complaint_date,user.name,complaint.complaint,complaint.reply from complaint,user where complaint.u_id=user.login_id and status='reply_sent'"
    res = db.selectall(qry)
    print(res)
    return render_template('Admin/ViewComplaints.html',res=res)

@app.route('/adm_complaintreply/<id>')
def adm_complaintreply(id):
    db=conn()
    qry="select * from complaint where complaint_id='"+id+"'"
    res=db.selectone(qry)
    return render_template('Admin/ComplaintReply.html',data=res)


@app.route('/adm_sendnotification')
def adm_sendnotification():
    return render_template('Admin/SendNotification.html')

@app.route('/adm_sendnotification2',methods=['post'])
def adm_sendnotification2():
    db = conn()
    subject=request.form['textfield']
    content=request.form['textfield2']
    type=request.form['select']
    qry="insert into notification values(null,'"+subject+"','"+content+"','2019-12-12','"+type+"')"
    db.nonreturn(qry)

    return redirect('/adm_sendnotification')

@app.route('/adm_viewnotification')
def adm_viewnotification():
    db=conn()
    qry="select notification.notification_id,notification.subject,notification.content,notification.notification_date,notification.type from notification"
    res=db.selectall(qry)
    return render_template('Admin/ViewNotification.html',res=res)

@app.route('/plc_delete_not/<id>')
def plc_delete_not(id):
    db=conn()
    qry="delete from notification where notification_id='"+id+"'"
    res=db.nonreturn(qry)
    return redirect('/adm_viewnotification')







@app.route('/plc_home')
def plc_home():
    return render_template('Police/Home.html')

@app.route('/plc_addmissingman')
def plc_addmissingman():
    return render_template('Police/AddMissingMan.html')

@app.route('/plc_addmiss',methods=['post'])
def plc_addmissingman2():
    db=conn()
    name=request.form['name']
    gender=request.form['gender']
    dob=request.form['dob']
    file = request.files['photo']
    if file and allowed_file(file.filename):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = timestr + secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    houseno=request.form['houseno']
    street=request.form['street']
    city=request.form['city']
    district=request.form['district']
    state=request.form['state']
    height=request.form['height']
    weight=request.form['weight']
    skintone=request.form['skintone']
    identificationmarks=request.form['identificationmarks']
    missingplace=request.form['missingplace']
    lastseen=request.form['lastseen']
    dress=request.form['dress']
    contact=request.form['contact']
    qry="insert into missingperson values(null,'"+name+"','"+gender+"','"+dob+"','"+filename+"','"+houseno+"','"+street+"','"+city+"','"+district+"','"+state+"','"+height+"','"+weight+"','"+skintone+"','"+identificationmarks+"','"+missingplace+"','"+lastseen+"','"+dress+"','"+contact+"','"+str(session['log_id'])+"')"
    db.nonreturn(qry)
    return redirect('/plc_addmissingman')

@app.route('/adm_viewmanmissing')
def adm_viewmanmissing():
    db=conn()
    qry="select * from missingperson"
    res=db.selectall(qry)
    return render_template('Admin/ViewManMissing.html',res=res)

@app.route('/plc_viewmanmissingreport')
def plc_viewmanmissingreport():
    db = conn()
    qry = "select report.report_id,report.manmissing_id,report.user_id,report.latitude,report.longitude,report.place,report.information from report,missingperson,user  where report.manmissing_id=missingperson.missing_id and report.user_id=user.user_id"
    res=db.selectall(qry)
    return render_template('Police/ViewManMissingReport.html',res=res)

@app.route('/plc_viewmanmissing')
def plc_viewmanmissing():
    db = conn()
    qry = "select * from missingperson"
    res = db.selectall(qry)
    return render_template('Police/ViewMissingMan.html',res=res)

@app.route('/plc_delete_missing/<id>')
def plc_delete_missing(id):
    db=conn()
    qry="delete from missingperson where missing_id='"+id+"'"
    res=db.nonreturn(qry)
    return plc_viewmanmissing()

@app.route('/plc_edit_missing/<id>')
def plc_edit_missing(id):
    db=conn()
    print(id)
    qry="select * from missingperson where missing_id='"+id+"'"
    res=db.selectone(qry)
    return render_template('Police/edit_missing.html',data=res)

@app.route('/plc_edit',methods=['post'])
def plc_edit():
    db=conn()
    hid=request.form['hid']
    name=request.form['name']
    gender=request.form['gender']
    dob=request.form['dob']
    file = request.files['photo']
    houseno = request.form['houseno']
    street = request.form['street']
    city = request.form['city']
    district = request.form['district']
    state = request.form['state']
    height = request.form['height']
    weight = request.form['weight']
    skintone = request.form['skintone']
    identificationmarks = request.form['identificationmarks']
    missingplace = request.form['missingplace']
    lastseen = request.form['lastseen']
    dress = request.form['dress']
    contact = request.form['contact']
    if file and allowed_file(file.filename):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = timestr + secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        qry="update missingperson set name='"+name+"',gender='"+gender+"',dob='"+dob+"',photo='"+filename+"',house_no='"+houseno+"',street='"+street+"',city='"+city+"',district='"+district+"',state='"+state+"',height='"+height+"',weight='"+weight+"',skin_tone='"+skintone+"',identification_marks='"+identificationmarks+"',missing_place='"+missingplace+"',last_seen='"+lastseen+"',dress='"+dress+"',contact='"+contact+"' where missing_id='"+hid+"'"
        db.nonreturn(qry)
    else:
        qry = "update missingperson set name='" + name + "',gender='" + gender + "',dob='" + dob + "',house_no='" + houseno + "',street='" + street + "',city='" + city + "',district='" + district + "',state='" + state + "',height='" + height + "',weight='" + weight + "',skin_tone='" + skintone + "',identification_marks='" + identificationmarks + "',missing_place='" + missingplace + "',last_seen='" + lastseen + "',dress='" + dress + "',contact='" + contact + "' where missing_id='" + hid + "'"
        db.nonreturn(qry)
    return redirect('/plc_viewmanmissing')


@app.route('/plc_complaintreply')
def plc_complaintreply():

    return render_template('Police/ComplaintReply.html')

@app.route('/plc_complaintreply2',methods=['post'])
def plc_complaintreply2():
    db=conn()
    hid=request.form['hid']
    reply=request.form['textarea']
    qry="update complaint set reply='"+reply+"',status='reply_sent' where complaint_id='"+hid+"' "
    db.nonreturn(qry)
    return redirect('/plc_viewcomplaints')

@app.route('/plc_viewcomplaints')
def plc_viewcomplaints():
    db = conn()
    qry = "select complaint.complaint_id,complaint.complaint_date,user.user_id,complaint.complaint,complaint.status from complaint,user where complaint.u_id=user.login_id and status='pending'"
    res = db.selectall(qry)
    return render_template('Police/ViewComplaints.html',res=res)


@app.route('/plc_viewnotification')
def plc_viewnotification():
    db = conn()
    qry="select * from notification where type='police'"
    res=db.selectall(qry)
    return render_template('Police/viewnotification.html',res=res)



@app.route('/police_add_criminallist')
def police_add_criminallist():
    db=conn()
    qry="SELECT * FROM `crime`"
    res1=db.selectall(qry)
    return render_template("police/criminallist_reg.html", data1=res1)


@app.route('/police_add_criminallist_post',methods=['post'])
def police_add_criminallis_post():
    db=conn()
    name=request.form['name']
    dob = request.form['dob']
    gender = request.form['radio']
    place = request.form['place']
    district = request.form['district']
    identification = request.form['identi']
    crime=request.form['crime']
    file = request.files['photos']
    father=request.form['father']
    mother=request.form['mother']
    blood=request.form['blood']
    house=request.form['house']
    street=request.form['street']
    post=request.form['post']
    pin=request.form['pin']
    if file and allowed_file(file.filename):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = timestr + secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    qry="INSERT INTO `criminal` VALUES(NULL,'"+name+"','"+gender+"','"+dob+"','"+blood+"','"+identification+"','"+house+"','"+street+"','"+place+"','"+post+"','"+pin+"','"+district+"','"+father+"','"+mother+"','"+crime+"','"+filename+"','"+str(session['log_id'])+"')"
    db.nonreturn(qry)
    return police_add_criminallist()




@app.route('/view_criminallist')
def view_criminallist():
    db=conn()
    qry="SELECT `criminal`.*,`crime`.`crime_name` FROM `criminal`,`crime` WHERE `criminal`.`crime_id`=`crime`.`c_id` AND `criminal`.`pid`='"+str( session['log_id'])+"'"
    res=db.selectall(qry)
    return render_template("police/view_criminallist.html", data=res)

@app.route('/edit_criminallist/<id>')
def edit_criminallist(id):
    db=conn()
    qry="SELECT `criminal`.*,`crime`.`crime_name` FROM `criminal`,`crime` WHERE `criminal`.`crime_id`=`crime`.`c_id` AND `criminal`.`pid`='"+str( session['log_id'])+"'AND `cr_id`='"+id+"'"
    res=db.selectone(qry)
    qry = "SELECT * FROM `crime`"
    res1 = db.selectall(qry)
    return render_template("police/criminallist_edit.html", data=res,data1=res1)



@app.route('/crimelist_update',methods=['POST'])
def crimelist_update():
    c=conn()
    id=request.form["hid"]
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['radio']
    place = request.form['place']
    district = request.form['district']
    identification = request.form['identi']
    crime = request.form['crime']
    file = request.files['photos']
    father = request.form['father']
    mother = request.form['mother']
    blood = request.form['blood']
    house = request.form['house']
    street = request.form['street']
    post = request.form['post']
    pin = request.form['pin']
    if file and allowed_file(file.filename):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        filename = timestr + secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        qry = "UPDATE `criminal` SET `name`='"+name+"',`gender`='"+gender+"',`dob`='"+dob+"',`blood_group`='"+blood+"',`identification_marks`='"+identification+"',`house_no`='"+house+"',`street`='"+street+"',`place`='"+place+"',`post`='"+post+"',`pin`='"+pin+"',`district`='"+district+"',`father`='"+father+"',`mother`='"+mother+"',`crime_id`='"+crime+"',`photo`='"+filename+"' WHERE `cr_id`='"+id+"'"
        c.nonreturn(qry)
    else:
        qry1 = "UPDATE `criminal` SET `name`='"+name+"',`gender`='"+gender+"',`dob`='"+dob+"',`blood_group`='"+blood+"',`identification_marks`='"+identification+"',`house_no`='"+house+"',`street`='"+street+"',`place`='"+place+"',`post`='"+post+"',`pin`='"+pin+"',`district`='"+district+"',`father`='"+father+"',`mother`='"+mother+"',`crime_id`='"+crime+"' WHERE `cr_id`='"+id+"'"
        c.nonreturn(qry1)
    return view_criminallist()


@app.route('/delete_criminallist/<id>')
def delete_criminallist(id):
    db=conn()
    qry="DELETE FROM `criminal` WHERE `cr_id`='"+id+"'"
    db.nonreturn(qry)
    return view_criminallist()


@app.route('/chat')
def chat():
    db=conn()
    qry="SELECT * FROM `user`"
    res=db.selectall(qry)
    return render_template('police/chat.html', data=res)


@app.route('/chat_ui/<id>')
def chat_ui(id):
    print("hhhh")
    print(id)
    print("dddd")
    return render_template('police/external_chat.html',lid=id)

@app.route('/external_chat_view',methods=['post'])
def external_chat_view():
    db = conn()
    lid = session['pol_id']
    toid = request.form['idd']
    qq="SELECT * FROM `chat` WHERE ((`from_id`='"+str(lid)+"' AND `to_id`='"+toid+"')OR(`from_id`='"+toid+"' AND `to_id`='"+str(lid)+"')) order by chat_id DESC"
    print(qq)
    qry = db.selectall(qq)
    print(qry)
    if len(qry)>0:
        return jsonify(qry)


@app.route('/external_chat_add',methods=['post'])
def external_chat_add():
    db = conn()
    lid = session['pol_id']
    toid = request.form['toid']
    msg = request.form['ta']
    qry = db.nonreturn("INSERT INTO `chat`(`from_id`,`to_id`,`msg`,`date`,`time`)VALUES('"+str(lid)+"','"+toid+"','"+msg+"',CURDATE(),CURTIME())")
    if len(qry)>0:
        return render_template('police/external_chat.html',lid=toid)


@app.route('/lookout_notice/<id>')
def lookout_notice(id):
    db=conn()
    qry="insert into lookout values (null ,'"+id+"')"
    db.nonreturn(qry)
    return redirect('/view_criminallist')

@app.route('/view_lookout')
def view_lookout():
    db=conn()
    qry="SELECT lookout.*,criminal.* FROM `lookout`,`criminal` WHERE `criminal`.`cr_id`=lookout.`cr_id` AND `criminal`.`pid`='"+str(session['log_id'])+"'"
    res=db.selectall(qry)
    return render_template('Police/view_lookout.html',data=res)

@app.route('/delete_lookout/<id>')
def delete_lookout(id):
    db=conn()
    qry="delete from lookout where lookout_id='"+id+"'"
    db.nonreturn(qry)
    return redirect('/view_lookout')



if __name__ == '__main__':
    app.run(port=4500)
