# Sleep Shift Scheduling Tool
Operational sleep shift scheduling tool to provide autonomous customization of a schedule for sleep, exercise, and nutrition in order to manage fatigue.

## Getting Started

The backend is a Django project that exposes a REST API.

I recommend using two consoles, with Django in one and Node in the other.

### Backend

Make sure that Python (with pip) is installed.

Navigate to the backend directory, where `manage.py` is located.

```bash
$ cd assessment-platform/backend/
```

Create a virtual environment and enter it.

```bash
$ python -m venv '.env'
$ source .env/Scripts/activate      # Windows
$ source .env/bin/activate          # Linux
```

Install the requirements to your environment. 

```bash
$ pip install -r requirements-base.txt
$ pip install -r requirements-test.txt
```

Migrate your local database and run the server.

```bash
$ python manage.py migrate
$ python manage.py runserver
```

You can now visit the site at `localhost:8000`.

### Frontend

Make sure that Node (with npm and yarn) is installed.

Navigate to the frontend directory, where `package.json` is located.

```bash
$ cd assessment-platform/frontend/
```

Install the requirements to your environment. 

```bash
$ yarn install
```

Run the server.

```bash
$ yarn dev
```

You can now visit the site at `localhost:3000`.

### Storybook

*This is assuming that the frontend has been set up*.

Run the server.

```bash
$ yarn nuxt storybook
```

You can now visit the site at `localhost:3003`.

## Development

### Credentials

You should set up a Django superuser account on your local database.

```bash
$ python manage.py createsuperuser
```

Log in to `localhost:8000/admin/` to access the Django admin panel.

Navigate to `localhost:8000/api/` to interact with the REST API.

### Linting

Linting is essential for maintaining code quality and preventing merge conflicts.

We use opinionated linters: `black` for python, and `ESLint` with `Prettier` for JavaScript. 

They're quite strict, but keep code clean and easy to maintain.

**Backend**

```bash
$ black .
```

**Frontend**

```bash
$ yarn lint         # Check for errors.
$ yarn lint --fix   # Fix errors automatically.
```

### Testing

Unit testing is integral to making sure that your code works. 

This includes making sure that there's no unintended side effects when pushing new code, which would be impossible to detect otherwise.

Django uses `unittest`, the Python standard library for testing. Our Node server is set up with `Jest`.

**Backend**

https://docs.djangoproject.com/en/3.1/topics/testing/

```bash
$ python manage.py test
```

**Frontend**

https://vuejs.org/v2/cookbook/unit-testing-vue-components.html

```bash
$ yarn test
```

### Storybook

Any files under `components/*.stories.js` will be found by the Storybook.

Creating a stories file is quite simple:

```javascript
// MyButton.stories.js
export default { title: 'Button' }

export const primaryButton = () => '<MyButton>Primary Button</MyButton>'
```

## Architecture

### Django + Vue + REST

There's three fundamental pieces to the architecture:

1. **Django** - The backend web server. Provides user authentication and manages the database.

2. **Nuxt (Vue.js)** - The frontend web client. Depends on the backend for data and authentication.

4. **REST API** - The Application Program Interface. Provides a standard way for the frontend to use HTTP requests to create, read, update and delete data.