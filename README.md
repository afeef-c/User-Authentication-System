# User Authentication System and Admin Panel

This project implements a User Authentication System and an Admin Panel for managing user accounts, viewing logs, and generating reports. The application is built using **Django** for the back end and **HTML/CSS/JavaScript** with **Bootstrap** for the front end. The database used is  **postgreSQL**.

---

## Features

### User Authentication System
- **User Registration**:
  - Secure user registration with proper form validation.
  - Password hashing using Django's `bcrypt`-based password system.

- **User Login/Logout**:
  - Login functionality with session-based authentication.
  - Logout functionality to clear user sessions.

- **Password Reset** :
  - Reset passwords (forgot password) by verifying user information.

### Admin Panel for Data Management
- **User Management**:
  - View, edit, and delete user accounts.

- **Logs**:
  - View logs of user activities such as account creation and password resets.

- **Reports**:
  - Generate reports of user data and logs.

- **Data Table Features**:
  - Filtering, sorting, and exporting data using `DataTables.js`.

- **Role-Based Access Control**:
  - Only admin users can access the admin panel.

---

## Technologies Used

### Back End:
- **Django**: Handles user authentication, session management, and database interactions.
- **postgreSQL**: Used for storing user credentials, logs, and other application data.Create an aws rds instace to manage db

### Front End:
- **HTML/CSS**: For structuring and styling the application.
- **Bootstrap**: Provides responsive design and in-built styling components.
- **JavaScript**: Adds interactivity and validation on the front end.
- **DataTables.js**: Enables dynamic tables with sorting, filtering, and exporting options.

---

## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/afeef-c/User-Authentication-System.git
   cd user_management
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   - User Authentication: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin`

---

## Application Details

### User Authentication System

#### Endpoints
- **Register**: `http://127.0.0.1:8000/register`
- **Login**: `http://127.0.0.1:8000/login`
- **Logout**: `http://127.0.0.1:8000/logout`
- **Password Reset**: `http://127.0.0.1:8000/password-reset`

#### Validation
- Client-side validation ensures proper input (e.g., strong passwords, non-empty fields).
- Back-end validation ensures data integrity and security.

### Admin Panel

#### Endpoints
- Admin Dashboard: `http://127.0.0.1:8000/admin-panel`

#### Features
- Role-based access control ensures only admin users can access this panel.
- Data tables include options for filtering, sorting, and exporting data.

---

## Screenshots

### User Authentication Pages
1. **Register Page**:
   ![Register Page](screenshots/register.png)
2. **Login Page**:
   ![Login Page](screenshots/login.png)

### Admin Panel
1. **Dashboard**:
   ![Dashboard](screenshots/dashboard.png)
2. **User Management**:
   ![User Management](screenshots/user_management.png)

---

## Security Features
- Passwords are securely hashed using Django's authentication system.
- Sessions are used to manage user authentication securely.
- Admin panel access is restricted to users with admin privileges.

---

## Dependencies
- **Django**
- **Bootstrap**
- **PostgreSQl**
---

## Future Enhancements
- Add support for JWT authentication.
- Implement email verification for registration and password reset.
- Enhance the admin panel with graphical analytics and user activity charts.

---

