# Mission Control Center Backend

This a backend project for storing records from a table in case an audit trail. We can store Applications, each application has a configuration object that could be of different types, each one has a set of roles and permissions depending of the type: {Role_key: Value} 

## Usage

This project stills on development but already provides functional endpoints ready to use:

### How to use the mission control service endpoints

Applications and Configurations both supports CRUD endpoints. For Mission control center we need to use the following.

Create an Application:
```
(POST) /api/v1/applications/
{
    "name": "Application Name",
    "department": "Department Name"
}
```

Get all applications:
```
(GET) /api/v1/applications/
```

Create a Configuration:
```
(POST) /api/v1/configurations/
{
    "type_choice": "meta",
    "roles_set": {"role_v1": "value for role", "role_v2": "value for role2"}
    "application": 1
}
```

Update a Configuration:
```
(PUT) /api/v1/configurations/
{
    "type_choice": "meta",
    "roles_set": {"role_v3": "value for role", "role_v6": "value for role6"}
    "application": 1
}
```

Get all configurations filtered by Application id:
```
(GET) /api/v1/configurations/?application=1
```

Get all versions for a configuration:
```
(GET) /api/v1/configurations/1/versions/
```

## Configure the project
### Create a virtualenv

```
$ python3 -m venv mission_control_center
```

This command will create a new folder with the name `mission_control_center`

### Clone the project

First verify your SSH Keys on github configuration
then if you dont have a key that points to your computer follow this tutorial:

* https://docs.github.com/de/developers/overview/managing-deploy-keys

```
$ git clone git@github.com:junior92jr/mission-control-center-backend.git
```

### Activate your enviroment
Inside the `mission_control_center` folder run the following command

```
$ source bin/activate
```

After this you will see the virtualenv name in your prompt. i.e.:

```
(mission_control_center) $
```

### Install requirements
```
(location_advisor)$ cd location_advisor_backend

(mission_control_center)$ pip install -r requirements.txt
```

### Setting up environment variables for project

For environment variables configuration, you will need a .env file in the parent directory of the current folder.

```
(mission_control_center) $ touch ../.env
```

../.env example

```
DEBUG=True

SECRET_KEY="secret_key_for_django_application"

FOURSQUARE_API_KEY="mission_control_center_api_key"
```


# Running the project
## Run the project

Once you have everything ok, you can run the project.

```
(mission_control_center) $ ./manage.py check

(mission_control_center) $ ./manage.py migrate

(mission_control_center) $ ./manage.py runserver
```

## Run tests

Coverage is configured for the project for running tests and measuring in Scrutinizer

```
(mission_control_center) $ coverage run --source="." manage.py test --settings=mission_control_center.test_settings --verbosity=2
```

Once ran, if you want to see fast the results you can run

```
(mission_control_center) $ coverage report
```

or you can run 

```
(mission_control_center) $ coverage html
```

and an HTML view of your test coverage will be generated in htmlcov/index.html

Note: Coverage stills missing but tests are running with test.py django command.

# Build Documentation

Sphinx is configured to build a user friendly site for code documentation.

To build this files run

```
(mission_control_center) $ cd docs
(mission_control_center) $ make html
```

They will be build in docs/build/html/ with index.html as the main page.
It can also be accessed from the admin site in the top navigation.

Note: Docstrings ready for Documentation but adding the library is missing.