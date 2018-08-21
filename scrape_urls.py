import requests
from bs4 import BeautifulSoup
import bggapi_get

def save_page(url='https://boardgamegeek.com/collection/user/DarkyLondon?own=1&subtype=boardgame&ff=1', file_name='collection.html'):
    '''
    Saves page from BGG to disk. Defaults to Darky's collection page.
    '''
    req = requests.get(url)
    #copy html to local
    with open(file_name, 'wb') as my_collection:
        my_collection.write(req.content)


def create_soup_obj(file_name):
    '''
    Input is a html page saved to disk.
    Output is a BeautifulSoup object.
    '''
    with open(file_name, 'r') as col_file:
        col_page = col_file.read()
    return BeautifulSoup(col_page, 'html.parser')


def create_url_dict(file_name='collection.html'):
    '''
    Returns a dictionary mapping game names to their links.
    '''
    soup = create_soup_obj('collection.html') #create soup to parse from
    #find all td class="collection_objectname" - where the name with the link dwells
    table = soup.find_all('td', {'class': 'collection_objectname'})

    game_link_dict = {}

    #Get all game names (including extensions) and corresponding links
    for td in table:
        game_mention = td.find('a')
        game_href = game_mention.get('href')
        #delete javascript mentions
        if 'javascript' in game_href:
            continue
        game_name = game_mention.get_text()
        #Check with api database to remove extensions
        if game_name in bggapi_get.get_game_dict().keys():
            game_link_dict[game_name] = 'https://boardgamegeek.com' + game_href

    return game_link_dict
