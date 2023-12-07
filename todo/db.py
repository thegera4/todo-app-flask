import mysql.connector
import click
import os
# g is a special object that is unique for each request
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions


def get_db():
    if 'db' not in g:
        # create a connection to the mysql database with the connector
        g.db = mysql.connector.connect(
            host=current_app.config["DATABASE_HOST"],
            user=current_app.config["DATABASE_USER"],
            password=current_app.config["DATABASE_PASSWORD"],
            database=current_app.config["DATABASE"]
        )

        # create a cursor to execute queries
        g.c = g.db.cursor(dictionary=True)

    return g.db, g.c


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()


@click.command("init-db")  # define a command line command called init-db
@with_appcontext  # tells flask to call the init_db_command() function and pass the app
def init_db_command():
    init_db()
    click.echo("Database initialized")


def init_app(app):
    # register the close_db() function with the app
    app.teardown_appcontext(close_db)
    # add the command to the app
    app.cli.add_command(init_db_command)
