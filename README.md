# Pyramid Framework test.

Test aplication made with Pyramid/postgresql setup based on  [Cookie-cutter](https://github.com/Pylons/pyramid-cookiecutter-starter) for Pyramid framework.

### Installation

Create the virtual enviroment and Install the dependencies.

```sh
$ inside projec path (before pull)
$ python3 -m venv env
$ env/bin/pip install -e .
```

Create postgresql database called 'kenwin'

```sh
$ psql
$ create database kenwin;
```

upgrade the database using Alembic to last revision.

```sh
$ env/bin/alembic -c development.ini upgrade head
```

Load default data into the database using a script.

```sh
$ env/bin/initialize_kenwin_db development.ini
```
Run the project.

```sh
$ env/bin/pserve development.ini
```
### Usage

Login with dummy data

| field | value |
| ------ | ------ |
| username | basic |
| password | basic |



### Todos

 - Write Tests

License
----

MIT


**Free Software, Hell Yeah!🇨🇴🤟 **

