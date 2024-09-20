# InstaCloneProject

InstaClone is a web application built using Django (API/backend) and JavaScript (frontend), 
inspired by some functionalities of Instagram. It allows users to create posts, upload images, comment on posts, and like posts. 
This project uses a media folder to store uploaded images and provides a carousel view for posts with multiple images.

## Features

- User can create posts with images and descriptions.
- User can like and comment on posts.
- Posts with multiple images are displayed using a carousel.
- Responsive design for displaying profile images, posts, and interactions.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or 4.x
- Node.js (optional if you want to use advanced frontend tools)

### Steps to Set Up

1. Clone the repository:

```bash
git clone https://github.com/yourusername/instaboard.git
cd instaboard


python -m venv venv
source venv/bin/activate  # For Linux/Mac
# or
venv\Scripts\activate  # For Windows

pip install -r requirements.txt

cd backend
python manage.py migrate
python manage.py createsuperuser  # Optional: Create a superuser for the admin panel
python manage.py runserver
