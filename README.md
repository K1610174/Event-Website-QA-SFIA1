# DEVOPS CORE FUNDAMENTAL PROJECT
- [DEVOPS CORE FUNDAMENTAL PROJECT](#devops-core-fundamental-project)
  - [BRIEF](#brief)
    - [Requirements](#requirements)
    - [My Aproach](#my-aproach)
  - [ARCHITECTURE](#architecture)
    - [Database Structure](#database-structure)
  - [CI PIPELINE](#ci-pipeline)
    - [Technologies](#technologies)
  - [PROJECT TRACKING](#project-tracking)
        - [Backlog](#backlog)
        - [Roadmap](#roadmap)
  - [RISK ASSESSMENT](#risk-assessment)
  - [TESTING](#testing)
  - [FRONT-END DESIGN](#front-end-design)
        - [Events](#events)
        - [Add Event](#add-event)
        - [Update](#update)
        - [Add Organiser](#add-organiser)
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
* Create a new event that is stored with details:
  - Event Name
  - Event Date
  - Description
  - Location
  
* View the events created by clicking the Events link in the navigation bar.
* Update and Delete the events.

* Create an organiser that is stored with details:
  - First Name
  - Last Name
  - Email


## ARCHITECTURE 
### Database Structure
Using an entity relationship diagram (ERD), I modeled the database structure with only the events and organiser tables implemented in the application.

![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/database_erd.png)

The ERD above shows a many to many relationship between the Events and the organisers using an association table (EventDetails). This means that events can have multiple organisers as well as organisers have many events.

## CI PIPELINE

![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/CI-Pipeline.PNG)

### Technologies
- JIRA: Project tracking
- Python: Source code
- FLask: Micro-framework
- Pytest: Unit Testing, Intergration Testing
- Git: Version Control System
- Jenkins: CI Server
- Google Cloud Platform: Virtual Machine and SQL Database
  

## PROJECT TRACKING
JIRA project management software was used to keep track of the progress of this project using a Kanban board.
##### Backlog
![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/backlog1.PNG)
![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/baclog2.PNG)
##### Roadmap
![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/roadmap.png)


## RISK ASSESSMENT
The risk assessment can be found by following the link below.

https://docs.google.com/spreadsheets/d/1uG0-4umykmeh4dQfKx4uUiqPzO27zNEqC6dxjtGQjgI/edit?usp=sharing

## TESTING
Pytest Unit testing and Intergration testing were used to carry out the tests for the application. 
An overall test coverage report of 89% was achieved with all the written tests passing.

![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/test-cov.PNG)

## FRONT-END DESIGN

##### Events
![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/eventspage.PNG)

##### Add Event
![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/addevent.PNG)

##### Update
![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/update.PNG)

##### Add Organiser
![](https://github.com/K1610174/QA-SFIA1/blob/documentation/images/addorganiser.PNG)

## ISSUES
The time of event can only be entered into the database using the update page instead of creation of the event.

## FUTURE IMPROVEMENTS
Currently, there is no registration or login functionality for the application. I would like different organisers to be able to login nd create events as well as see events created by other organisers. 

## AUTHORS
Amanda Kekitinisa
