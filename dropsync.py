from utils.db_utils import DatabaseInit

"""
Drop and sync (= update) the database.
Uses data from BGG API and bgg-json.azuresites.net
"""

DatabaseInit().drop_sync()
