Tecnologie Web - Università degli studi di Napoli Parthenope

SkiHub - Participants:
- Pasqualina Errico | 0124002786 | pasqualina.errico001@studenti.uniparthenope.it
- Musella Antonio | 0124003149 | antonio.musella001@studenti.uniparthenope.it

Technologies used in the project:

- Frontend: HTML, CSS, JavaScript, Jinja2 (Flask)
- Backend: Python Flask Framework
- Database: MySQL Relational Database
- Environment Variables: dotenv

Prerequisites:

- MySQL Community Server (8.0 or higher)
- Python 3.11.9 or higher
- Flask 3.1.2 or higher
- Git
- PyCharm recommended


How to open web app:
1) Install the required version of Python, Flask, and MySQL
2) Create a new database from the MySQL Command Line Client called skihub: "create database skihub;"
3) Clone this git repository and open the terminal in the folder where 'skihub.sql' exists
4) Assuming the command mysql is in the environment variables for your system, use the following command where 'user' and password can be found in the .env file
5) mysql -u 'user' -p skihub < skihub.sql
6) If you dont have PyCharm open the terminal where app.py exists and run python3 app.py and skip to the next step(Assuming the command python is in the environment variables for your system)
7) If you have PyCharm installed, open the project folder and run app.py after selecting the correct interpreter
8) If successful you should get the access url, click it and enjoy!


