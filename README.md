# DEVOPS CORE FUNDAMENTAL PROJECT
- [DEVOPS CORE FUNDAMENTAL PROJECT](#devops-core-fundamental-project)
  - [BRIEF](#brief)
    - [Requirements](#requirements)
    - [My Aproach](#my-aproach)
  - [ARCHITECTURE](#architecture)
    - [Database Structure](#database-structure)
  - [CI PIPELINE](#ci-pipeline)
  - [PROJECT TRACKING](#project-tracking)
  - [RISK ASSESSMENT](#risk-assessment)
  - [TESTING](#testing)
  - [FRONT-END DESIGN](#front-end-design)
  - [ISSUES](#issues)
  - [FUTURE IMPROVEMENTS](#future-improvements)
  - [AUTHORS](#authors)
## BRIEF
This project is an application with which a user can create, read, update and delete and event from an SQL database. This project was developed using technologies for project management, python source code development, source code management, continuous intergration and databases. 

### Requirements
* Kanban board
* Relational database - with atleast two tables with a relationship.
* Clear documentation - outlining the design, architecture and risk assessment.
* Python coded functional CRUD application.
* Testing - automated tests and best test coverage
* Flask front-end website
* Version Control System with feature branch model built through a CI server and deployed to a cloud-based virtual machine.

### My Aproach
For this project, I decided to develop a simple event application that allows a user to do the following:
    Create a new event that is stored with details:
        Event Name
        Event Date
        Description
        Location

    View the events created by clicking the Events link in the navigation bar.
    Update and Delete the events.

    Create an organiser that is stored with details:
        First Name
        Last Name
        Email


## ARCHITECTURE 
### Database Structure
Using an entity relationship diagram (ERD), I modeled the database structure with only the events and organiser tables implemented in the application.

ERD

The ERD above shows a many to many relationship between the Events and the organisers using an association table (EventDetails). This means that events can have multiple organisers as well as organisers have many events.

## CI PIPELINE




## PROJECT TRACKING
JIRA project management software was used to keep track of the progress of this project using a Kanban board.

Backlog

Roadmap


## RISK ASSESSMENT
The risk assessment can be found by following the link below.

https://docs.google.com/spreadsheets/d/1uG0-4umykmeh4dQfKx4uUiqPzO27zNEqC6dxjtGQjgI/edit?usp=sharing

## TESTING
pytest unit testing and intergration testing

## FRONT-END DESIGN
Events

Add Event

Update

Add Organiser

## ISSUES
can only enter the time of event using the update page instead of creation of the event.
## FUTURE IMPROVEMENTS
Include a register and login functionality
match the organisers to the events on the website
## AUTHORS
Amanda Kekitinisa