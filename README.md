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

📷 Screenshots 
Add screenshots of login/signup/change-password pages here if needed.
![Screenshot (26)](https://github.com/user-attachments/assets/8a6![Screenshot (28)](https://github.com/user-attachments/assets/3aa7281c-1af3-4cea-bebe-a37fef46d956)
578d5-1d7c-442b-9e6a-268faccfa867)![Screenshot (29)](https://github.com/user-attachments/assets/d5da4dcf-4cd0-4656-913c-d9a6c024e8bc)
![Screenshot (31)](https://github.com/user-attachments/assets/aa88c0ce-e66e-495a-938b-2d02ebcead74)

![Screenshot (30)](https://github.com/user-attachments/assets/405e5371-5211-4e06-83a1-03d00374eaa2)

📄 License![Screenshot (26)](https://github.com/user-attachments/assets/630976b0-0495-40ac-a8f1-52fc36e3b9ec)

This project is licensed under the MIT License - feel free to use and modify it.

Author: Vishal Rathore
For any issues or suggestions, feel free to open an issue or reach out.
