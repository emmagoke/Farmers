# Assessment

## Local Requirement

- Requires Python 3.7 or Later
- Django 4.1 or Lower
- MySql version 5

#### Virtual Environment

For this project I used pipenv to create and manage my virtual environment.[pipenv installation guide](https://pipenv.pypa.io/en/latest/installation/)

##### To Create a virtual Environment

```
pipenv shell
```

After pipenv installation, I the clone project directory run

```
pip install -r requirements.txt install
```

## Database Setup

#### Running Mysql

To `start` your server use
` sudo service mysql start`

Create a database called `assessment`

```
CREATE DATABASE IF NOT EXISTS assessment;
```

You can also change the database settings in `assessment\settings.py`

```
# some settings

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'assessment',
       'USER': 'goke',
       'PASSWORD': 'root',
       'HOST': '127.0.0.1',
       'PORT': '3306',
       'OPTIONS': {
           'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
       }
# some more setting
```

#### Running the Migrations

To run the migrations. In the project directory run

```
 python manage.py migrate;
```

#### Creating a superuser

To access the admin panel in django, create a super user

```
 python manage.py createsuperuser
```

## To run the Django Development Server

`python manage.py runserver`

## Endpoints

### POST '/api/v1/auth/create-user/'

- This endpoint is for user registration
- Request Body:

```
{
	"first_name": "first name",
    "last_name": "last name",
    "email": "your email",
    "phone_number": "your nigeria phone",
    "password": "your password"
}
```

- Response: A status code `201` if request is successful.

### POST 'api/v1/auth/login/'

- This is the login endpoint, you can use email/phone number and password to login
- Request Body:

```{
	'email': 'your email/ or phone numer',
	'password': 'your password'
}
```

- Response: A status code `200` if request is successful and two pair of `jwt` token

```{
	'refresh': 'refresh token',
	'access': 'access token'
}
```

### GET '/api/farmers/<int:farmer_id>'

- This is endpoint retrieve a single user. You pass the `farmer id` in the url path
- Request Header : {'Bearer': 'access_jwt_token_generated_during_login'}
- Request Body:

```{
	'email': 'your email/ or phone numer',
	'password': 'your password'
}
```

- Response: A status code `200` if request is successful and the users details
  e.g /api/farmers/10 will return a respone like

```
{
	10,
	"Wale",
	"Sam",
	"07023456789”,
	34,
	"90, Sam ife str, Ikeja, Lagol”,
	“maize, rice, cassava”,
	“dry/rainy”
}
```

### GET '/api/v1/farmers/list?min_age=30&crops=maize&page=1'

- Gets a list all farmers in the data base, paginated by 10
- Request Header : {'Bearer': 'access_jwt_token_generated_during_login'}

- Response: A list of all the farmers in the database.

> Example: `curl http://127.0.0.1:5000/api/v1/farmers/list?min_age=30&crops=maize&page=1`

```
[
	{
 	4,
 	"Wale",
 	"Sam",
 	"07023456789”,
 	34,
 	"90, Sam ife str, Ikeja, Lagos",
 	"maize, rice, cassava",
 	"dry/rainy',
 	'The user_id of the user that created it'
	},
	{
 	9,
 	"Wale",
 	"Sam",
 	"09023190789”,
 	34,
 	"9, ife str, Ibadan, oyo",
 	"maize, rice, cassava",
 	"dry/rainy',
 	'The user_id of the user that created it'
	},
	...
]
```

### POST 'api/v1/farmers/create/'

- This endpoint allows SINGLE BULK insertion endp
- Request Header : {'Bearer': 'access_jwt_token_generated_during_login'}
- Request Body: Note the phone_number n=must be unique

```{
	id,
	first_name,
	last_name,
	phone_number,
	age,
	address,
	crops,
	season_best_for_crops
}

or a List
[
	...,
	{
	id,
	first_name,
	last_name,
	phone_number,
	birth_date,
	address,
	crops,
	season_best_for_crops
	},
	...
]
```

- Response: status code to show success or not

> Example: `curl http://127.0.0.1:5000/api/v1/farmers/create/`

```
{
	message: "Farmers Successfully Created"
}
```

<!-- ### GET 'farmers/users/<int:user_id>/

- Gets a dictionary of questions, paginated in groups of 10.
- Response a csv file all farmers a certain user has created as a csv file

> E.g: `curl http://127.0.0.1:5000/questions`

```
{
    "categories": [
        "Science",
        "Art",
        "Geography",
        "History",
        "Entertainment",
        "Sports"
    ],
    "current_category": [],
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 1,
            "difficulty": 5,
            "id": 24,
            "question": "The Astronomical Unit (AU) is a unit of measurement based on the average distance between what two bodies?"
        }
        ... # remaining questions on the page
    ],
    "success": true,
    "total_questions": 40
}
``` -->

## Documentation

- /api/schema/swagger/

## Running the Celery Worker For Cron JOB

- To run the celery beat `celery -A core worker --loglevel=info --beat` in another console tab, but in the **directory** that contains this code

## The Management Tool

- This management tool requires a url parameter. You new to set the environment variable `USERNAME` and `PASSWORD`

```
e,g USERNAME=username PASSWORD=your_password python manage.py csv_upload url
```
