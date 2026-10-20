import os
import sqlite3
from flask import Flask, g

SCHEMA = '''
CREATE TABLE IF NOT EXISTS reminders (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL,
 description TEXT NOT NULL DEFAULT '',
 category TEXT NOT NULL DEFAULT 'Pessoal',
 due_at TEXT NOT NULL,
 repeat_rule TEXT NOT NULL DEFAULT 'none',
 completed INTEGER NOT NULL DEFAULT 0,
 created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
'''

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-only-change-me'), DATABASE=os.path.join(app.instance_path, 'applembrer.sqlite3'))
    if test_config:
        app.config.update(test_config)
    os.makedirs(app.instance_path, exist_ok=True)

    def get_db():
        if 'db' not in g:
            g.db = sqlite3.connect(app.config['DATABASE'])
            g.db.row_factory = sqlite3.Row
        return g.db

    @app.teardown_appcontext
    def close_db(error=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    with app.app_context():
        connection = sqlite3.connect(app.config['DATABASE'])
        connection.executescript(SCHEMA)
        connection.close()

    from .routes import bp
    app.register_blueprint(bp)
    app.get_db = get_db
    return app
