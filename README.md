
<h1 align="center">

  <br>  
  QA Automation for REST API
  <br>
</h1>

## Test Goals
Regarding the [Trello Plataform](https://trello.com), I built in Python this solution for performing API testing and WEB testing over the Trello Boards and its dependencies.

### Objective 1 
The aim of the task is to prepare a Python or JS/TS or Postman test suite for the public Trello APIs.
Documentation is available here https://developers.trello.com/reference#introduction

Organising the actions below into test scenarios is part of the task.

* Actions/steps to be covered:
- Create a board
- Create 3 cards on that board
- Edit one of the cards
- Delete one of the cards
- Add a comment to one of the cards
 
### Objective 2

Please write a selenium test (or equivalent e.g. Cypress or Playwright) that logins in Trello and
checks the above board. Using language as TypeScript will be preferable (but you can choose any
other language you are comfortable with).

Actions/steps to be covered:
- Verify that there are 2 cards on the board
- Verify that there is a card with a comment
- Add a new comment to that card
- Set the card as DONE

Bonus

- Add negative paths to the tests

Additional info
- To get authentication tokens you have to create a free account

<h2 align="center">

  <br>
  Solution
  <br>
</h2>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![screenshot](screen-capture.gif)


## Test Plan & Test Cases

[Test Plan](https://docs.google.com/document/d/1YtnoL2g4OToV-7GQkNB_V-JdaCMcJErhLt8R20SFvLk/edit?usp=sharing)


## Key Features

* API_Adapter Module - where you will find API_Core class to perform all API operations depending on the Verb and action you want
  - Create, Get, Update and Delete **Boards**
  - Create, Get, Update and Delete **Lists**
  - Create, Get, Update and Delete **Cards**
  - Create, Get, Update and Delete **Comments**
  - Perform **Actions**

    Métodos:
    - **Lib_actions**
    - **Lib_boards**
    - **Lib_cards**
    - **Lib_lists**


* WEB_Adapter Module - where you will find WEB_Core class to perform all WEB operations depending on the action over the page
  - **Locators** : where you will find the main ways of reaching an element (ongoing improvements)
  - **Web_Actions** : where you will find the encapsuled methods to use the locators
  - **Web_Methods** : methods that portrays the proper action done and named as a user (High Level), like: Deleting a card, Comment a card


* Data_Adapter Module - Unfinished module to create a Test DataBase and generate random data for your fuutre test (need to be adapted for this project)

* Test_Cases - where you will find the automated tests built on RobotFramework

* Requirements.txt - all dependencies/modules required to run this project if you want to know more, but I used a virtual enviroment (venv) for this project

* Cross browsers 
  - Chrome, Firefox.

  ## Credits

This software uses the following open source packages:

[Robot Framework](https://robotframework.org/robotframework/)

[Python](https://docs.python.org/3/)


## Observations

## TODO

- Try to solve the problem with Manager WebDrivers Library, it has not been working when executing from Robot FrameWork, only when using py command.

- Implement if it’s feasible, more neagtive Test Cases by using Robot Framework

- It would be interesting to use Locust framework in case of requiring Performance or Load Testing

- Try to think up other unhappy flows and evaluate them to see if it’s worthy automate them

- Get Data_Adapter done/working to generate data for tests and track it (db persistence)

- Increase the Unit Tests, only made for WEB_Core.py

- Try to implement BDD practices or using pytest-bdd module

- Try to create a docker image from this solution

- Implement security Testing



## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone 

# Go into the repository
$ cd Zyte_Project

# Install dependencies
$ pip3 install -r requirements.txt


