![Screenshot (30)](https://github.com/user-attachments/assets/8fac1f99-2a7b-4b02-b923-168553660f7b)


![Screenshot (27)](https://github.com/user-attachments/assets/51d21b2e-78a4-4531-89e3-214d0250de1a)

![Screenshot (26)](https://github.com/user-attachments/assets/a7226e9f-2e8a-42b3-9912-4e6e33ba805f)

![Screenshot (28)](https://github.com/user-attachments/assets/4e019b1a-6f59-4886-a0dd-59c25da31a21)
![Screenshot (29)](https://github.com/user-attachments/assets/f9e7053c-48a7-43a3-acb1-7145e4a0472d)
![Screenshot (31)](https://github.com/user-attachments/assets/189c6cd6-95ef-4ab2-838e-6e4aaac6f0aa)

# Django User Authentication System

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





cense

This project is licensed under the MIT License - feel free to use and modify it.

Author: Vishal Rathore
For any issues or suggestions, feel free to open an issue or reach out.
