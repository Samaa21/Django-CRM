# Django CRM 
A simple **Customer Relationship Management (CRM)** application built with Django.  
This project demonstrates core Django features such as routing, templates, views, and **CRUD operations** (Create, Read, Update, Delete) for managing records.

---

## Features

- **Home Page** rendering with Django templates.
- **CRUD Operations** for managing records:
  - **Create** new records via forms.
  - **Read** (view) record details in a clean interface.
  - **Update** existing records with real-time validation.
  - **Delete** records securely with confirmation.
  - 
- Django's **Admin Panel** for superuser management.
- Clean URL routing using `urls.py`.
- Project structure with reusable templates and apps.

---

## Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS (Django templates)
- **Environment:** Virtualenv

---

---

## Installation

### 1. Clone the repository
```bash Command

git clone https://github.com/Samaa21/Django-CRM.git

### 2.Create and activate a virtual environment
python -m venv virt

# Windows GitBash
source virt\Scripts\activate

### 3.Install dependencies
pip install django mysql-connector-python

## For SQl Server
pip install mysqlclient

### 4.Apply migrations:
python manage.py migrate

### 5.Running the Server
python manage.py runserver

### Go to server
http://localhost:8000

