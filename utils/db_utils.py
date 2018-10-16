import os
import sys
sys.path.append(os.path.dirname(__file__)) #Resolve import problems

import sqlite3
import bggapi_get
from gameinfo import GameInfo

parentDirectory = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(parentDirectory, 'db.sqlite3') # Where the database lives

class DatabaseInit:

    def create_db(self):
        '''
        Create an SQLite3 database.
        '''
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute('DROP TABLE IF EXISTS Games')
        cur.execute('CREATE TABLE Games (title TEXT, id INTEGER, player_num_min INTEGER, player_num_max INTEGER,\
                    playing_minutes INTEGER, coco TEXT, mechanics TEXT, url TEXT)')
                    #coco = cooperative or competitive
        print("Database dropped")
        cur.close()

    def fill_db(self):
        '''
        Fill the DB with all our games, using data from gameinfo.
        '''

        def get_tuple(gd): # make tuple from game dict to feed it to the db easily. mechanics is a string
            if gd.get('mechanics'):
                mechanics = '; '.join(gd.get('mechanics'))
            else:
                mechanics = ''
            return (gd.get('title'), gd.get('id'), gd.get('player_num_min'), gd.get('player_num_max'),\
                    gd.get('playing_minutes'), gd.get('coco'), mechanics, gd.get('url'),)

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        print("Getting titles and IDs from BGG API to fetch info...")
        all_games_dict = bggapi_get.get_game_dict() # ids and titles
        data_to_fill = []

        print("Collecting all games data from bgg-json.azurewebsites.net...")
        for game_id in all_games_dict.keys(): #collect all data from all games to feed it to db, key=name
            one_game_dict = GameInfo().get_game_info(game_id)
            if one_game_dict:
                data_to_fill.append(get_tuple(one_game_dict))

        print("Filling database...")
        stmt = '''
        INSERT OR REPLACE INTO Games (title, id, player_num_min, player_num_max,
        playing_minutes, coco, mechanics, url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cur.executemany(stmt, data_to_fill) #fill in all games

        conn.commit()
        cur.close()
        print("Done!")

    def print_db(self):
        '''
        Prints db in the terminal. A function for debugging.
        '''
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        print('Games:')
        cur.execute('SELECT title, id, player_num_min, player_num_max, playing_minutes, coco, mechanics, url FROM Games')
        for row in cur:
            print(row)
        cur.close()

    def drop_sync(self):
        import time
        start_time = time.time()

        print("Committing droppage and syncing...")
        self.create_db()
        self.fill_db()
        time_elapsed = int(time.time() - start_time)
        print("Elapsed " + str(time_elapsed) + " seconds")

        return time_elapsed


class GetGames:

    def get_by_title(self, game_title):
        '''
        Test function. Take a name and print the tuple with that game info
        '''
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        stmt = "SELECT * FROM Games WHERE title = ?;"
        cur.execute(stmt, (game_title,))
        #Print game info in console
        for row in cur:
            for i in range(len(row)):
                print(row[i])
        cur.close()


    def search_db(self, query):
        '''
        Takes a query of name, exact number of players, playing time, and coco
        (this is a dictionary).
        Searches the database.
        Returns all incidences as a list of tuples, or returns nothing.
        '''
        if not query:
            print("Empty query")
            return -1

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        # Form a request to the db
        stmt = "SELECT * FROM Games WHERE "
        for key in query.keys():
            if key == "player_num":
                stmt = stmt + "player_num_max >= " + query[key] + " AND " +\
                            "player_num_min <= " + query[key] + " AND "
            elif key == "playing_minutes":
                stmt = stmt + "playing_minutes >= " + str(int(query[key]) - 14) + " AND "
                stmt = stmt + "playing_minutes <= " + str(int(query[key]) + 14) + " AND "
            elif key == "coco":
                stmt = stmt + key + " = \"" + query[key] + "\" AND "
            else:
                # it's a title or other arbitrary input. protect against SQL injection
                stmt = stmt + key + " LIKE ? AND "

        print("Retrieving suitable games...")

        # Get data from request
        if query.get("title"):
            title_like = "%" + query["title"] + "%"
            cur.execute(stmt[:-5], (title_like,))
        else:
            cur.execute(stmt[:-5])

        results = [] # a list of tuples

        #Print in console
        for row in cur:
            results.append(row)
            for i in range(len(row)):
                print(row[i])
            print()

        cur.close()

        return results
