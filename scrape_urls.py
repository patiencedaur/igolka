import requests
from bs4 import BeautifulSoup
import bggapi_get

def create_url_dict(url='https://boardgamegeek.com/collection/user/DarkyLondon?own=1&subtype=boardgame&ff=1'):
    '''
    Returns a dictionary mapping game names to their links.
    '''
    req = requests.get(url)
    page = req.content
    soup = BeautifulSoup(page, 'html.parser')
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
        if game_name in bggapi_get.get_game_dict().values():
            game_link_dict[game_name] = 'https://boardgamegeek.com' + game_href

    return game_link_dict

print(create_url_dict())
