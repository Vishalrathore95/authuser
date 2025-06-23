![Screenshot (30)](https://github.com/user-attachments/assets/8fac1f99-2a7b-4b02-b923-168553660f7b)# Django User Authentication System

This is a Django-based user authentication system that provides a simple and secure way to manage users. It includes features such as sign up, login, logout, change password (with and without the old password).

## 🔐 Features

- User Sign Up
- User Login
- User Logout
- Change Password (with old password)
- Change Password (without old password)

## 🛠️ Technologies Used

- Python
- Django (latest version)
- HTML/CSS (for basic frontend)

## 📁 Project Structure

myproject/
│
├── authuser/ # Django app for authentication
│ ├── templates/
│ │ ├── login.html
│ │ ├── signup.html
│ │ ├── change_password.html
│ │ └── change_password_without_old.html
│ ├── views.py
│ ├── urls.py
│ └── ...
│
├── myproject/ # Django main project folder
│ ├── settings.py
│ ├── urls.py
│ └── ...
│
├── db.sqlite3 # Default database
└── manage.py



## 🚀 Getting Started

### 1. Clone the Repository

```bash
https://github.com/Vishalrathore95/authuser
cd django-user-auth
2. Create Virtual Environment and Activate

python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
3. Install Dependencies

pip install django
4. Apply Migrations

python manage.py migrate
5. Run the Server

python manage.py runserver
6. Access the App
Open your browser and go to:


http://127.0.0.1:8000/
🔑 Authentication URLs
/signup/ - User Registration

/login/ - Login Page

/logout/ - Logout View

/change-password/ - Change password with old password

/change-password-no-old/ - Change password without old password

📌 Notes
CSRF protection is enabled in all forms.

Passwords are securely hashed using Django's default PBKDF2 algorithm.

Validation for password matching is included during registration and change password.

📷 Screenshots 
Add screenshots of login/signup/change-password pages here if needed.

![Screenshot (26)](https://github.com/user-attachments/assets/a4b7fc0b-ecce-4575-99c9-98339962fd1f)


📄 Li![Screenshot (27)](https://github.com/user-attachments/assets/1b99f209-0659-4e2c-8f13-1486334e5712)


![Screenshot (28)](https://github.com/user-attachments/assets/0fc1888f-04c7-4dee-9f60-b41f2564b446)


![Screenshot (29)](https://github.com/user-attachments/assets/b0dca4d0-9152-49d8-b26a-c55fb1fab0c6)

![Screenshot (30)](https://github.com/user-attachments/assets/ece79858-a66d-490a-875f-4069a3c9976d)


![Screenshot (31)](https://github.com/user-attachments/assets/a084d7d0-48dd-4b33-be40-6de061a73c29)


cense

This project is licensed under the MIT License - feel free to use and modify it.

Author: Vishal Rathore
For any issues or suggestions, feel free to open an issue or reach out.
