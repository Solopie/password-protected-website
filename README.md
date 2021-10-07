# Password Protected Website Template

Template repository to create websites that required a password to access. You may want only certain people to access the website but still want the website to be open publicly.

Built with:

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

*Docker file coming soon!*
