from flask import Flask, render_template,request,redirect,url_for
import db


app= Flask(__name__)

global events
events=db.getEvents()

def confirmAction():
    selection=0

    if(selection==1):
        return 1
    else:
        return 0

@app.route("/home")
def renderHome():
    global events
    events=db.getEvents()
    return render_template('Home.html', events=events)


@app.route("/")
def default():
    return redirect(url_for('renderHome'))


@app.route('/submit', methods=['POST'])
def submit():
    global events
    event_title = request.form['eventTitle']
    event_description = request.form['eventDescription']
    event_date = request.form['eventDate']
    event_hour = request.form['eventHour']
    event_datetime=formatdate(event_date,event_hour)
    event=(0,event_datetime,event_title,event_description)
    events.append(event)
    db.postEvent(event_datetime,event_title,event_description)
    return redirect(url_for('renderHome'))


@app.route('/delete', methods=['POST'])
def delete():
    global events
    event_ID = request.form['eventID']
    db.deleteEvent(event_ID)
    return redirect(url_for('renderHome'))


@app.route('/update', methods=['POST'])
def update():
    global events
    event_title = request.form['UeventTitle']
    event_description = request.form['UeventDescription']
    event_date = request.form['UeventDate']
    event_hour = request.form['UeventHour']
    event_ID = request.form['UeventID']
    event_datetime=formatdate(event_date,event_hour)
    db.putEvent(event_datetime,event_title,event_description,event_ID)
    return redirect(url_for('renderHome'))


def formatdate(date, hour):
    date.replace("-", "/")
    datetime = date + " " + hour
    return datetime
