import bggapi_get
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

    necessary_data = {
                'title': data['name'],
                'id': data['gameId'],
                'player_num_min': data['minPlayers'],
                'player_num_max': data['maxPlayers'],
                'playing_minutes': data['playingTime'],
                'mechanics': data['mechanics'],
                'coco': None,
                'url': None, #will fill in later
    }
    #Cooperativity must be a separate value
    if 'Cooperative Play' in data['mechanics']:
        necessary_data['mechanics'].remove('Cooperative Play')
        necessary_data['coco'] = 'Cooperative'
    else:
        necessary_data['coco'] = 'Competitive'

    #Add game url on BGG
    url_dict = create_url_dict()
    if data['name'] in url_dict.keys(): #check with the dictionary of urls
        necessary_data['url'] = url_dict[data['name']]

    return necessary_data


def print_game_data(necessary_data): #takes a dict
    for datum in necessary_data:
        print(datum + ": " + str(necessary_data[datum]))


# data = get_game_info(127398)
# print_game_data(data)
