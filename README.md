
# Authentication App

This project is a Django-based web application designed to handle user authentication. It includes features like user registration, login, logout, and password management. The project is structured using Django’s best practices for modularity and scalability.






## Run Locally

Clone the project

```bash
  git clone https://github.com/thorbus/WhatBytes_Assignment.git
```

Go to the project directory

```bash
  cd Authentication_app
```

Install dependencies

```bash
  pip install django
  pip install django-crispy-forms
  pip install django-bootstrap4

```

Run Database Migration

```bash
  
    python manage.py migrate


```

Run App

```bash
  
      python manage.py runserver


```





## Environment Variables


## Features


User Authentication

    Login using email or username with a secure password.
    Sign up with validation for username, email, and password.
    Forgot Password functionality with an email-based reset link.
    Change Password feature accessible only to authenticated users.

Page Access Restrictions

    Restrict access to the Dashboard, Profile, and Change Password pages for unauthenticated users.
    Redirect unauthenticated users to the login page.

Pages

    Login Page
        Fields for username/email and password.
        Links for Sign Up and Forgot Password.

    Sign Up Page
        Fields for username, email, password, and confirm password.
        Redirect to the Login page after successful registration.

    Forgot Password Page
        Input field for email.
        Sends a password reset link to the provided email address.

    Change Password Page
        Requires authentication to access.
        Fields for old password, new password, and confirm new password.
        Redirects to the Dashboard after a successful password change.

    Dashboard
        Displays a greeting message like "Hi, username!".
        Links to the Profile and Change Password pages.
        Option to log out.

    Profile Page
        Displays user information:
            Username
            Email
            Date Joined
            Last Updated
        Links back to the Dashboard.
        Option to log out.
