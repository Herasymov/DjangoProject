# DjangoProject

DjangoProject is a Django-based web application that consists of two apps: `profiles` and `cart`. This project uses environment variables stored in a `.env` file for sensitive data such as the secret key, database credentials, and Redis cache location.

## Installation

1. Clone the repository:

git clone https://github.com/Herasymov/djangoProject.git

2. Navigate to the project directory:
 
cd djangoProject

3. Create a virtual environment (optional but recommended):

python -m venv venv

source venv/bin/activate

4. Install the project dependencies:

pip install -r requirements.txt

5. Create a `.env` file in the project root directory and update it with your environment-specific values:

SECRET_KEY=your_secret_key
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
REDIS_LOCATION=your_redis_location


Make sure to replace `your_secret_key`, `your_database_name`, `your_database_user`, `your_database_password`, `your_database_host`, `your_database_port`, and `your_redis_location` with your actual values.

6. Apply database migrations:

python manage.py migrate

7. Start the development server:

python manage.py runserver

## Configuration

The main project settings can be found in the `settings.py` file. Here are some important settings:

- `SECRET_KEY`: This is the secret key used for cryptographic signing. Make sure to keep it secret and don't share it publicly.
- `DEBUG`: Set this to `True` for development and `False` for production.
- `ALLOWED_HOSTS`: Add the hostnames or IP addresses that the application can serve. Leave it empty for development.
- `INSTALLED_APPS`: This list contains the names of all installed apps in the project. The `profiles` and `cart` apps are included by default.
- `DATABASES`: Configure the database connection details using environment variables.
- `CACHES`: Configure the Redis cache backend using environment variables.
- `AUTHENTICATION_BACKENDS`: Specify the authentication backends for the project. The default backend is included.
- `STATIC_URL`: This setting defines the URL prefix for static files.

For more information on Django settings, refer to the [official documentation](https://docs.djangoproject.com/en/4.2/ref/settings/).

## Usage

### Profiles App

The `profiles` app handles user profiles and authentication. It provides RESTful APIs for user registration, login, and profile management. The API endpoints can be accessed at `/`.

### Cart App

The `cart` app manages the user's shopping cart. The API endpoints can be accessed at `/cart/`.

## Additional Notes

- The project includes the `corsheaders` middleware and allows CORS requests from any origin (`CORS_ORIGIN_ALLOW_ALL = True`) to simplify development. Make sure to configure CORS settings appropriately for production.
- The project uses the `rest_framework` package for building APIs and token-based authentication using `rest_framework_simplejwt`.
- The JWT access token has a lifetime of 10 minutes (`'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10)`), and the refresh token has a lifetime of 1 day (`'REFRESH_TOKEN_LIFETIME': timedelta(days=1)`).
- The project includes caching using Redis. Configure the `REDIS_LOCATION` environment variable with the appropriate Redis server details.
- The project follows the UTC timezone by default (`TIME_ZONE = 'UTC'`). Adjust it according to your requirements.
- The project includes password validation settings. You can customize the password validation requirements in the `AUTH_PASSWORD_VALIDATORS` list.
- The project supports static files. By default, the static URL is set to `'static/'`. You can configure it according to your needs.
- The project uses the `django.db.models.BigAutoField` as the default primary key field type. If you need a different primary key field type, update the `DEFAULT_AUTO_FIELD` setting.

