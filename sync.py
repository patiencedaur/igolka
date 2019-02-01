from utils.db_utils import DatabaseInit

"""
Update the database without dropping first (supply new data).
Uses data from BGG API and bgg-json.azuresites.net
"""

DatabaseInit().sync()
