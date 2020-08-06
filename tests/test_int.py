import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Events, Event_Details, Organisers

test_organiser_first_name = "John"
test_organiser_last_name = "Doe"
test_organiser_email = "john@email.com"

test_event_event_name= "Event One"
test_event_event_date="10-10-2020 00:00:00"
test_event_location="Tenerife"
test_event_description="Carnival"

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/kkekitinisa/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestEvent(TestBase):

    def test_add_event(self):

        self.driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="event_name"]').send_keys(test_event_event_name)
        self.driver.find_element_by_xpath('//*[@id="event_date"]').send_keys(
            test_event_event_date)
        self.driver.find_element_by_xpath('//*[@id="description"]').send_keys(
            test_event_description)
        self.driver.find_element_by_xpath('//*[@id="location"]').send_keys(
            test_event_location)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        assert url_for('event') in self.driver.current_url

class TestOrganiser(TestBase):
    def test_add_organiser(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/a[3]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_organiser_first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
            test_organiser_last_name)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(
            test_organiser_email)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)
        assert url_for('home') in self.driver.current_url


if __name__ == '__main__':
    unittest.main(port=5000)
