import os
parentDirectory = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(parentDirectory, 'db.sqlite3')
# absolute path to the directory up one level from where the file dwells
