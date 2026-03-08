## Blog API

A scalable RESTful backend for a blogging platform built with Django and Django REST Framework.
The API provides endpoints for managing blog posts, categories, tags, and comments, enabling developers to build modern content-driven applications.

This project demonstrates clean backend architecture, relational database modeling, and structured API design.

# Features

Create, update, delete, and retrieve blog posts
Category-based post organization
Tagging system for flexible content discovery
Comment system for user interaction
RESTful API endpoints
Admin dashboard for content management
Structured and scalable database relationships

 ## Tech Stack

# Backend
Django
Django REST Framework

# Database
SQLite (development)

# Tools
Git
Virtual environments


## Project Structure
blog_api/
│
├── blog/                # Blog application
│   ├── models.py        # Database models
│   ├── serializers.py   # API serializers
│   ├── views.py         # API views
│   ├── urls.py          # App routes
│   └── admin.py         # Admin configuration
│
├── core/                # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py / wsgi.py
│
├── manage.py
└── requirements.txt

## Installation
# Clone the repository
git clone https://github.com/yourusername/blog-api.git
cd blog-api

# Create a virtual environment
python -m venv venv

# Activate the environment
Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Run migrations
python manage.py migrate
Start the development server
python manage.py runserver
