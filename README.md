# Smart Start Academy

A comprehensive Django-based school management system designed to streamline administrative tasks for schools, teachers, students, and parents.

## Features

### User Management
- **Multi-Role Authentication**: Supports four user roles - School, Teacher, Student, and Parent.
- **Custom User Model**: Email-based authentication with role-based access control.
- **Profile Management**: Users can update their profiles, including photos and contact details.

### School Administration
- **School Registration**: Schools can register and create their profiles with details like name, code, establishment year, contact, and website.
- **Dashboard**: Overview of total students, teachers, subjects, and classes (standards) in the school.

### Student Management
- **Add Students**: Schools can add new students with details such as GR number, roll number, admission date, caste, date of birth, blood group, and parent contact.
- **View All Students**: List all students in the school, ordered by GR number.

### Class Management
- **Add Standards**: Create classes (standards) with division and room number.
- **View All Standards**: List all classes in the school.

### Subject Management
- **Add Subjects**: Create subjects linked to specific classes, with code and description.
- **View All Subjects**: List all subjects in the school.

### Additional Features
- **Responsive UI**: Built with HTML, CSS, and JavaScript for a user-friendly interface.
- **REST API Ready**: Includes Django REST Framework for potential API integrations.
- **Media Handling**: Support for uploading user photos and other media files.

## Tech Stack
- **Backend**: Django 5.2.7
- **Database**: SQLite (default, can be configured for PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, JavaScript
- **API Framework**: Django REST Framework
- **Authentication**: Django's built-in auth with custom user model

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/smart-start-academy.git
   cd smart-start-academy
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage

1. **Register a School**: Visit the registration page to create a new school account.
2. **Login**: Use your email and password to log in.
3. **Manage School Data**: Once logged in as a school admin, you can add/view students, classes, and subjects.
4. **Profile Updates**: Update school and user profiles as needed.

## Project Structure

```
smart_start_academy/
├── main_app/                 # Main Django app
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── forms.py             # Django forms
│   ├── urls.py              # URL patterns
│   ├── admin.py             # Admin configurations
│   ├── migrations/          # Database migrations
│   └── ...
├── smart_start_academy/     # Project settings
├── static/                  # Static files (CSS, JS)
├── templates/               # HTML templates
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support,
Email - sureshparmar.dev@gmail.com,
Phone no - 9879929741.