from flask import Flask, render_template,request,redirect,url_for
import db

app= Flask(__name__)
global events
events=db.getEvents()

@app.route("/home")
def renderHome():
    global events
    return render_template('Home.html', events=events)


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
    print (events)
    db.postEvent(event_datetime,event_title,event_description)
    return redirect(url_for('renderHome'))


def formatdate(date, hour):
    date.replace("-", "/")
    datetime = date + " " + hour
    print(datetime)
    return datetime
