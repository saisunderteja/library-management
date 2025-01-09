# Library Management

This project is a **Library Management** built using **FastAPI**, designed to handle user and book data efficiently. It supports user authentication, book management, and database integration using SQLAlchemy ORM and MySQL. The project structure follows best practices for modularity and scalability, making it easy to maintain and extend.

---

## Key Features

### **1. User Management**
- Create, Read, Update, and Delete (CRUD) operations for user data.
- Secure storage of user passwords using hashing (`bcrypt`).
- User data validation with Pydantic schemas.

### **2. Book Management**
- CRUD operations for managing book records.
- Support for dynamic data validation using Pydantic schemas.

### **3. Authentication**
- Secure authentication using hashed passwords.
- Token-based authentication can be extended for secure API access.

### **4. Database Integration**
- MySQL database integration using SQLAlchemy ORM.
- Database schema and model definitions are centralized in `models.py`.
- Easy-to-configure database connection in `database.py`.

### **5. API Documentation**
- Auto-generated interactive API documentation with Swagger UI at `/docs`.

---

## Installation and Setup

### **1. Clone the Repository**
```
git clone https://github.com/YOUR_GITHUB_USERNAME/library-management.git
cd library-management
```
### **2. Create a Virtual Environment**
```
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows
```
### **3. Install Dependencies**
Install the required dependencies listed in `requiements.txt`:
```
pip install -r requirements.txt
```

### **4. Set Up the Database**
- Create a MySQL database (e.g: `library_management`).
- Update the database connection settings in `app/database.py`:
```
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost:3306/library_management"
```

### **5. Run the Application**
Start the FastAPI server using:
```
uvicorn app.main:app --reload
```
Access the API documentation at:
- Swagger UI: `http://127.0.0.1:8000/docs`
---

## Usage
### **1. Endpoints**
The following API endpoints are available:
#### User Endpoints
- POST /users: Create a new user.
- GET /users/{user_id}: Retrieve user details by ID.
- PUT /users/{user_id}: Update user information.
- DELETE /users/{user_id}: Delete a user.
#### Book Endpoints
- POST /books: Add a new book.
- GET /books/{book_id}: Retrieve book details by ID.
- PUT /books/{book_id}: Update book information.
- DELETE /books/{book_id}: Delete a book.
#### Authentication
- POST /auth/login: Authenticate a user and generate an access token.
