# app_pasticceria
A simple application with a display case of sweets in Python (flask).

## Commands for execution

### Packages to install:
* sqlalchemy;
* flask; 
* flask-login;
* postgresql;
* psycopg2.

## DBMS creation
We use the following shell commands:
*	sudo su – postgres
*	psql

Once in the interactive PostgreSQL terminal, write the commands listed below:
*	ALTER USER postgres PASSWORD ‘test123’;
*	CREATE USER sofia WITH PASSWORD ‘cioccolato98’;
*	ALTER USER sofia WITH SUPERUSER;
*	CREATE DATABASE mydb;
*	GRANT ALL PRIVILEGES ON DATABASE mydb TO sofia;

To delete the newly created database execute:
*	DROP DATABASE mydb;

To delete the user execute:
*	DROP USER sofia;

Running the app:
* export Flask_APP=app.py
* flask run

## Home page (part 1)
The list with ingredients is visible through overlay.
The default sale date is the current one at the first launch of the application.
![alt text](https://github.com/sofiacrudu/app_pasticceria/blob/main/images/home1.png?raw=true)

## Home page (part 2)
![alt text](https://github.com/sofiacrudu/app_pasticceria/blob/main/images/home2.png?raw=true)

## Login
![alt text](https://github.com/sofiacrudu/app_pasticceria/blob/main/images/login.png?raw=true)

## Backoffice area
![alt text](https://github.com/sofiacrudu/app_pasticceria/blob/main/images/backoffice.png?raw=true)
