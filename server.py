from flask import Flask, request
import sqlite3


class Database:

    @staticmethod
    def connect(db='quotes.db'):
        return sqlite3.connect(db)

    @staticmethod
    def create_table(conn, name, fields):
        return conn.execute(f'CREATE TABLE {name} {fields}')

    @staticmethod
    def create_quote(conn, name, quote):
        cur = conn.cursor()
        cur.execute('INSERT INTO quotes (name, quote) VALUES (?, ?)', (name, quote))

        conn.commit()

    @staticmethod
    def _construct_new_db():
        Database.create_table(db, 'quotes', '(name TEXT, quote TEXT)')


app = Flask(__name__)

@app.route('/post_quote')
def post_quote():
    db = Database.connect()
    Database.create_quote(db, request.form['name'], request.form['quote'])
    db.close()

    return 'ur pecks r epic\nthanks.. bro'

if __name__ == '__main__':
    app.run()

