import json
from bs4 import BeautifulSoup
from scrape_urls import *

''''
Get all info about Darky's games from BGG site, one by one.
'''

def get_game_info(link):
    '''
    Parse the BGG page for game, get info and put it in the tuple.
    link is a str, found in the values of scrape_urls.create_url_dict().
    Returns a dictionary like {title: 'Sagrada', id: 199561, player_num_min: 1, player_num_max: 4,
                 playing_minutes: 30, coco: 'Competitive', genre: 'Abstract',
                 mechanics: ['Dice Rolling', 'Pattern Building'], url: 'http://path.to.game')
    'coco' means 'cooperative or competitive'.
    '''
    game_data_html = 'tempgame.html'
    save_page(url=link, file_name=game_data_html)
    soup = create_soup_obj(game_data_html)

    #use https://bgg-json.azurewebsites.net/thing/199561

    return {}


def make_game_list(game_dict):
    '''
    Returns a list of tuples (title, id(int), player_num_min(int), player_num_max(int),
                 playing_time(int), coco(str), genre(str), mechanics(list of str), url(str)).
    'coco' means 'cooperative or competitive'.
    game_dict is a dict of game names and urls made by scrape_urls.create_url_dict().
    '''
    list_game_rows = []
    for g in game_dict.keys():
        title = g
        url = game_dict[g]
        list_game_rows.append((title, url))
        # add more info from get_game_info(game_dict[k])
