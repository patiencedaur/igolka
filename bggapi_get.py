from boardgamegeek import BGGClient

bgg = BGGClient()
my_col = bgg.collection('DarkyLondon', exclude_subtype='boardgameexpansion')
games = my_col.items

def write_file(file_name='gamebase'):
    '''
    Write game names and id in file.
    '''
    with open(file_name, 'w') as f:
        for g in games:
            f.write(g.name + '\t' + str(g.id) + '\r\n') #windows carriage return + new line

def get_game_dict(file_name='gamebase'):
    '''
    Returns a dictionary mapping games to ids.
    '''
    game_dict = {}
    for g in games:
        if g.name not in game_dict:
            game_dict[g.name] = g.id
    return game_dict

def display_coll(file_name='gamebase'):
    '''
    Display in CLI for test.
    '''
    print("My current collection:")
    with open(file_name, 'r') as f:
        print(f.read())
