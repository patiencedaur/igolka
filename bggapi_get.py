from boardgamegeek import BGGClient

bgg = BGGClient()
my_col = bgg.collection('DarkyLondon', exclude_subtype='boardgameexpansion')
games = my_col.items

def get_game_dict():
    '''
    Returns a dictionary mapping games to ids.
    '''
    game_dict = {}
    for g in games:
        if g.id not in game_dict:
            game_dict[g.id] = g.name
    return game_dict
