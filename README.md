# Flask + React Project Template

Project template / boilerplate for a micro-service providing endpoints via Flask (Python) and a frontend via React 
(JavaScript).

**Table of Contents**

1. [Requirements](#requirements)
    1. [Tech Stack](#tech-stack)
2. [Customisation](#customisation)
3. [Installation](#installation)
4. [Running the App](#running-the-app)
    1. [Environment Config](#environment-config)

## Requirements

- Python3.6+
- NodeJS / npm
- MongoDB **or** MySQL

### Tech Stack

**Backend**

- **Flask** framework for hosting API endpoints and delivering the frontend
- **pymongo** for MongoDB access
- **mysql-connector-python** for MySQL access

**Frontend**

- **React** basic framework for the frontend
- **Redux** a global store for the frontend, used for data exchange with the API and to avoid handing down data through
component hierarchies
- **Webpack** and **Babel** to transpile the frontend into a single `index.js`, which gets included by the `index.html`
- **Plotly.JS** a Javascript adaptation of the popular Python charting library Plotly
- **Moment.JS** the standard library for date/time handling in JavaScript
- **S Alert** a basic notification library 
- **ESLint** and **Prettier** for linting Javascript code and auto-format
- Custom **Basic Utilities** and **Style Mixins** (see `frontend/src/util.js` and `frontend/src/mixins.js`)

## Customisation

The following changes should be performed at the beginning of a project based on this repository:

**Choose a Database**

The boilerplate offers support for 2 different databases: MongoDB and MySQL. The following adaptations are required to 
pick one:

- Update the `requirements.txt` and remove the database driver for the database you don't need.
- Update the `config.py` and remove the environment variables for the database you don't need (they're prefixed with 
`MONGO_` or `MYSQL_`).
- Update the `runner.py` and potentially remove the MySQL related connection stuff, if you decide to use MongoDB.
- Create a copy of the `.env.template` file and call it `.env`. This file will be used to load environment variables 
like the database credentials from this file (which is also on `.gitignore`). Remove the database parameters for the 
database you don't need
- Remove the example store of the database you _didn't_ choose from the `storage/` folder.

**Create Stores**

After having chosen a database, you can now start to create stores. We recommend having separate `.py` files for each
table / collection in the `storage/` folder.

The stores are initialised in the `runner.py` and references to these stores are stored in the `stores` dictionary, 
which allows to easily pass all database stores into other components such as API handler or data adapter components.
Clean up the `TODO` items in the `runner.py` and remove traces of the database functions you don't need.

**Remove Example API**

The Flask app provides the following illustrative examples how to access a database, which should be removed to avoid 
confusion:

- `storage/example_mongo_store.py` - an example implementation of a very basic MongoDB collection
- `storage/example_mysql_store.py` - an example implementation of a very basic MySQL table
    - `storage/resources/tables/examples.sql` - table definition for this table
- `api/example_api.py` - example endpoints for getting and creating example entries. Uses MongoDB as example
    - `runner.py` contains the registration of these endpoints (clean up `import` and `register_endpoints` call)
- `frontend/src/redux` - remove the `example.js` and also remove the reference and registration of the Redux store in 
`reducers.js`
- `frontend/src/containers/LandingPage` - remove connection to example store (see the `@connect` section) and remove the
dispatch of the `getExamples()` event in the `componentDidMount()` hook.

**Change Frontend Title**

The template for the index.html is located here: `frontend/index.html`.
Webpack will use that file and inject the script which represents the transpiled frontend. Note: the 
`templates/index.html` is created by Webpack and will be overwritten every time the frontend compiles.

## Installation

First, try to run:

```bash
make install-deps
```

You might have to run it with `sudo`.

That should install the Python (pip) dependencies and Javascript (npm) dependencies.
This assumes, that your Python/Pip binaries are `python3` and `pip3`.

**Manual Installation**

If above doesn't work, install the dependencies separately:

_Javascript:_

```bash
npm install
``` 

_Python:_

```bash
pip install -r requirements.txt
```

## Running the App

If you just want to compile the frontend once and then serve it via the backend (e.g. production mode), simply run:

```bash
npm run build
```

This will produce an index.js containing all the frontend code in the `/static` directory and put the index.html in the 
`/templates` folder. Those 2 directories are used by the Flask app to deliver the frontend components.

The backend's entry point is the script `runner.py` on the root of the project. To run the backend, simply execute:

```bash
make start
```

Again, if your Python binary differs from `python3`, simply run:

```bash
python runner.py
```

(and replace `python` with whatever you use as binary)

- This'll serve the Flask app via: http://localhost:5555

**Frontend Development**

The frontend can be continuously re-compiled whenever you change the code.
In a separate bash window, simply run:

```bash
make frontend
```

Or

```bash
npm run hot-client
```

This will run the `webpack` watcher, which will observe the `/frontend/src` folder for changes and re-compile the 
frontend when changes have occurred. 

In case of compilation errors, this bash window will also tell you what is wrong 
with your code. 

_Do not close this window while you're developing, or you quit the watcher._

### Environment Config

As mentioned before, the Flask app is using an `.env` file to load environment variables which specify database access.
Check the `config.py` for all currently supported environment variables.

You can easily extend this and add getters for additional environment configuration and add those to your `.env` file.
Please provide meaningful defaults for all additional config variables (_except 3rd party service credentials_)
