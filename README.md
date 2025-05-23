# Contacts API

A RESTful API for managing contacts built with Django REST Framework.

## Features

- User Authentication with JWT
- Contact Management (CRUD operations)
- Swagger Documentation
- CORS Support

## Tech Stack

- Python 3.10
- Django
- Django REST Framework
- PyJWT
- Swagger/OpenAPI Documentation

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create .env file with required environment variables:
   ```
   DEBUG=False
   SECRET_KEY=your-secret-key-here
   JWT_SECRET_KEY=your-jwt-secret-key-here
   SECURE_SSL_REDIRECT=True
   ```
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Start the server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login user
- `GET /api/contacts/` - List all contacts
- `POST /api/contacts/` - Create new contact
- `GET /api/contacts/{id}/` - Retrieve contact
- `PUT /api/contacts/{id}/` - Update contact
- `DELETE /api/contacts/{id}/` - Delete contact

## Documentation

API documentation is available at:
- Swagger UI: `/`
- ReDoc: `/redoc/`

## Deployment

This project is configured for deployment on Heroku:

1. Create a new Heroku app
2. Set the required environment variables in Heroku
3. Deploy using Git:
   ```
   git push heroku main
   ```

## License

MIT License#   c o n t a c t s  
 