# API created by Mitchell Zarb | Y12
import sqlite3
import json

sql_command = "select id, name from superhero_modified;"

with sqlite3.connect("SQL/SuperHeroAPI.db") as database:
    cursor = database.cursor()
    cursor.execute(sql_command)

    