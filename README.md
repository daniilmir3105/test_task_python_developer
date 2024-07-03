# Hotel Booking Project

This is a Django-based hotel booking project.

## Requirements

- Python 3.8+
- Django 3.0+
- PostgreSQL

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd hotel_booking
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the PostgreSQL database:
    - Install PostgreSQL and create a database and user.
    - Update the `DATABASES` setting in `hotel_booking/settings.py` with your database credentials.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'hotel_booking_db',
            'USER': 'your_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser for accessing the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open the admin panel in your browser:

    ```
    http://127.0.0.1:8000/admin/
    ```

## Usage

- The API endpoint for rooms is available at:

    ```
    http://127.0.0.1:8000/api/rooms/
    ```

## HTTPS Setup

To set up HTTPS for your Django project:

1. Obtain SSL certificates (e.g., using Let's Encrypt).

2. Configure your web server (e.g., Nginx) to handle SSL.

3. Update your Django settings to use HTTPS:
    ```python
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    ```

## .gitignore

Ensure your `.gitignore` file includes the following to avoid committing sensitive information and unnecessary files:


## Contributing

If you would like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is open-source and available under the [MIT License](LICENSE).
