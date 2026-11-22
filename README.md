# Flask Authentication System

A user authentication web application built with **Python, Flask, Jinja2, and SQLite**. The application allows users to create accounts, log in securely, access protected pages, and log out.

## Features

- **User Registration:** Allows new users to create accounts.
- **User Login:** Authenticates registered users using their credentials.
- **Password Hashing:** Uses Werkzeug security utilities to hash passwords before storing them in the database.
- **Session Management:** Maintains user authentication sessions.
- **Protected Routes:** Restricts access to authenticated users.
- **User Logout:** Allows users to terminate their sessions.
- **Flash Messages:** Displays feedback and error notifications to users.
- **SQLite Database:** Stores user account information.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Flask | Web application framework |
| Jinja2 | HTML templating engine |
| SQLite | Database management |
| Werkzeug | Password hashing and verification |
| HTML | Web page structure |
| CSS | Web page styling |
| JavaScript | Client-side functionality |

## Project Structure

```text
authentication-system/
│
├── app.py
├── data_b.db
│
├── templates/
│   ├── home.html
│   ├── login.html
│   └── dashboard.html
│
├── static/
│   └── styles.css
│
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Navigate into the Project Directory

```bash
cd authentication-system
```

### 3. Create a Virtual Environment

```bash
python3 -m venv vir-env
```

### 4. Activate the Virtual Environment

On Linux:

```bash
source vir-env/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python3 app.py
```

### 7. Open in Your Browser

Visit:

```text
http://127.0.0.1:5000
```

## How It Works

### Registration

1. A new user visits the registration page.
2. The user provides the required information.
3. The application validates the submitted information.
4. The password is hashed using Werkzeug.
5. The user's information is stored in the SQLite database.
6. The user is redirected to the login page.

### Login

1. The user submits their login credentials.
2. The application retrieves the user's information from the database.
3. Werkzeug verifies the submitted password against the stored password hash.
4. If the credentials are valid, the application creates an authenticated session.
5. The user gains access to protected pages.

### Logout

1. The user requests to log out.
2. The application clears the authentication session.
3. The user is redirected to an appropriate page.
4. Protected pages are no longer accessible without authentication.

## Security Considerations

- Passwords are stored as hashes rather than plain text.
- User sessions are managed using Flask's session functionality.
- Protected routes require authentication.
- User input should be validated before processing.
- A secure secret key should be configured through environment variables before deployment.

## Future Improvements

- Password reset functionality.
- Email verification.
- User profile management.
- Role-based access control.
- Improved form validation.
- Automated application testing.

## Currently Saved Accounts

| Name | Email | Password |
|---|---|---|
| Samuel | sam@gmail.com | sam65mnL |
| Peter | pete@yahoo.com | pET78nmw7 |
| Elizabeth | liz@gmail.com | liZa120uj |
| Patrick | pat65@yahoo.com | pay6trPU |
| Maxwell | max34@yahoo.com | Mah67YTr45 |


This project was developed as a practical exercise in Python backend development, Flask web development, database integration, and user authentication.