# File Flow
This is a small Django web app that enables a user to upload, add and delete contents from a file i.e `json & csv`

<br />
<hr/>

## Project set up
```bash
# clone the repository
$ git clone <project link>

# navigate into the cloned project
$ cd <project name>

# activate the pipenv environment and install dependancies
$ pipenv shell  
$ pipenv install


# set up the migrations for app storage
$ python manage.py makemigrations flows
$ python manage.py migrate

# run application
$ python manage.py runserver



> press CTRL+C to exit server
```

To visit the site [Live link](https://massesment.herokuapp.com/)