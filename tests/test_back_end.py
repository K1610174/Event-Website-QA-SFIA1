import unittest
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Events, Event_Details, Organisers
from wtforms.validators import ValidationError
from os import getenv


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        event = Events(event_name='Test',event_date='2020-09-09 00:00:00',location='Zanzibar',description='First test event.')

        organiser = Organisers(first_name='John',last_name='Doe',email='john@doe.com')

        details = Event_Details(event_id=1,organiser_id=1)

        db.session.add(event)
        db.session.add(organiser)
        db.session.commit()
        db.session.add(details)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_eventpage_view(self):
        response = self.client.get(url_for('event'))
        self.assertEqual(response.status_code, 200)

    def test_organiserpage_view(self):
        response = self.client.get(url_for('organiser'))
        self.assertEqual(response.status_code, 200)

    def test_updatepage_view(self):
        response = self.client.get('/update/1')
        self.assertEqual(response.status_code, 200)


class TestEvents(TestBase):
    def test_add_new_event(self):
        with self.client:
            response = self.client.post(
                url_for('event'),
                data=dict(
                    event_name='Test Event',
                    event_date='2020-09-09 00:00:00',
                    location='London',
                    description='First test event.'
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test Event', response.data)
            
    def test_redirect_eventpage(self):
        with self.client:
            response=self.client.get(url_for('event'),follow_redirects=True)
            self.assertEqual(response.status_code, 200)

class TestUpdateEvent(TestBase):

    def test_update_event(self):
        with self.client:
            response = self.client.post(
                    '/update/1',
                    data=dict(
                        event_name='Event',
                        event_date='2020-09-09 00:00:00',
                        location='Zanzibar',
                        description='This is an update'
                        ),
                    follow_redirects=True)
            self.assertIn(b'Event', response.data)
            self.assertEqual(response.status_code, 200)
        
    def test_update(self):
        with self.client:
            response = self.client.post(('/update/1'),data=dict(
                        event_name='Event One',
                        event_date='2020-09-09 00:00:00',
                        location='Zanzibar',
                        description='This is an update'
                        ),follow_redirects=True ) 
            self.assertIn(b'Event One',response.data)
            self.assertNotIn(b'Test Event',response.data)
            self.assertEqual(response.status_code, 200)

    def test_redirect_updatepage(self):
        with self.client:
            response=self.client.get(('/update/1'),follow_redirects=True)
            self.assertEqual(response.status_code, 200)


class TestDeleteEvent(TestBase):
    
    def test_delete_event(self):
        with self.client:
            response = self.client.post('/delete/1',follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_redirect_deletepage(self):
        with self.client:
            response=self.client.get(('/delete/1'),follow_redirects=True)
            self.assertEqual(response.status_code, 200)

class TestOrganisers(TestBase):
    def test_add_new_organiser(self):
        with self.client:
            response = self.client.post(
                url_for('organiser'),
                data=dict(
                    first_name='Test',
                    last_name='Name',
                    email='test@name.com'
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test', response.data)

    def test_redirect_eventpage(self):
        with self.client:
            response=self.client.get(url_for('organiser'),follow_redirects=True)
            self.assertEqual(response.status_code, 200)
