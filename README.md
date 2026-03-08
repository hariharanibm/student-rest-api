# Student CRUD REST API

## Overview

Student CRUD REST API built using Flask and SQLite.

## Features

* Add student
* Get all students
* Get student by ID
* Update student
* Delete student
* Healthcheck endpoint
* Database migration support

## Setup

```bash id="jlwmb3"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Application

```bash id="jlwmb4"
make run
```

## Migration

```bash id="jlwmb5"
export FLASK_APP=run.py
flask db upgrade
```

## API Endpoints

* GET /healthcheck
* POST /api/v1/students
* GET /api/v1/students
* GET /api/v1/students/<id>
* PUT /api/v1/students/<id>
* DELETE /api/v1/students/<id>

