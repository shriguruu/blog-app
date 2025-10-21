# Django Blog Application

A simple and elegant blog application built with Django and MySQL.

## Features

- Create, read, update, and delete blog posts
- User authentication and authorization
- Rich text blog content
- MySQL database integration
- Clean and responsive interface

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- MySQL Server
- pip (Python package manager)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shriguruu/blog-app.git
cd your-repo-name
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL Database

Create a MySQL database for the project:

```sql
CREATE DATABASE blog_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'blog_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON blog_db.* TO 'blog_user'@'localhost';
FLUSH PRIVILEGES;
```

### 6. Update Database Settings

In your `settings.py`, configure the database connection:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'blog_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 7. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 9. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to view the application.

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/`
- Log in with your superuser credentials
- Start creating blog posts!

## Project Structure

```
project-name/
│
├── blog/                  # Main blog application
├── myapp/          # Project settings
├── templates/             # HTML templates
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Technologies Used

- **Django**: Web framework
- **MySQL**: Database
- **Python**: Programming language
- **HTML/Bootstrap**: Frontend

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).


## Acknowledgments

- Django Documentation
- Django Community