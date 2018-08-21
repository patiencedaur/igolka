import sqlite3
import scraper

def create_db():
    '''
    Creates an SQLite3 database with all our games, using parsed data and data from the BGG API.
    '''
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS Games')
    cur.execute('CREATE TABLE Games (title TEXT, id INTEGER, player_num_min INTEGER, player_num_max INTEGER,\
                playing_minutes INTEGER, coco TEXT, genre TEXT, mechanics TEXT, url TEXT)')
                #coco = cooperative or competitive

    #Fill table with parsed titles and links
    game_dict = scraper.create_url_dict()
    for k in game_dict.keys():
        cur.execute('INSERT INTO Games (title, url) VALUES (?, ?)', (k, game_dict[k]))
    #cur.execute('INSERT INTO Games (title, id) VALUES (?, ?)', ("Aeon's End", 218417))
    conn.commit()

    print('Games:')
    cur.execute('SELECT title, url FROM Games')
    for row in cur:
        print(row)

    cur.close()

create_db()
