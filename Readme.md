# Person resource Webservice API



## Table of Contents
- [Person Resource Webservice API](#person-resource-webservice-api)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Install Dependencies](#2-install-dependencies)
    - [3. Database Setup](#3-database-setup)
    - [4. Run migrations](#4-run-migrations)
    - [5. Create a superuser](#5-create-a-superuser)
    - [6. Run the Development Server](#6-run-the-development-server)
  - [API Endpoints](#api-endpoints)
  - [Usage](#usage)
- [Example 1](#example-1)
  - [Response](#response)
  - [Example 2 ](#example-2-)
  - [Response ](#response-)

## Introduction
Person resouce webservice is a web application that provides CRUD(Create,Read, Update, Delete) operations for managing information about people. It was built using Django rest framework and sqlite and provides th


## Requirements

- Python 3.7 or higher
- Django 4.0
- Django Rest Framework (DRF) 3.8
  

## Setup


### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```
### 2. Install Dependencies<br>
```
pip install -r requirements.txt
```
### 3. Database Setup
Create a database and configure your database settings in settings.py.
### 4. Run migrations<br>
```
python manage.py migrate
```
### 5. Create a superuser<br>
```
python manage.py createsuperuser
```
### 6. Run the Development Server<br>
```
python manage.py runserver
```
## API Endpoints

- POST /api/: Create a new person record.
- GET /api/{id}/: Retrieve person(s) by name.
- PUT /api/{id}/: Update a person by name.
- DELETE /api/{id}/: Delete a person by name.


## Usage
 1. Start the Development server :

    python manage.py runserver<br>


2. Acsess the API using the provided endpoints:<br>
   
- To add a new person  : POST :<br>

    http://localhost:8000/api
- To get a person by id : GET:<br>
  http://localhost:8000/api/{id}

- To uodate a person's data by id :<br>
PUT:<br>
http://localhost:8000/api/{id}<br>

- To delete a person by id:<br> 
  http://localhost:8000/api/{id}

# Example 1<br>
POST : http: // localhost: 800 /api<br>
JSON : {
    <br>
    "name" : "Chisom"<br>
}<br>
## Response<br>

{ 
    <br><br>
    "success" : "True",<br>
    "message" : "Added Successfuly !<br><br>
}

## Example 2 <br>

GET: http : // localhost : 8000 /api/ {id}<br>

## Response <br>
{ <br><br>
    "name: Paschal" <br><br>
}