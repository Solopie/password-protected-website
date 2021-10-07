# Password Protected Website Template

Template repository to create websites that required a password to access. You may want only certain people to access the website but still want the website to be open publicly.

Built with:

- Python 3
- Flask
- SQLite

## Environment variables

Check out ".env.sample" file

**ENABLE_TOKEN**

- Values: True | False
    - Default: True 
- Description: Enable the password protection

**ACCESS_DB_PATH**
- Values: String of path
    - Default: access.db
- Description: Path of the database file

## Deployment

### Manual

*Should only be used for testing*

Install dependencies 

    pip install -r requirements.txt

Ensure you initialise your SQLite database using the `init.sql` script before running app

    sqlite3 access.db < init.sql

Run `main.py`

    python main.py

Application will be running on port 8000 (or whatever port you have specified in `main.py`)

### Docker

*Docker file coming soon!*
