from flask import render_template,redirect, url_for, request
from application import app,db
from application.models import Events, Event_Details, Organisers
from application.forms import EventForm, UpdateEventForm, OrganiserForm

@app.route('/')
@app.route('/home')
def home():
    eventData=Events.query.all()
    return render_template('home.html', title='Home Page', events=eventData)


@app.route('/event', methods=['GET','POST'])
def event():
    form = EventForm()
    if form.validate_on_submit():
        eventData = Events(
            event_name = form.event_name.data,
            event_date = form.event_date.data,
            location = form.location.data,
            description = form.description.data
        )
        db.session.add(eventData)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('event.html', title='Add Event',form=form)


@app.route('/update/<event_id>', methods=['GET','POST'])
def update(event_id):
    event = Events.query.filter_by(event_id=event_id).first()
    form = UpdateEventForm()
    if form.validate_on_submit():
        event.event_name = form.event_name.data
        event.event_date = form.event_date.data
        event.location = form.location.data
        event.description = form.description.data
        db.session.commit()
        return redirect(url_for('home',event_id = event_id))
    elif request.method == 'GET':
        form.event_name.data = event.event_name
        form.location.data = event.location 
        form.description.data = event.description
    return render_template('update.html', title='Update',form = form)


@app.route('/delete/<event_id>', methods=['GET','POST'])
def delete(event_id):
    event = Events.query.filter_by(event_id = event_id).first()
    event_details_delete = Event_Details.query.filter_by(event_id = event.event_id).all()
    for event_details in event_details_delete:
        db.session.delete(event_details)
        db.session.commit()

    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/organiser', methods=['GET','POST'])
def organiser():
    form = OrganiserForm()
    if form.validate_on_submit():
        orgData = Organisers(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data   
        )
        db.session.add(orgData)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('organiser.html', title='Add Organiser',form=form)
