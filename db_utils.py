import sqlite3
import gameinfo
import bggapi_get

def create_db():
    '''
    Create an SQLite3 database.
    '''
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Games')
    cur.execute('CREATE TABLE Games (title TEXT, id INTEGER, player_num_min INTEGER, player_num_max INTEGER,\
                playing_minutes INTEGER, coco TEXT, mechanics TEXT, url TEXT)')
                #coco = cooperative or competitive
    cur.close()

def fill_db():
    '''
    Fill the DB with all our games, using data from gameinfo.
    '''

    def get_tuple(gd): # make tuple from game dict to feed it to the db easily, except mechanics - it will be stored separately
        return (gd['title'], gd['id'], gd['player_num_min'], gd['player_num_max'],\
                gd['playing_minutes'], gd['coco'], gd['url'],)

    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    all_games_dict = bggapi_get.get_game_dict() # ids and titles
    data_to_fill = []

    for game_id in all_games_dict.keys(): #collect all data from all games to feed it to db
        one_game_dict = gameinfo.get_game_info(game_id)
        data_to_fill.append(get_tuple(one_game_dict))

    stmt = '''
    INSERT OR REPLACE INTO Games (title, id, player_num_min, player_num_max,
    playing_minutes, coco, url)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''' #Make mechanics referencing another db? Make separate db for mechanics?
    cur.executemany(stmt, data_to_fill) #fill in all games

    #stmt_mech = 'INSERT OR REPLACE INTO Games (mechanics) VALUES (?)'

    conn.commit()
    cur.close()

def print_db():

    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    print('Games:')
    cur.execute('SELECT title, id, player_num_min, player_num_max, playing_minutes, coco,url FROM Games')
    for row in cur:
        print(row)

    cur.close()

fill_db()
print_db()
