from . import bggapi_get
import requests
from bs4 import BeautifulSoup


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


def get_game_info(game_id):
    """Search game by id in a json file, return dictionary with data necessary for the db"""
    #use https://bgg-json.azurewebsites.net/thing/199561

    url = "https://bgg-json.azurewebsites.net/thing/" + str(game_id)
    page = requests.get(url)
    data = page.json()

    #See what we are getting from the internet

    if data.get("name"): #protection against empty entries
        print("Collecting " + str(data.get('name')))
        necessary_data = {
                'title': data.get('name'),
                'id': data.get('gameId'),
                'player_num_min': data.get('minPlayers'),
                'player_num_max': data.get('maxPlayers'),
                'playing_minutes': data.get('playingTime'),
                'mechanics': data.get('mechanics'),
                'coco': None, #will fill in later
                'url': None, #will fill in later
        }

        #Cooperativity must be a separate value
        if 'Cooperative Play' in data.get('mechanics'):
            necessary_data['mechanics'].remove('Cooperative Play')
            necessary_data['coco'] = 'Cooperative'
        else:
            necessary_data['coco'] = 'Competitive'

        #Add game url as on BGG site
        url_dict = create_url_dict()
        if data.get("name") in url_dict.keys(): #check with the dictionary of urls
            necessary_data['url'] = url_dict[data.get('name')]

        return necessary_data


def print_game_data(necessary_data): #takes a dict
    for datum in necessary_data:
        print(datum + ": " + str(necessary_data[datum]))
